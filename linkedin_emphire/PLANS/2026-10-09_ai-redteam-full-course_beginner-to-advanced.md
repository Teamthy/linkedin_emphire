# AI RED TEAMING: FULL COURSE, BEGINNER → ADVANCED
Written Fri Oct 9, 2026. For: Olusanya Timothy. Horizon: 24 weeks at 10-12 hrs/wk, BUT the phase audit below decides where you actually start.
Companion: PLANS/2026-10-09_14-day-ai-redteam-crash-course.md = compressed Phase 2. That runs NOW regardless; it is this course's exam week.

## STRUCTURE
Six phases. Each has: SKILLS, LABS, GATE (pass it, move on; gates are practical, not quizzes), and OUTPUT (what the phase adds to your public/repo body of work, because you never study without producing).

====================================================================
## PHASE 0 - PREREQUISITES AUDIT (weeks 0-2) [YOU START HERE, most of this you clear in an evening]
SKILLS: Python (API calls, requests, files, async basics) | CLI + HTTP (curl, status codes, headers) | Git/GitHub | security mental models (CIA triad, authn vs authz, threat surface) | LLM mechanics (tokens, context window, temperature, system vs user turns, embeddings, vector search, RAG, tool calling, streaming)
LABS (self-test - skip anything you pass): build a chatbot from a raw API call in 20 min; build a naive RAG over 20 files; explain to a rubber duck why a system prompt is not access control; use an API token from an env var, not hardcoded.
GATE: all four labs unassisted, under 90 min total.
OUTPUT: prerequisites repo folder. If any lab stalls >30 min, that's your Phase 0 syllabus, 1-2 weeks max.

====================================================================
## PHASE 1 - SECURITY THINKING (weeks 3-6)
SKILLS: threat modeling for AI systems (assets, trust boundaries, attacker personas) | STRIDE adapted | MITRE ATLAS navigation (browse to fluency, not memorization) | OWASP LLM Top 10 (all 10, with your own examples per entry) | NIST AI RMF + GenAI Profile (MAP/MASURE/MANAGE/GOVERN deeply; your bootcamp cert made this familiar, now make it operational) | finding writing (repro, impact, fix, verification - the 4-part format you already invented)
LABS: threat-model 4 systems (your chatbot, your CV pipeline, a Quivly-style post-sale agent from your comment, a fintech bot concept); write 2 full practice reports; map 2 real public incidents (not AI - a classic breach post-mortem) to NIST functions
GATE: a stranger reads one of your threat models and can name the top 3 risks without you present.
OUTPUT: methodology.md + 3 reports in repo. Feeds: your articles' structure, Sudhir deliverables.

====================================================================
## PHASE 2 - CORE ATTACK SKILLS (weeks 7-11) [crash course lives here]
SKILLS: direct injection + jailbreak technique families (instruction override, roleplay, encoding/obfuscation, multilingual, few-shot induction, low-resource language attacks) | indirect injection (RAG corpus, browsing, email/docs, memory poisoning) | extraction (system prompt, retrieved content, fine-tune data if applicable) | exfiltration channels (markdown/URL, tool args, timing) | tool-call attacks (forgery, argument tampering, confirmation bypass, loop induction, denial-of-wallet) | automation (garak probes/buffs, promptfoo redteam, PyRIT intro incl TAP + Crescendo)
LABS: for each class: attack → capture → mitigate → retest → regression-test. Your target set: your bot, your naive agent, 1 CTF arena (Gandalf full ladder + HackAPrompt archive replication)
GATE: take ANY fresh LLM feature you've never seen (your own, rebuilt differently), 2 hours, find ≥3 distinct finding classes + write the report. Speed matters, gates under time.
OUTPUT: the 14-day crash course IS this phase's capstone. findings/ folder = 30+ entries. Feeds: Articles 2-8, all micro proof-of-work.

====================================================================
## PHASE 3 - DEFENSES & CONTROLS (weeks 12-15)
SKILLS: guardrails (Llama Guard, NeMo Guardrails, LLM Guard: what each catches, cost, false-refusal behavior) | architecture patterns (dual-LLM, quarantine, context fencing, human gate design) | identity+permissions for agents (scoped creds, tool allowlists, delegation, revocation, kill switches, circuit breakers, budgets, idempotency) | observability (trace completeness: prompt ver + retrieved chunks + tool calls + PERMISSION STATE at action time) | evals as regression (promptfoo CI gates, golden sets, drift watches) | "controls that fail loudly" doctrine
LABS: harden your bot+agent against your full Phase 2 battery → target: 0 high-severity survives, false-refusal under your set threshold; publish the guardrail eval (rates, not vibes); wire CI; build one dashboard (even a Metabase over logs) that answers "what was the agent allowed to do when it did that?"
GATE: your hardened app survives a fresh 90-min attack session BY YOU (switch hats) with only low-severity findings; then a friend/peer attacks it 30 min - if they break a high in 30, you fail, iterate.
OUTPUT: hardening playbook in repo (this becomes a PAID artifact - your workshop outline materializes here). Feeds: workshop offer ($2k), Sudhir follow-on.

====================================================================
## PHASE 4 - SPECIALIZATION & ADVANCED (weeks 16-21)
SKILLS - core for everyone in this field:
  agentic/MCP security (server trust, tool-description injection, pinning à la Tarique guide, multi-agent trust boundaries, identity propagation, human-approval flow design, lethal-trifecta audits) | supply chain (HF model risks: pickle/remote-code, LoRA poisoning, plugin/marketplace attacks, prompt-file "skills" as vectors) | model-level literacy (adversarial examples/patches FGSM/PGD conceptually, backdoors, extraction attacks, data poisoning at scale, why evals get gamed: reward hacking, benchmark gaming) | automation authorship (write a garak probe yourself; a PyRIT orchestrator; an LLM-as-attacker fuzz loop)
SKILLS - YOUR moat (multimodal/CV):
  adversarial patches/typography against detectors | OCR-as-injection (photo text → agent instructions) | vision→prompt exfil | audio/voice agent surface basics
LABS: mcp-scan a real server + manual tool-desc audit; write your own garak probeset for YOUR app's tool layer; multimodal attack series on your own CV pipeline (1 model, 3 attack classes); build a mini "attacker LLM" loop (PyRIT or DIY) that finds one thing you didn't; one authorized bug-bounty AI target read-through (HackerOne AI programs - READ disclosed reports; only submit if clearly in scope and you'd stake nothing on embarrassment risk)
GATE: one finding from an automated loop or custom probe that you could NOT have found by manual guessing in 2 hours; and your multimodal writeup is good enough that a CV person DMs you about it.
OUTPUT: 2 repos: probes + your MCP checklist. Articles 15-21 fully pre-researched. This is where "AI red teamer" stops being a claim and becomes a niche you visibly own.

====================================================================
## PHASE 5 - PROFESSIONAL PRACTICE (weeks 22-24, then forever)
SKILLS: scoping + rules of engagement (what's fair game, what's a lawsuit) | engagement lifecycle (intake → threat model → test windows → report → remediation re-test → regression handoff) | industry overlays (regulated finance: NIST mapping, audit trails, "prove the control worked that day"; consumer: abuse cases, viral-embarrassment risks; B2B SaaS: multi-tenant leak hunting) | comms (exec summary craft, surviving the CTO pushback) | methodology design (write the plan BEFORE the tools) | teaching (your workshop, your series, conference/meetup talk = Lagos AI meetup?)
LABS: run a COMPLETE professional-style assessment on the hardest target you can legally access (your own production-ish system treated as a client's: contract, scope, timeline, interim comms, final report, re-test); turn Phase 3 playbook into the $2k workshop with slides; deliver one live session (Talent Nation pitch, Learn2Earn community, or internal at Teamart); submit one PR to Tarique's guide (starter checklist, from article 6 plan)
GATE: the client (real or simulated with a peer role-playing a hostile CTO) accepts the report as "professional standard," no rewrites asked for.
OUTPUT: the whole machine: report template + workshop + methodology + public portfolio + the fork credit. At this point the $10k isn't a goal, it's inventory management.

====================================================================
## MASTER RESOURCE STACK (no others without a reason written down first)
- Tarique AI-Red-Teaming-Guide (your fork) - spine, all phases
- OWASP GenAI (genai.owasp.org) LLM Top 10 + Agentic TI - the taxonomy, re-read per phase
- NIST AI RMF 1.0 + Generative AI Profile - Phase 1 & 3 & the regulated-sales edge
- garak (NVIDIA) docs incl writing probes; promptfoo redteam docs; PyRIT docs
- Simon Willison blog archive (injection canon); Johann Rehberger blog (agent exploits)
- MITRE ATLAS (browse to fluency)
- Books: Rehberger "Cybersecurity Attacks - Red Team Strategies" (craft) | Steve Wilson O'Reilly LLM security playbook (defense) | Chip Huyen AI Engineering (shared language with your targets)
- Practice arenas: Lakera Gandalf, HackAPrompt archive, any official AI CTF when live
- Communities (1 hr/wk max): garak discord, OWASP GenAI working sessions, AI Village content

## WEEKLY CADENCE TEMPLATE (10-12 hrs)
2 labs x 2h (Tue/Thu evening) | 1 read x 1h (Sat) | 1 write x 1h (findings or article, Sun) | browse/CTF 1-2h (gap days, optional) | ONE LinkedIn line/day harvested from the work
On client weeks: client work counts as lab time. It always has. That's why you chose this.

## ADVANCED-LEVEL DEFINITION (so "finished" means something)
You are advanced when: (1) you design the assessment, not just run tools; (2) you can price and defend a scope document; (3) you've found something via automation you built; (4) you own a niche (for you: multimodal agents + non-English attack surface + Lagos-built); (5) people send YOU unsolicited target reviews. Track these five; the course ends when all five are checked, not when week 24 arrives.
