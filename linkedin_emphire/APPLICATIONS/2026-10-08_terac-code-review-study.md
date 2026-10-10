# Terac — Software Engineers: Paid Code Review for AI Agent Evaluation
Started: Thursday, 2026-10-08
Platform: terac.com — venture-backed expert network (Antigravity Capital), ~104K panel, pays 90+ countries via PayPal/wallet, $10 min withdrawal. Legit; complaints are screening volume and a glitchy AI interview, not payment.
Rate: $65/hr (their board median is $80/hr — this study is mid-band).
Opportunity: review coding tasks + evaluation harnesses used to benchmark AI agents; verify logic, test cases, structure; think aloud on screen share.
Notes: independent contractor, weekly pay. No H1B/STEM OPT (does not affect us). ID verification = standard platform KYC.

## APPLICATION STEPS (in order)
1. Connect LinkedIn profile
2. ID verification (govt ID; name must match exactly)
3. Short screening interview (AI-led, recorded, glitchy — if it fails, retry, it's known)
4. Then: study sessions, paid on approval

## BIO (paste into "about you" fields)
Backend engineer (Go, Node, TypeScript, Python tooling) who treats code review as a discipline: test adequacy over test count, harness robustness over happy path. I red team LLM features for a living, so I know exactly how an agent games a weak evaluation. I write publicly about AI failure modes (Breaking AI, 21-part series) and run structured adversarial testing on every AI feature I ship.

## THE RUBRIC (this is the study itself — internalize it, it answers any screening question)
What separates a good benchmark task from a bad one, in order of how often teams get it wrong:
1. REALISM — would an engineer plausibly receive this ticket on a Monday? Puzzle-tasks (tricky algorithms with no repo context) measure test-taking, not engineering.
2. TEST ADEQUACY WITHOUT OVERFIT — tests must pass every correct solution and fail every incorrect one. The classic failure: tests that assert an exact implementation, so a valid different approach gets punished. When I check a harness, I ask: would a senior engineer solving this correctly, differently, still pass?
3. SPECIFICATION FAIRNESS — requirements precise enough that a good engineer never has to guess hidden expectations. If a task's difficulty is really just ambiguity, the benchmark measures mind-reading.
4. DIFFICULTY CALIBRATION — does the labeled difficulty match real time-to-solve for a competent engineer? Most harnesses label 4-hour work as 30-minute "easy" because the author wrote the solution.
5. REWARD ROBUSTNESS — can an agent win without solving: reading tests to special-case inputs, hardcoding outputs for sample data, exploiting a fixture? If yes, the metric is gameable and the benchmark is lying.
6. ENVIRONMENT FIDELITY — real dependency versions, realistic repo structure, tests runnable the way a human would run them. Sandboxes that hide half the work measure half the skill.

## LIKELY SCREENING QUESTIONS -> ANSWERS
- "How would you judge whether test cases are sufficient?" -> adequacy-without-overfit (#2) + an example: "I write down what a correct-but-different solution looks like and check the tests still pass it."
- "Experience with eval harnesses?" -> my Breaking AI work is evaluation: fixed known-good examples re-run on every model/prompt change; the chatbot test log (6 attempts, 4 breaks) documented exactly.
- "Comfortable thinking aloud?" -> it's how I write. One post/comment per day this month has been practice.

## EXPECTATIONS + MOVES
- Opportunity-based platform: volume fluctuates. Apply to every software/AI-evaluation study that appears, keep profile tags broad (backend, testing, AI evaluation, code review).
- Study quality feedback is the product: the sharper the delivered review, the more invites. Treat first study as reputation-building; a strong one unlocks recurring higher-rate invitations (their specialist studies run $100-350 per session, sometimes $110+/hr).
- Referral program: up to $1,000 per referred expert who gets paid. Do NOT spam for this. If the Nigerian engineer network grows, share once in a relevant community, that's it.
- NEVER pay anything, ever, on any platform. Wallet -> PayPal withdrawal is the only money flow expected.

## STATUS
- [x] micro1 Zara interview done (Oct 8, pre-deadline)
- [ ] Terac: LinkedIn connect + ID verification
- [ ] Terac: screening interview
- [ ] First study completed -> log pay
- Log results here for the Nov 1 review (income tracker for the $10k goal)

---

## DUE DILIGENCE VERDICT (Oct 8, 6:40 AM WAT)
**Legit and pays: YES.** First-hand withdrawal proof (two cash-outs, incl. M-Pesa same-day), multiple Reddit payment confirmations, work trials documented as paid ("3-hour trial, $90/hr on completion" listing), SF company ~$9M raised, named clients (Maze, Tegus, Listen Labs), Trustpilot 4.4-4.5, public support responses to complaints.

**Honest with friction:** payout delays trace to ID/name mismatch (fix: profile name = exact legal name, not the LinkedIn display name). Screening is heavy and unpaid (budget 15 min max on any screening that isn't a top-rate study).

**HARD RULE: never connect LinkedIn for the referral upload.** The one-star "scam" complaint is specifically about being asked for LinkedIn credentials via the referral app. Plain referral link only.

### THIS STUDY (SWE Coding Benchmarks & RL Environments, $75/hr)
- Fit: over-qualified. The work = judging benchmark tasks and test adequacy; that is his written public expertise (regression set, evals, harness robustness).
- Rate: anchor $75 (range listed $45-75).
- Before trial: confirm "trial paid even if not onboarded?" (their listings say paid-on-completion, get it in writing for this one).
- US/Canada preferred; "exceptional elsewhere" lane = rely on GitHub + written quality.

## PROFILE AUDIT (Oct 8, ~7:05 AM) — CRITICAL
Account: terac.com/u/olusanya-t, email tomicialgraphics@gmail.com (NOT Timothy's known email - flag: change or confirm monitored)
**IMPORTED/UNVERIFIABLE ENTRIES ON PROFILE — must delete before interview unless proven real:**
- Deep Learning Specialist · Asana 2025-Present (overlap with Teamart, unverifiable)
- Creative Director · Corewell Health 2023-2025 (Michigan health system; not his)
- Senior Data Specialist · University of Idaho 2024-2025 (he's a contact there via Kevin Chang, not staff)
- Senior Backend Engineer · Northwind Systems 2018-2019 ("Northwind" = sample-database name)
- Software Engineer · BrightPath Labs 2016-2018
- Independent contract block 2019-Present with unverifiable metrics (10k orders/min crypto, 5M events/day Kafka, 12-entity finance platform)
- Education: Kwara BMLS 2019-2024 + Unilag BSc 2012-2016 (contradicts actual NOUN CS expected Apr 2028)
**Risk: verification fail, payout hold, account loss. Rule on these platforms: verified + modest > impressive + unverifiable.**
FIXES: delete above; rate $75; 2FA on; public profile on; identity verification with exact legal name; full LinkedIn URL; upload RESUME/Timothy_Olusanya_AI_ML_Engineer.pdf
INTERVIEW SCRIPT: saved below (3 blocks + Q&A from actual week; rubric = 6-point list earlier in file)
