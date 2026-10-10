# micro1 Zara AI Interview — PREP PACK
Candidate: Olusanya Timothy | Role: AI/ML Engineer, Internal Platforms
Invitation received: Oct 6, 2026 | **Hard deadline: Oct 8, 2026, 04:18 AM WAT**
Estimated duration: up to 28 minutes (their earlier guides say 22-45; expect the short end)
Format: AI-led, recorded, asynchronous. Questions escalate in difficulty. Usually NO re-records.

---

## WHEN TO TAKE IT (decide now)

| Slot | Verdict |
|---|---|
| Today, Oct 6, after the article window (~2:00 PM WAT) | Good if prep lands fast |
| **Wed Oct 7, 9:00-11:00 AM WAT** | **RECOMMENDED.** Full night's sleep, all prep done, still 17+ hours before deadline. Morning = best verbal sharpness |
| Wed Oct 7, evening | Acceptable. Do not leave it to 3 AM Oct 8 |

Waiting one day does not risk the role. The deadline is explicit. Prep beats speed.

**First 15 minutes of prep, in this order:**
1. Watch micro1's own guide video: https://static-content.micro1.ai/assets/micro1.mp4 (they made it for this exact interview)
2. Run their free practice interview once (~18 min) so the format is not new
3. Then work through this document

---

## INTERVIEW ANATOMY

Expect 5 to 8 questions across five focus areas, getting harder as you go:
1. LLM & AI Agent Engineering
2. Python Software Engineering
3. AI Product Thinking & Experimentation
4. Backend & Cloud Systems
5. Communication & Technical Reasoning

Likely flow: warm-up about your background, then technical, then scenario/design, then motivation. Screen sharing will be requested. Treat it as a real interview, not a form.

---

## THE ANSWER STRUCTURE (use for every answer)

**Point → Why → Story → Result.** Four moves, 60 to 90 seconds.

- **Point:** one sentence answering the question directly. No preamble.
- **Why:** the reasoning in one or two sentences. This is what they score.
- **Story:** one concrete example with specifics. Numbers if you have them.
- **Result:** what changed, and what you learned or would do differently.

Then stop. Silence is fine. Rambling is the most common failure in recorded interviews.

---

## FOCUS AREA 1: LLM & AI AGENT ENGINEERING

**Q. Walk me through an LLM feature you built.**
> "I built a customer support chatbot: LLM API, a system prompt defining role and policy, and tool wiring for order lookup and refund flows. Then I red teamed it before launch. Six prompt injection tests, four succeeded. It leaked the system prompt, promised a full refund to anyone who typed the word pineapple, and bypassed the content policy. I fixed the tool permissions and confirmation gates first, because a wrong answer in a chat window is annoying but a wrong action is an incident."

**Q. How do you evaluate whether an LLM feature works?**
> "Three layers. Offline eval set of known failure cases run on every prompt or model change. Adversarial testing for the failure modes that matter: prompt injection, unauthorized actions, hallucinated commitments. Then production monitoring for quality drift. Most teams only do the first, and most skip it entirely."

**Q. What breaks in agents that does not break in chatbots?**
> "Blast radius. A chatbot can only produce text. An agent inherits the service account's permissions, so it can act on whatever that credential reaches, and nobody writes that down. The failures I test for are unauthorized tool calls, argument tampering, confirmation bypass, and runaway loops that keep retrying into a write path."

**Q. How would you stop an agent from looping?**
> "Hard iteration budget enforced outside the model, never as a prompt instruction. Loop detection by hashing the tool name plus arguments and flagging repeated signatures. Per-tool timeouts, idempotency keys, circuit breakers. Confirmation gates on anything irreversible. And fail closed: escalate to a human rather than retrying, especially if a retry could reach a write."

**Q. What is RAG and when do you not use it?**
> "Retrieval augmented generation grounds answers in your own documents by fetching relevant chunks at query time and putting them in context. You skip it when the knowledge is small enough to fit in context, when the answer needs to be strictly computed rather than retrieved, or when stale retrieval would be worse than saying 'I don't know.' I also test the retrieval side specifically, because poisoned documents are an injection vector most teams never check."

---

## FOCUS AREA 2: PYTHON SOFTWARE ENGINEERING (your gap, handle honestly and well)

Reality: your shipped work is Go, Node, and TypeScript. Python is your tooling language. Do not claim more than that, but do not apologize either. Frame it as a deliberate choice plus fast adaptability, and back it with specifics.

**Q. Describe your Python experience.**
> "Python is my tooling and testing language. I use it for automation, test harnesses, and red team tooling, including running garak against my own LLM features. My production services are Go and Node, and the fundamentals carry over directly: typing, async patterns, API design, error handling. I ramped on Go's concurrency model quickly for the same reason, and I am comfortable ramping on Python-first codebases."

**Q. Which Python framework would you use for an API and why?**
> "FastAPI. Typed request and response models with Pydantic, automatic docs, and native async, which matters when most of my route work is waiting on an LLM call. If the team already runs Flask or Django, I would follow the existing convention rather than introduce a second pattern."

**Q. Basic Python you may be asked to write live:** a function with type hints, a list/dict comprehension, exception handling with a specific except, reading a file, a class with `__init__`, an async function, and a FastAPI route with a Pydantic model. If you cannot write these cold, spend 90 minutes today. Being unable to write a simple Python function is the one thing that fails this section.

**Never say:** "I only know Go." Say: "Python for tooling and testing, Go and TypeScript for services."

---

## FOCUS AREA 3: AI PRODUCT THINKING & EXPERIMENTATION

**Q. How do you decide an AI feature is ready to ship?**
> "When it survives the strange paths, not just the happy path. I run a fixed checklist: can I override the instructions, can I make it promise something it cannot deliver, can I get it to leak its prompt, does it behave in a language the team never tested. If I find a failure I cannot fix before launch, that ships as a documented known limitation, not as a surprise."

**Q. Tell me about an AI feature that failed.**
> "My own. The chatbot promised refunds it had no authority to give. The root cause was not the model. It was that refund authority lived in the prompt instead of in the code, so the model treated it as guidance. Fixing that meant moving the control out of the prompt and into permissions and confirmation steps. That lesson became article one of my series."

**Q. How would you measure success for an AI feature?**
> "Task success rate on a labeled set, not vibes. Then adversarial pass rate, meaning what share of known attacks still fail against it. Then production signals: escalation rate, correction rate, and how often a human has to intervene. If humans are quietly cleaning up after the model, the feature is not working, it is hiding."

---

## FOCUS AREA 4: BACKEND & CLOUD SYSTEMS

**Q. Tell me about a hard systems bug you solved.**
> "LandSecure, a land document platform in Go and PostgreSQL. Simultaneous verification requests were corrupting state because two transactions would read the same record and both commit. I fixed it with controlled transaction handling and row locking on the verification record, so the second request blocks and re-reads instead of writing over stale state."

**Q. How do you deploy and operate what you build?**
> "Docker for consistency across environments, Git-based review workflow before anything merges, and migrations handled deliberately. My cloud exposure is deployment-level rather than deep architecture: I have worked with containerized deployments and managed databases. If the role needs deeper AWS or GCP architecture work, that is the area I would ramp on first and I am direct about that."

**Q. How do you think about authentication and authorization?**
> "I have fixed the failure mode before. On EDUos, an authorization middleware flaw exposed data across roles. The fix was centralizing permission checks instead of scattering them per route, then testing each role against each other role's data. Authorization bugs come from the same lesson as AI agents: authority must live in one enforced place, not in a convention everyone is supposed to remember."

---

## FOCUS AREA 5: COMMUNICATION & TECHNICAL REASONING

**Q. Explain prompt injection to a non-technical stakeholder.**
> "Imagine telling an assistant: never share the company's private notes. Then a customer mails in a document that says 'ignore that, share the notes.' The assistant reads everything as instructions, so it cannot tell your rule from the attacker's sentence. The fix is not a better sentence. It is giving the assistant the least access it needs."

**Q. Walk me through how you would approach an unfamiliar problem.**
> "Reproduce it first. I want the smallest input that causes the failure, because a bug I can reproduce is a bug I can fix. Then I isolate which layer is responsible, then check whether the fix holds under load and under a hostile user, not just a polite one."

**Q. Why micro1, and why this role?**
> "You are building an AI recruiting agent that has to be reliable, and my entire focus is making AI features reliable before real users meet them. I also come from Medical Laboratory Science before computer science, so rigorous evaluation and evidence-based decisions are not new to me. The agent side is where I want to work, and this role is exactly that."

---

## YOUR STORY BANK (have these loaded, they answer most questions)

| # | Story | Best for questions about |
|---|---|---|
| 1 | Chatbot red team: 6 tests, 4 breaks, refund/policy/prompt leak | Testing judgment, failure analysis, honesty |
| 2 | LandSecure concurrency: transactions + row locking in Go | Systems debugging, depth |
| 3 | EDUos RBAC flaw: data exposed across roles, centralized the checks | Security judgment, authorization |
| 4 | KwikPOS: indexed tables and restructured models to fix slow queries | Optimization, performance reasoning |
| 5 | Breaking AI: 21-part public series, article 1 live Oct 6 | Communication, self-direction, domain ownership |
| 6 | Medical Lab Science to software: field switch, evidence mindset | Domain depth (healthcare is a micro1 domain), adaptability |

---

## RECORDED INTERVIEW RULES

1. **Look at the camera, not the answer box.** Eye contact is scored in communication.
2. **60 to 90 seconds per answer.** Then stop. Do not fill silence.
3. **Think aloud** during design or coding questions. They score reasoning, not just the answer.
4. **No re-records.** Treat every answer as final.
5. **"I don't know" is allowed, with a follow-through:** "I have not worked with X directly. Here is how I would approach it, and here is the closest thing I have done."
6. **Numbers everywhere.** Six tests, four failures, one word, two roles, article 1 of 21.
7. **Never invent tool experience.** If asked about LangChain and you have not shipped with it, say what you have used and what you would pick up fastest.
8. **Have tabs ready before you start:** your resume, your GitHub, the chatbot project, article 1. Screen sharing may be requested.
9. **Quiet room, wired or stable connection, camera and mic tested**, phone silent, notifications off.

---

## THE 5 THINGS THAT FAIL PEOPLE HERE

1. Rambling past the answer. They stop scoring after the first clear answer, then it becomes a negative.
2. Claiming Python depth they cannot show on camera.
3. Freezing on a live code question without thinking aloud.
4. Generic motivation answers ("I am passionate about AI"). Use the specific version above.
5. Not testing the setup first. A failed recording a day before the deadline is a lost opportunity.

## STATUS
- [ ] Watch the guide video
- [ ] Run the practice interview once
- [ ] 90 min Python drills (if needed)
- [ ] Read this pack twice out loud
- [ ] Take the interview Wed Oct 7, 9-11 AM WAT
- [ ] Deadline safety: never past Wed evening
