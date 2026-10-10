# RESUME AUDIT + REWRITE PLAN
Date: Tuesday, October 6, 2026
Purpose: rebuild Timothy's resume for (A) the micro1 AI/ML Engineer application, (B) the Oct 28 job hunt, (C) client-facing credibility alongside the Breaking AI series.

---

## VERDICT
Current resume is a competent BACKEND ENGINEER resume. It is the WRONG resume for the current positioning.
For micro1 specifically, it fails the first screening pass: their req requires LLM/AI API experience, agent frameworks (LangChain / LangGraph / LlamaIndex), FastAPI, model evaluation, RAG. None of those appear as experience in the current document.

---

## WHAT'S BROKEN (ranked by damage)

1. **Zero AI content.** LinkedIn positioning = AI red teaming. Resume = "Interests: AI Safety." Missing: the support chatbot build + 6-attempt/4-break injection testing, any RAG work, the Breaking AI series, the red team checklist. This is the entire differentiator.
2. **No employment dates anywhere.** ATS ranks on tenure. Current role vs gap is undeterminable.
3. **No metrics.** "Improved code maintainability", "multiple user roles", "improved query performance under high transaction load" with no before/after.
4. **Company inconsistency.** LinkedIn shows Teamart.inc. Resume shows YKAY ConsultingHub and never mentions Teamart. Recruiters cross-check this.
5. **Python evidence missing.** micro1 is Python-first. All three projects listed are Go/Node/TypeScript. Python appears only in the skills line, unsupported by any project.
6. **Mechanical errors:**
   - "Expected April 2028" detached, floating at top of TECHNICAL SKILLS
   - "Go, NestJS, Next.js" stray mid-line inside KwikPOS section
   - "Backend Engineering & Systems Design — Self-Led Learnin" cut off
   - KwikPOS missing its tech-stack line format used by other projects
7. **Degree end date April 2028** while job hunting. Needs framing (working while finishing), not concealment.

## WHAT'S GOOD (keep and strengthen)
- LandSecure: concurrency handling + DB locking strategy in Go. Real engineering story.
- EDUos: RBAC permission conflict fixed after a data exposure. Security-adjacent, valuable for red teaming narrative.
- KwikPOS: query indexing and data model restructure with a performance outcome.
- Medical Laboratory Science background: asset for micro1 specifically (they recruit healthcare domain experts to train models).
- NIST AI Bootcamp: directly relevant to AI red teaming / NIST AI RMF.

---

## TARGET STRUCTURE (AI-forward, ATS-friendly, one page)

**NAME**
Software Engineer · AI Integration & Red Teaming
Lagos, Nigeria | email | github.com/Teamthy | linkedin.com/in/olusanya-timothy

**SUMMARY (3 lines)**
Software engineer who builds AI features and breaks them before users do. Ships LLM integrations (chatbots, RAG, tool-calling agents) and runs pre-launch red teaming against them. Python and Go backend engineer with production REST API, auth, and data-heavy systems experience. Author of Breaking AI, a public 21-part field guide to shipping AI that survives real users.

**TECHNICAL SKILLS**
- Languages: Python, Go, TypeScript, JavaScript, SQL
- AI/LLM: LLM APIs, prompt engineering, prompt injection testing, RAG pipelines [CONFIRM components], tool/function calling, model evaluation, agent workflows [CONFIRM frameworks]
- Backend: REST APIs, FastAPI [CONFIRM], Node.js, NestJS, Go, JWT auth, RBAC
- Data: PostgreSQL, MongoDB, vector databases [CONFIRM]
- Cloud/DevOps: Docker, Git, [CONFIRM: AWS/GCP/Azure or VPS]
- Security: prompt injection, adversarial testing, LLM threat modeling, NIST AI RMF

**AI SECURITY & RED TEAMING (moved to top for AI roles)**
- Built a customer support chatbot [stack, model, purpose], then ran 6 prompt injection tests before launch. 4 succeeded, exposing a system prompt leak, an unauthorized refund commitment, and a content policy bypass. Implemented fixes and converted the findings into a repeatable test checklist.
- Author, Breaking AI (2026): 21-part technical series documenting reproducible failure modes in shipped AI features. Article 1 published Oct 6, 2026.
- [CONFIRM: RAG work, vector DB work, any client red team engagement]

**ENGINEERING EXPERIENCE**
Senior Developer — YKAY ConsultingHub | [DATES NEEDED]
- [Quantify: how many client products, users served, team size]
- Designed REST APIs and multi-role authentication serving [N] user roles across [N] client-facing products
- [Quantify the modular architecture outcome if possible]

[Teamart.inc entry if separate: role, dates, what it is]

**PROJECTS** (condense to 2 bullets each once metrics are known)
- Nigeria LandSecure (Go, Next.js, PostgreSQL): concurrency handling + DB locking for simultaneous verification requests; document validation with role-based permissions
- EDUos (Node.js, TypeScript, Next.js): multi-role education platform; refactored authorization middleware after RBAC conflicts caused data exposure
- KwikPOS (Go, NestJS, Next.js): POS + inventory; indexed tables and restructured data models to fix slow queries under load

**EDUCATION**
BSc Computer Science — National Open University of Nigeria | Expected April 2028 [CONFIRM start year + whether part-time while working]
Medical Laboratory Science — previous academic background

**CERTIFICATIONS**
NIST AI Bootcamp — AI Risk & Safety Frameworks | AI & Backend Engineering (Udemy) | [dates]

---

## QUESTIONS BLOCKING THE REWRITE (answer these and the PDF gets built in one pass)
1. YKAY dates (start to end, or Present). Relationship to Teamart.inc: same job, freelance, or separate?
2. Any numbers: users, records, requests, response times, team size, time saved, client count.
3. Tool truth: LangChain / LangGraph / LlamaIndex? FastAPI? Cloud actually deployed to?
4. Support chatbot: what it does, stack, who for, did it ship?
5. Retrieval: any embeddings / vector DB work? Which tools?
6. How much Python shipped, honestly?

## MICRO1 KEYWORD TARGETS (their screener reads for these exact terms)
Python, LLM APIs, LangChain, LangGraph, LlamaIndex, FastAPI, AWS/GCP/Azure, RAG, tool calling, model evaluation, prompt engineering, production deployment, agent orchestration, open source contributions.

## DELIVERABLES WHEN UNBLOCKED
- Timothy_Olusanya_AI_ML_Engineer.pdf (micro1-tailored, ATS-safe, one page)
- Timothy_Olusanya_Software_Engineer.pdf (general version for Oct 28 job hunt)
- Matching DOCX so edits stay easy


---

## STATUS (Oct 6, 2026)
- [x] v1 built: Timothy_Olusanya_AI_ML_Engineer.pdf (1 page, ATS-safe) + .docx + build_resume.py
- [x] Dates filled: Teamart.inc July 2025-Present, YKAY Nov 2024-June 2025 (CONFIRM against real records)
- [x] Teamart.inc now on resume, matches LinkedIn
- [ ] Confirm optional keywords (see 2026-10-06_insert-ready-lines_and-fill-ins.md)
- [ ] Add metrics
- [ ] General SWE version after Oct 28 prep
