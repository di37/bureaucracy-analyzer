import os

from dotenv import load_dotenv

_ = load_dotenv()

HR_QUESTIONS = [
    "How many approval levels are required for posting a new job position?",
    "How long does it typically take to approve a new job posting?",
    "Are job postings often delayed due to missing information or approvals?",
    "How many steps are involved from candidate selection to final approval?",
    "How often do you receive incomplete applications that delay the hiring process?",
    "Is there a system in place to provide real-time updates to applicants?",
    "Are background checks and reference verifications automated or manual?",
    "How often are hiring decisions delayed due to unavailability of decision-makers?",
    "Could any steps in the hiring process be automated to reduce manual work?",
    "How often do candidates withdraw due to delays in the hiring process?",
    "Are there any other departments involved in the hiring approvals that are difficult to coordinate with?",
]

FINANCIAL_QUESTIONS = [
    "How many levels of approval are required for travel requests?",
    "How long does it usually take to approve a travel request?",
    "Are there frequent delays in getting travel approvals? If yes, why?",
    "What documents are required for a travel request? Are they digital or paper-based?",
    "How many steps are involved in the purchase of an item?",
    "How often are item purchase requests resubmitted due to missing documents?",
    "Is the purchasing process primarily manual or automated?",
    "How long does it typically take from request submission to item purchase completion?",
    "Are there delays caused by miscommunication or lack of clear information?",
    "Could any part of the travel or purchasing process be streamlined using automation?",
    "Are there any other departments involved in the approvals for travel or purchases that are hard to coordinate with? ",
]

HR_EXAMPLE = f"""Human Resources Department Examples (New Hiring Process)

1.	{HR_QUESTIONS[0]} Example Answers: 3 levels (department head, HR manager, dean).
2.	{HR_QUESTIONS[1]} Example Answers: 7-10 days.
3.	{HR_QUESTIONS[2]} Example Answers: Yes, frequently due to incomplete forms.
4.	{HR_QUESTIONS[3]} Example Answers: 5 steps.
5.	{HR_QUESTIONS[4]} Example Answers: About 30% of the time (i.e., from 10 applications, 3 usually incomplete).
6.	{HR_QUESTIONS[5]} Example Answers: No, updates are communicated manually.
7.	{HR_QUESTIONS[6]} Example Answers: Manual.
8.	{HR_QUESTIONS[7]} Example Answers: About 40% of the time.
9.	{HR_QUESTIONS[8]} Example Answers: Yes, candidate screening and document verification.
10.	{HR_QUESTIONS[9]} Example Answers: 15% of the time.
11.	{HR_QUESTIONS[10]} Example Answers: Yes, finance department for budget confirmation.

Example Analysis:

- Bottleneck: Too many approval levels for job postings and manual background checks.
- Proposed Action: Implement workflow automation for job postings and digital background checks.
- Example Tool: Use Microsoft Power Automate for approvals and a digital verification platform for background checks.
- Expected Improvement: Reduce approval levels from 3 to 1, decrease delays by automating manual steps.
- Bureaucracy Score Before: 14 points
- Bureaucracy Score After: 7 points
- Reduction: 50%"""

FINANCE_EXAMPLE = f"""Financial Department Examples (Travel Request and Item Purchase)

1.	{FINANCIAL_QUESTIONS[0]} Example Answers: 2 levels (department head, finance office).
2.	{FINANCIAL_QUESTIONS[1]} Example Answers: 5-7 days.
3.	{FINANCIAL_QUESTIONS[2]} Example Answers: Yes, due to incomplete supporting documents.
4.	{FINANCIAL_QUESTIONS[3]} Example Answers: Travel form, approval letter; mostly paper-based.
5.	{FINANCIAL_QUESTIONS[4]} Example Answers: 4 steps.
6.	{FINANCIAL_QUESTIONS[5]} Example Answers: About 20% of the time.
7.	{FINANCIAL_QUESTIONS[6]} Example Answers: Primarily manual.
8.	{FINANCIAL_QUESTIONS[7]} Example Answers: 10-15 days.
9.	{FINANCIAL_QUESTIONS[8]} Example Answers: Yes, often due to unclear requirements.
10.	{FINANCIAL_QUESTIONS[9]} Example Answers: Yes, approval and notification processes.
11.	{FINANCIAL_QUESTIONS[10]} Example Answers: Yes, logistics department for vendor verification.

Example Analysis:

- Bottleneck: Manual purchasing process and frequent resubmissions due to missing documents.
- Proposed Action: Digitize purchasing documents and implement a shared platform for tracking requests.
- Example Tool: Use Google Workspace for document digitization and Trello for tracking.
- Expected Improvement: Reduce manual processes and minimize resubmission delays.
- Bureaucracy Score Before: 13 points
- Bureaucracy Score After: 10 points
- Reduction: 23%"""

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-pro-exp-0827"
