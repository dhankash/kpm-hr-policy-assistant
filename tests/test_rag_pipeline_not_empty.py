from __future__ import annotations

import json

from rag import config
from rag.chunker import load_chunks, save_chunks
from rag.document_loader import extract_docx_text, save_clean_text
from rag.embeddings import build_index, index_stats, load_vector_index
from rag.generator import HRPolicyAssistant
from rag.memory import ConversationMemory
from rag.retriever import PolicyRetriever


def rebuild_test_index():
    save_clean_text()
    save_chunks()
    build_index(rebuild=True)


def test_hr_policy_file_and_extraction_are_not_empty():
    assert config.RAW_POLICY_PATH.exists()
    text = extract_docx_text(config.RAW_POLICY_PATH)
    assert len(text) > 10_000
    assert "5.6 Family & Medical Leave" in text


def test_chunks_are_not_empty_and_have_metadata():
    rebuild_test_index()
    chunks = load_chunks()
    assert len(chunks) >= 40
    for chunk in chunks:
        assert chunk["text"]
        assert chunk["chunk_id"]
        assert chunk["section"]
        assert chunk["subsection"]
        assert chunk["title"]


def test_faiss_index_count_matches_chunks():
    rebuild_test_index()
    chunks = json.loads(config.STORAGE_CHUNKS_PATH.read_text(encoding="utf-8"))
    index = load_vector_index()
    ntotal, _ = index_stats(index)
    assert ntotal == len(chunks)


def test_retriever_returns_expected_sections_for_core_questions():
    rebuild_test_index()
    retriever = PolicyRetriever()

    fmla = retriever.retrieve("How does FMLA work?")
    assert len(fmla) >= 3
    assert any(result.chunk["subsection"] == "5.6" for result in fmla[:3])

    late = retriever.retrieve("What happens if I'm late?")
    assert any(result.chunk["subsection"] == "3.2" for result in late[:3])

    remote = retriever.retrieve("Can I work from home?")
    assert any(result.chunk["subsection"] == "3.4" for result in remote[:3])

    ppe = retriever.retrieve("What PPE do I need?")
    assert any(result.chunk["subsection"] in {"6.5", "7.7"} for result in ppe[:3])


def test_overtime_answer_is_grounded_and_not_fallback():
    rebuild_test_index()
    result = HRPolicyAssistant().answer(
        "How does overtime work?", name="Alex", memory=ConversationMemory()
    )
    assert "couldn't locate" not in result.answer
    assert "Section 3.3" in result.answer
    assert result.sources
