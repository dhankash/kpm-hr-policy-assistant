# TEST REPORT

## Evaluation Results
- HITS@1: 1.000
- HITS@3: 1.000
- Intent accuracy: 1.000
- Intent macro F1: 1.000

## Smoke Test Outputs

### How does FMLA work?
- Expected sections: 5.6
- Retrieved sections: 5.6, 5.7, 5.8, 3.7, 5
- Raw scores: `[{"section": "5.6", "raw_score": 0.5161, "vector_score": 0.5161, "keyword_score": 1.0, "metadata_score": 1.5, "confidence": 1.125}, {"section": "5.7", "raw_score": 0.4124, "vector_score": 0.4124, "keyword_score": 0.9288, "metadata_score": 0.6, "confidence": 0.715}, {"section": "5.8", "raw_score": 0.4113, "vector_score": 0.4113, "keyword_score": 0.9092, "metadata_score": 0.6, "confidence": 0.709}]`
- Source citations: Section 5.6 Family & Medical Leave (FMLA); Section 5.7 Maternity Leave; Section 5.8 Paternity Leave
- HITS@1: True
- HITS@3: True
- Intent: expected leave, predicted leave
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- Eligible employees may take up to 12 weeks of unpaid, job-protected leave under the Family and Medical Leave Act (FMLA) for qualifying reasons, including: Birth or adoption of a child; Serious health condition of the employee; Care for a spouse, child, or parent with a serious health condition; Certain military-related needs
- Coordination With Other Leave: FMLA may run concurrently with: Maternity leave (Section 5.7); Paternity leave (Section 5.8); Workers’ compensation leave; PTO or sick leave; Employees should consult HR to understand how different leave types interact.
- Benefits During FMLA: Employees may continue health insurance coverage during FMLA by paying their portion of premiums.
- Leave Duration: Eligible employees may take maternity leave for; Medical recovery (typically 6–8 weeks depending on delivery type); Bonding time under FMLA (up to 12 weeks total leave); Some portions of maternity leave may be paid depending on available PTO or short-term disability benefits.

Sources: Section 5.6 Family & Medical Leave (FMLA); Section 5.7 Maternity Leave; Section 5.8 Paternity Leave

For official interpretation or personal employment situations, contact HR.

Did this answer your question?

### What is the dress code?
- Expected sections: 6.5, 7.7
- Retrieved sections: 6.5, 6.1, 6.2, 6.3, 6.4
- Raw scores: `[{"section": "6.5", "raw_score": 0.5295, "vector_score": 0.5295, "keyword_score": 1.0, "metadata_score": 1.5, "confidence": 1.125}]`
- Source citations: Section 6.5 Dress Code & Personal Protective Equipment (PPE)
- HITS@1: True
- HITS@3: True
- Intent: expected conduct, predicted conduct
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- KPM maintains a dress code to ensure safety, professionalism, and compliance with customer and regulatory requirements.
- Staff and Administrative Employees: Employees in office or administrative roles should dress in business-casual attire. Clothing should be neat, clean, and appropriate for a professional environment.
- Production Employees: Production employees must wear: Company-issued uniforms (if applicable); Steel-toe or composite-toe safety shoes; Safety glasses; Gloves, hearing protection, or other PPE as required; Hairnets or beard nets in designated areas; Loose clothing, jewelry, or accessories that could become entangled in machinery are prohibited.
- Special Requirements: Certain areas of the facility may require additional PPE based on; OSHA regulations; Customer audits; Internal safety assessments; Employees must follow all posted PPE requirements and instructions from supervisors.

Sources: Section 6.5 Dress Code & Personal Protective Equipment (PPE)

For official interpretation or personal employment situations, contact HR.

Did this answer your question?

### What happens if I'm late?
- Expected sections: 10.6, 3.2
- Retrieved sections: 3.2, 10.6, 3.5, 4.3, 9.2
- Raw scores: `[{"section": "3.2", "raw_score": 0.3781, "vector_score": 0.3781, "keyword_score": 1.0, "metadata_score": 1.5, "confidence": 1.125}, {"section": "10.6", "raw_score": 0.261, "vector_score": 0.261, "keyword_score": 0.7913, "metadata_score": 1.4, "confidence": 0.986}]`
- Source citations: Section 3.2 Attendance & Punctuality; Section 10.6 Attendance-Related Discipline
- HITS@1: True
- HITS@3: True
- Intent: expected attendance, predicted attendance
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- Reporting Absences: Employees must notify their supervisor before the start of their shift if they will be absent or late. Notification should occur as early as possible to allow supervisors to adjust staffing. Failure to report an absence may be considered a no-call/no-show, which is a serious violation of company policy.
- Tardiness: Employees are considered tardy if they arrive after their scheduled start time. Repeated tardiness may result in corrective action as outlined in Section 10.
- Unscheduled Absences: Unscheduled absences should be limited to emergencies or unavoidable circumstances. Excessive unscheduled absences may impact performance evaluations and could result in disciplinary action.; Attendance Records; Supervisors maintain attendance records for all employees. Employees may request a review of their attendance history through HR.
- Consistent attendance is essential in automotive manufacturing, where production lines depend on every team member being present and prepared.

Sources: Section 3.2 Attendance & Punctuality; Section 10.6 Attendance-Related Discipline

For official interpretation or personal employment situations, contact HR.

Did this answer your question?

### Can I work from home?
- Expected sections: 3.4, 8.2, 8.3
- Retrieved sections: 3.4, 8.6, 8.2, 8.3, 8.1
- Raw scores: `[{"section": "3.4", "raw_score": 0.3528, "vector_score": 0.3528, "keyword_score": 1.0, "metadata_score": 1.5, "confidence": 1.125}, {"section": "8.2", "raw_score": 0.2074, "vector_score": 0.2074, "keyword_score": 0.0, "metadata_score": 0.8, "confidence": 0.394}]`
- Source citations: Section 3.4 Remote Work (Staff-Only); Section 8.2 Data Privacy and Confidentiality
- HITS@1: True
- HITS@3: True
- Intent: expected remote_work, predicted remote_work
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- While the majority of KPM’s workforce is engaged in hands-on production roles that require on-site presence, certain administrative and support functions may be eligible for remote work arrangements.
- Eligibility: Remote work may be available to employees in roles such as; Human Resources; Accounting and Finance; Procurement; Scheduling and Planning; Engineering (non-production tasks); Administrative support; Production-line employees, maintenance technicians, and logistics personnel are not eligible for remote work due to the nature of their responsibilities.
- Approval Process: Remote work requires supervisor approval and may be granted on a temporary, part-time, or hybrid basis depending on business needs. HR may review remote work arrangements periodically to ensure compliance and effectiveness.
- Expectations for Remote Employees: Employees approved for remote work must: Maintain reliable internet access; Be available during core business hours; Follow all data-security and confidentiality policies (see Section 8); Use company-approved tools and systems; Remain responsive to supervisors and team members; Ensure a safe and distraction-free work environment

Sources: Section 3.4 Remote Work (Staff-Only); Section 8.2 Data Privacy and Confidentiality

For official interpretation or personal employment situations, contact HR.

Did this answer your question?

### What PPE do I need?
- Expected sections: 6.5, 7.7
- Retrieved sections: 7.7, 6.5, 7.9, 7.8, 10.5
- Raw scores: `[{"section": "7.7", "raw_score": 0.4458, "vector_score": 0.4458, "keyword_score": 1.0, "metadata_score": 1.5, "confidence": 1.125}, {"section": "6.5", "raw_score": 0.3754, "vector_score": 0.3754, "keyword_score": 0.9078, "metadata_score": 1.5, "confidence": 1.084}]`
- Source citations: Section 7.7 Personal Protective Equipment (PPE); Section 6.5 Dress Code & Personal Protective Equipment (PPE)
- HITS@1: True
- HITS@3: True
- Intent: expected PPE, predicted PPE
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- Employees must wear required PPE at all times in designated areas.
- Examples include: Safety glasses; Steel-toe or composite-toe shoes; Gloves; Hearing protection; High-visibility vests; Respirators (when required); Supervisors will communicate PPE requirements and ensure employees have access to necessary equipment.
- PPE requirements vary by department and task.
- Production Employees: Production employees must wear: Company-issued uniforms (if applicable); Steel-toe or composite-toe safety shoes; Safety glasses; Gloves, hearing protection, or other PPE as required; Hairnets or beard nets in designated areas; Loose clothing, jewelry, or accessories that could become entangled in machinery are prohibited.

Sources: Section 7.7 Personal Protective Equipment (PPE); Section 6.5 Dress Code & Personal Protective Equipment (PPE)

For official interpretation or personal employment situations, contact HR.

Did this answer your question?

### What is the drug policy?
- Expected sections: 6.3
- Retrieved sections: 6.3, 6.10, 6.2, 1.3, 6.1
- Raw scores: `[{"section": "6.3", "raw_score": 0.4549, "vector_score": 0.4549, "keyword_score": 1.0, "metadata_score": 1.5, "confidence": 1.125}]`
- Source citations: Section 6.3 Drug & Alcohol Policy
- HITS@1: True
- HITS@3: True
- Intent: expected conduct, predicted conduct
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- Drug and Alcohol Testing: Testing may be required; Pre-employment; Post-accident; When reasonable suspicion exists; Randomly (for safety-sensitive positions); Employees who refuse testing may be subject to disciplinary action.
- Prohibited Behavior: Employees may not: Use, possess, or distribute illegal drugs on company property; Report to work under the influence of drugs or alcohol; Consume alcohol during work hours or breaks; Misuse prescription medications
- Prescription Medications: Employees taking prescribed medications that may impair performance must notify HR or their supervisor. KPM will work with the employee to determine appropriate accommodations.
- Because KPM operates in a safety-sensitive automotive manufacturing environment, maintaining a drug- and alcohol-free workplace is essential.

Sources: Section 6.3 Drug & Alcohol Policy

For official interpretation or personal employment situations, contact HR.

Did this answer your question?

### How do performance reviews work?
- Expected sections: 9.3
- Retrieved sections: 9.3, 9.4, 9.8, 7.8, 9.1
- Raw scores: `[{"section": "9.3", "raw_score": 0.5952, "vector_score": 0.5952, "keyword_score": 1.0, "metadata_score": 1.4, "confidence": 1.117}]`
- Source citations: Section 9.3 Performance Reviews
- HITS@1: True
- HITS@3: True
- Intent: expected performance, predicted performance
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- Review Components: Performance reviews typically include: Job knowledge and technical skills; Quality of work and attention to detail; Productivity and efficiency; Safety compliance and incident history; Attendance and reliability; Teamwork and communication; Initiative and problem-solving; Adherence to company values; Supervisors may also consider customer feedback, audit results, and production metrics when evaluating performance.
- KPM conducts annual performance reviews for all employees.
- These reviews provide a formal opportunity to evaluate performance, discuss accomplishments, and identify areas for improvement.
- During the review meeting, supervisors will: Discuss performance ratings; Provide examples of strengths and improvement areas; Review goals for the upcoming year; Discuss training or development opportunities; Answer employee questions; Employees are encouraged to actively participate in the discussion.

Sources: Section 9.3 Performance Reviews

For official interpretation or personal employment situations, contact HR.

Did this answer your question?

### How does overtime work?
- Expected sections: 3.3
- Retrieved sections: 3.3, 2.1, 4.5, 3.5, 2.1
- Raw scores: `[{"section": "3.3", "raw_score": 0.5599, "vector_score": 0.5599, "keyword_score": 1.0, "metadata_score": 1.5, "confidence": 1.133}]`
- Source citations: Section 3.3 Overtime
- HITS@1: True
- HITS@3: True
- Intent: expected overtime, predicted overtime
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- Due to the nature of automotive manufacturing, overtime may be required to meet customer deadlines, respond to increased demand, or recover from production disruptions.
- Eligibility: Non-exempt employees are eligible for overtime pay at 1.5 times their regular hourly rate for hours worked over 40 in a workweek.; Exempt employees are not eligible for overtime compensation.
- Overtime Approval: All overtime must be pre-approved by a supervisor. Unauthorized overtime may result in disciplinary action, even if the hours were worked.; Mandatory Overtime; In certain situations—such as urgent customer orders, equipment downtime recovery, or supply chain delays—mandatory overtime may be required. Supervisors will provide as much notice as possible.
- Weekend or holiday overtime may be scheduled during peak automotive production cycles.

Sources: Section 3.3 Overtime

For official interpretation or personal employment situations, contact HR.

Did this answer your question?

### What if my paycheck is wrong?
- Expected sections: 4.5
- Retrieved sections: 4.5, 4.1, 4.2, 4.4, 4.3
- Raw scores: `[{"section": "4.5", "raw_score": 0.365, "vector_score": 0.365, "keyword_score": 1.0, "metadata_score": 1.5, "confidence": 1.125}, {"section": "4.1", "raw_score": 0.3679, "vector_score": 0.3679, "keyword_score": 0.3257, "metadata_score": 0.95, "confidence": 0.633}]`
- Source citations: Section 4.5 Pay Adjustments and Corrections; Section 4.1 Pay Schedule
- HITS@1: True
- HITS@3: True
- Intent: expected payroll, predicted payroll
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- If an employee believes there is an error in their pay, they should notify Payroll immediately.
- Common issues may include: Incorrect hours; Missing overtime; Incorrect deductions; Missing shift differentials; KPM will investigate and correct verified errors as quickly as possible, typically within the next pay cycle.; Overpayments; If an overpayment occurs, KPM will work with the employee to establish a reasonable repayment plan. Employees are expected to cooperate fully in resolving overpayments.
- KPM strives to ensure that all employees are paid accurately and on time.
- Any discrepancies should be reported to the Payroll Department within five business days of receiving the statement.

Sources: Section 4.5 Pay Adjustments and Corrections; Section 4.1 Pay Schedule

For official interpretation or personal employment situations, contact HR.

Did this answer your question?

### What happens for no-call/no-show?
- Expected sections: 10.6, 3.2
- Retrieved sections: 10.6, 3.2, 3.5, 10.8, 3.4
- Raw scores: `[{"section": "10.6", "raw_score": 0.2246, "vector_score": 0.2246, "keyword_score": 1.0, "metadata_score": 1.5, "confidence": 1.125}, {"section": "3.2", "raw_score": 0.2746, "vector_score": 0.2746, "keyword_score": 0.4562, "metadata_score": 1.5, "confidence": 0.88}]`
- Source citations: Section 10.6 Attendance-Related Discipline; Section 3.2 Attendance & Punctuality
- HITS@1: True
- HITS@3: True
- Intent: expected attendance, predicted attendance
- Status: PASS

Final chatbot answer:

Hi Alex, based on the KPM HR Policy Manual, here's what I found:

- Attendance expectations are outlined in Section 3. Violations may include: Excessive tardiness; Unscheduled absences; No-call/no-show incidents; Leaving work early without approval; A single no-call/no-show may result in immediate disciplinary action.
- Reporting Absences: Employees must notify their supervisor before the start of their shift if they will be absent or late. Notification should occur as early as possible to allow supervisors to adjust staffing. Failure to report an absence may be considered a no-call/no-show, which is a serious violation of company policy.
- Tardiness: Employees are considered tardy if they arrive after their scheduled start time. Repeated tardiness may result in corrective action as outlined in Section 10.
- Unscheduled Absences: Unscheduled absences should be limited to emergencies or unavoidable circumstances. Excessive unscheduled absences may impact performance evaluations and could result in disciplinary action.; Attendance Records; Supervisors maintain attendance records for all employees. Employees may request a review of their attendance history through HR.

Sources: Section 10.6 Attendance-Related Discipline; Section 3.2 Attendance & Punctuality

For official interpretation or personal employment situations, contact HR.

Did this answer your question?
