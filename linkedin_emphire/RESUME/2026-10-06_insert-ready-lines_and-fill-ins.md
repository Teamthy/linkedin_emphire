# Resume v1 — what's in it, what's deliberately missing, and what to confirm
Date: Tuesday, October 6, 2026
Files: Timothy_Olusanya_AI_ML_Engineer.pdf (send this one) + .docx (editable twin)
Generator: build_resume.py (rerun after edits, one command)

---

## WHAT THIS VERSION DOES
Reorders your story for AI/ML roles: AI Security & Red Teaming sits at the top, above generic backend work, and everything is written in the exact terms micro1's screeners look for. No claims you can't defend in an interview.

## DELIBERATELY NOT IN IT (do not add until you confirm)
These are the micro1 keywords that would jump this resume a full tier. I left them out because I can't verify them. Confirm any of them and I insert the line in one pass:

| If this is true | Insert this exact line under TECHNICAL SKILLS or use it in bullets |
|---|---|
| Used LangChain / LangGraph / LlamaIndex | `AI Frameworks: LangChain, LlamaIndex, agent orchestration` |
| Used FastAPI | `Backend: REST APIs (FastAPI), Node.js, NestJS, Go` |
| Deployed to AWS / GCP / Azure | `Cloud: AWS (EC2, S3, Lambda)` (adjust to your real services) |
| Used a vector DB (Pinecone, pgvector, FAISS, Weaviate) | `Data: PostgreSQL, MongoDB, vector databases (FAISS)` |
| Built retrieval / embeddings into a product | Add bullet under AI Security: `Built and tested a retrieval-augmented pipeline: ingestion, embeddings, retrieval quality evaluation, and injection testing against poisoned documents.` |
| Python shipped in a real project (not just scripts) | Add to the chatbot bullet: `(Python, LLM API)` and add a Python line to any project's stack line |

## DATES FILLED IN (Oct 6) — VERIFY THESE BEFORE SENDING
Chosen structure: two years, continuous, no gaps, no overlap. Teamart.inc now matches LinkedIn.

| Role | Dates used | Why this shape |
|---|---|---|
| Software Engineer, AI Integration & Red Teaming — Teamart.inc | July 2025 - Present | Matches the Teamart.inc entry on LinkedIn. Currently active, so the AI work reads as your present job |
| Senior Developer — YKAY ConsultingHub | Nov 2024 - June 2025 | Ends exactly where Teamart begins. No overlap, no gap |

Window covered: Nov 2024 to Oct 2026 = two years of continuous work.

**Why you must confirm:** employment dates are the one field an employer can verify with a phone call, and a mismatch costs the offer after the interview. This structure is what reads best. It is only safe if it is also true.

**How to check yours in 2 minutes (in order of reliability):**
1. First commit or PR in each company's repo (`git log --reverse` or GitHub activity history)
2. First invoice or payment received (bank statement, Paystack/Wise history)
3. Contract or offer letter (email search: company name + offer or contract)
4. Onboarding email, Slack or Discord join date
5. Oldest message in the company WhatsApp/Slack thread

If either real start date is different, tell me the two numbers and I rebuild both files in seconds. If YKAY is still active, say so, and we present it as ongoing freelance alongside Teamart instead of ending it in June 2025.

**Quick sanity checks:** does Nov 2024 sit after your Medical Lab Science chapter ended? Does July 2025 line up with when the AI work actually started?

## ADD NUMBERS IF YOU HAVE THEM (highest leverage upgrade)
Every number moves this from "competent" to "hired". Even rough figures work:
1. Roughly how many users or clients did the YKAY products serve?
2. How many user roles or permission levels in the auth system?
3. Team size you reviewed code for?
4. KwikPOS query improvement: before and after (even "slow to under a second" works)?
5. LandSecure: how many documents or how much concurrency?
6. Chatbot: whose was it, did it ship, how many conversations?

## HOW TO REGENERATE
Edit the text values inside `build_resume.py`, then:
```
cd /home/user/linkedin_emphire/RESUME && python3 build_resume.py
```
Both the PDF and the DOCX rebuild together.

## WHY THE AI SECTION IS FIRST
micro1's screener reads for: Python, LLM APIs, LangChain/LangGraph/LlamaIndex, FastAPI, AWS/GCP/Azure, RAG, tool calling, model evaluation, prompt engineering, production deployment, open source, agent orchestration. The summary and top section now carry LLM APIs, prompt engineering, tool calling, model evaluation, prompt injection, and production failure modes. The framework and cloud keywords are the gap, and they are the table above.

## SECOND VERSION TO BUILD LATER (after Oct 28 prep)
`Timothy_Olusanya_Software_Engineer.pdf` — general version for the job hunt. Same facts, backend/full-stack framing first, AI section second. Build it when the AI version is filled in, so both come from the same verified facts.

## ALSO WANTED (for the next iteration)
- A portfolio URL if the Breaking AI series gets a home page. Right now the series has no single link. Article 1's published URL works as a proxy until then.
- Add the article link to the resume header line once Article 1 is live today: `breaking AI series: [article URL]`
