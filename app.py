"""Browser UI and smoke test entry point for the KPM HR Policy Assistant."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from rag import config
from rag.chunker import load_chunks, save_chunks
from rag.document_loader import extract_docx_text, save_clean_text
from rag.embeddings import build_index, ensure_index, index_stats, load_vector_index
from rag.generator import HRPolicyAssistant
from rag.memory import ConversationMemory
from rag.retriever import PolicyRetriever


SMOKE_QUESTIONS = [
    ("How does FMLA work?", {"5.6"}),
    ("What happens if I'm late?", {"3.2", "10.6"}),
    ("Can I work from home?", {"3.4"}),
    ("What PPE do I need?", {"6.5", "7.7"}),
    ("What is the drug policy?", {"6.3"}),
    ("How does overtime work?", {"3.3"}),
    ("What if my paycheck is wrong?", {"4.5"}),
    ("How do performance reviews work?", {"9.3"}),
]


def rebuild_pipeline() -> str:
    save_clean_text()
    save_chunks()
    meta = build_index(rebuild=True)
    return (
        f"Rebuilt {meta['chunk_count']} chunks using {meta['backend']} "
        f"embeddings and {meta['index_backend']} index."
    )


def ensure_pipeline() -> None:
    ensure_index()


def debug_rag(test_query: str = "How does FMLA work?") -> None:
    print("Resolved project root:", config.PROJECT_ROOT)
    print("HR policy file path:", config.RAW_POLICY_PATH)
    print("HR policy file exists:", config.RAW_POLICY_PATH.exists())
    if config.RAW_POLICY_PATH.exists():
        print("HR policy file size:", config.RAW_POLICY_PATH.stat().st_size)
    extracted = extract_docx_text(config.RAW_POLICY_PATH)
    print("Extracted text character count:", len(extracted))
    print("First 500 characters of extracted text:")
    print(extracted[:500])

    save_clean_text()
    save_chunks()
    chunks = load_chunks()
    print("Number of chunks created:", len(chunks))
    print("First 3 chunk IDs/titles:")
    for chunk in chunks[:3]:
        print(f"- {chunk['chunk_id']} | Section {chunk['subsection']} | {chunk['title']}")

    meta = ensure_index()
    index = load_vector_index()
    ntotal, dimension = index_stats(index)
    print("FAISS vector count:", ntotal)
    print("Embedding dimension:", dimension)
    print("Index metadata:", json.dumps(meta, indent=2))

    retriever = PolicyRetriever()
    print("Test query:", test_query)
    raw_results = retriever.raw_vector_search(test_query, top_k=5)
    print("Top 5 raw FAISS results with scores/distances:")
    for result in raw_results[:5]:
        print(
            f"- raw={result.raw_score:.4f} vector={result.vector_score:.4f} "
            f"keyword={result.keyword_score:.4f} | Section {result.chunk['subsection']} "
            f"{result.chunk['title']} | {result.chunk['chunk_id']}"
        )

    final_results = retriever.retrieve(test_query, top_k=5)
    print("Top 5 final retrieved chunks after filters:")
    for result in final_results[:5]:
        print(
            f"- confidence={result.confidence:.4f} raw={result.raw_score:.4f} "
            f"vector={result.vector_score:.4f} keyword={result.keyword_score:.4f} "
            f"metadata={result.metadata_score:.4f} | Section {result.chunk['subsection']} "
            f"{result.chunk['title']} | {result.chunk['chunk_id']}"
        )

    answer = HRPolicyAssistant(retriever=retriever).answer(
        test_query, name="Alex", memory=ConversationMemory()
    )
    print("Final answer:")
    print(answer.answer)


def sources_markdown(sources: list[dict]) -> str:
    if not sources:
        return "No source sections retrieved."
    lines = ["### Retrieved Sources"]
    for source in sources:
        lines.append(
            f"- **Section {source['subsection']} {source['title']}**  \n"
            f"  `{source['chunk_id']}` | confidence {source['confidence']}  \n"
            f"  {source['snippet']}"
        )
    return "\n".join(lines)


def run_smoke_test(write_report: bool = True) -> list[dict]:
    ensure_pipeline()
    assistant = HRPolicyAssistant()
    memory = ConversationMemory()
    outputs: list[dict] = []
    for question, expected_sections in SMOKE_QUESTIONS:
        result = assistant.answer(question, name="Alex", memory=memory)
        top3 = result.retrieved_sections[:3]
        hit = bool(expected_sections & set(top3))
        raw_scores = [
            {
                "section": source.get("subsection"),
                "raw_score": source.get("raw_score"),
                "vector_score": source.get("vector_score"),
                "keyword_score": source.get("keyword_score"),
                "metadata_score": source.get("metadata_score"),
                "confidence": source.get("confidence"),
            }
            for source in result.sources
        ]
        item = {
            "question": question,
            "expected_sections": sorted(expected_sections),
            "retrieved_sections": result.retrieved_sections,
            "raw_scores": raw_scores,
            "top3_hit": hit,
            "status": "PASS" if hit and "couldn't locate" not in result.answer else "FAIL",
            "answer": result.answer,
            "sources": result.sources,
        }
        outputs.append(item)
        print("=" * 80)
        print(f"User question: {question}")
        print(f"Retrieved sections: {', '.join(result.retrieved_sections) or 'None'}")
        print(f"Raw scores: {json.dumps(raw_scores)}")
        print(f"Expected section appeared in top 3: {hit}")
        print(f"Status: {item['status']}")
        print("Final chatbot answer:")
        print(result.answer)

    if write_report:
        write_test_report(outputs)
    return outputs


def write_test_report(smoke_outputs: list[dict]) -> Path:
    metrics = None
    results_path = config.EVALUATION_DIR / "results.json"
    if results_path.exists():
        metrics = json.loads(results_path.read_text(encoding="utf-8"))

    lines = ["# TEST REPORT", ""]
    if metrics:
        lines.extend(
            [
                "## Evaluation Results",
                f"- HITS@1: {metrics.get('hits_at_1', 0):.3f}",
                f"- HITS@3: {metrics.get('hits_at_3', 0):.3f}",
                f"- Intent accuracy: {metrics.get('intent_accuracy', 0):.3f}",
                f"- Intent macro F1: {metrics.get('intent_macro_f1', 0):.3f}",
                "",
            ]
        )

    lines.extend(["## Smoke Test Outputs", ""])
    for item in smoke_outputs:
        source_citations = [
            f"Section {source['subsection']} {source['title']}" for source in item["sources"]
        ]
        lines.extend(
            [
                f"### {item['question']}",
                f"- Retrieved sections: {', '.join(item['retrieved_sections']) or 'None'}",
                f"- Raw scores: `{json.dumps(item['raw_scores'])}`",
                f"- Source citations: {'; '.join(source_citations) or 'None'}",
                f"- Expected section appeared in top 3: {item['top3_hit']}",
                f"- Status: {item['status']}",
                "",
                "Final chatbot answer:",
                "",
                item["answer"],
                "",
            ]
        )

    report_path = config.PROJECT_ROOT / "TEST_REPORT.md"
    report_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return report_path


def build_interface():
    import gradio as gr

    ensure_pipeline()
    assistant = HRPolicyAssistant()

    def submit(user_message, chat_history, memory_state, name):
        if not user_message or not user_message.strip():
            return chat_history, memory_state, "", "Enter a question to search KPM policies.", ""
        memory = ConversationMemory.from_state(memory_state)
        result = assistant.answer(user_message, name=name, memory=memory)
        chat_history = (chat_history or []) + [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": result.answer},
        ]
        return (
            chat_history,
            memory.to_state(),
            "",
            "Searched KPM policies.",
            sources_markdown(result.sources),
        )

    def quick_submit(question, chat_history, memory_state, name):
        return submit(question, chat_history, memory_state, name)

    def clear_chat():
        return [], [], "Conversation cleared.", "No source sections retrieved."

    def rebuild():
        status = rebuild_pipeline()
        return status

    with gr.Blocks(title="KPM HR Policy Assistant") as demo:

    # -------------------------
    # HEADER
    # -------------------------
      gr.Markdown(
          "## 👋 Welcome to the KPM HR Policy Assistant\n"
          "I can answer questions about KPM HR policies using the official HR manual and show the source sections.\n\n"
          "**Please begin by entering your name in the Name field above the chat.**"
      )

      memory_state = gr.State([])

      # -------------------------
      # NAME + STATUS
      # -------------------------
      with gr.Row():
          name = gr.Textbox(label="Name", value="Alex", scale=1)
          status = gr.Textbox(
              label="Status",
              value="Ready to search KPM policies.",
              interactive=False,
              scale=2
          )

      # -------------------------
      # CHATBOT + SOURCES
      # -------------------------
      chatbot = gr.Chatbot(label="Chat", type="messages", height=430, allow_tags=False)
      sources = gr.Markdown("No source sections retrieved.", label="Source Citations")

      # -------------------------
      # ASK-A-QUESTION ROW
      # -------------------------
      with gr.Row():
          message = gr.Textbox(
              label="Ask a question",
              placeholder="Example: How does FMLA work?",
              scale=5,
          )
          send = gr.Button("Send", variant="primary", scale=1)

      # -------------------------
      # ACCORDION 1 — QUICK QUESTIONS
      # -------------------------
      quick_questions = [
          "How does FMLA work?",
          "What happens if I'm late?",
          "Can I work from home?",
          "What PPE do I need?",
          "What is the dress code?",
          "What is the drug policy?",
          "How does overtime work?",
          "What if my paycheck is wrong?",
          "How do performance reviews work?",
      ]

      with gr.Accordion("Quick Questions", open=False):
          with gr.Column():
              for question in quick_questions:
                  gr.Button(question).click(
                      quick_submit,
                      inputs=[gr.State(question), chatbot, memory_state, name],
                      outputs=[chatbot, memory_state, message, status, sources],
                  )

      # -------------------------
      # ACCORDION 2 — BROWSE BY TOPIC
      # -------------------------
      topic_buttons = [
          "1. Introduction & Company Overview",
          "2. Employment Policies",
          "3. Work Hours, Attendance & Scheduling",
          "4. Compensation & Payroll",
          "5. Benefits & Leave Policies",
          "6. Workplace Conduct & Expectations",
          "7. Health, Safety & Compliance",
          "8. Technology & Data Policies",
          "9. Performance Management",
          "10. Disciplinary Action & Termination",
      ]

      with gr.Accordion("Browse by Topic (Main Headings)", open=False):
          with gr.Column():
              for topic in topic_buttons:
                  gr.Button(topic).click(
                      quick_submit,
                      inputs=[gr.State(f"Tell me about {topic}"), chatbot, memory_state, name],
                      outputs=[chatbot, memory_state, message, status, sources],
                  )

      # -------------------------
      # CLEAR + REBUILD BUTTONS
      # -------------------------
      with gr.Row():
          clear = gr.Button("Clear conversation")
          rebuild_button = gr.Button("Rebuild index")

      # -------------------------
      # EVENT BINDINGS
      # -------------------------
      send.click(
          submit,
          inputs=[message, chatbot, memory_state, name],
          outputs=[chatbot, memory_state, message, status, sources],
      )

      message.submit(
          submit,
          inputs=[message, chatbot, memory_state, name],
          outputs=[chatbot, memory_state, message, status, sources],
      )

      clear.click(clear_chat, outputs=[chatbot, memory_state, status, sources])
      rebuild_button.click(rebuild, outputs=[status])

    return demo



def main() -> None:
    parser = argparse.ArgumentParser(description="Run the KPM HR Policy Assistant.")
    parser.add_argument("--smoke-test", action="store_true", help="Run chatbot pipeline without launching Gradio.")
    parser.add_argument("--debug-rag", action="store_true", help="Print hard RAG diagnostics and one sample answer.")
    parser.add_argument("--debug-query", default="How does FMLA work?", help="Question to use with --debug-rag.")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild the policy index before launching.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=7860)
    args = parser.parse_args()

    if args.rebuild:
        print(rebuild_pipeline())

    if args.debug_rag:
        debug_rag(args.debug_query)
        return

    if args.smoke_test:
        run_smoke_test(write_report=True)
        return

    demo = build_interface()
    demo.launch(server_name=args.host, server_port=args.port, share=True)


if __name__ == "__main__":
    main()
