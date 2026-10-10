# 21 AI RED TEAMING ARTICLES — REALISTIC PLAN (reset Oct 2, 2026)
Status: ZERO published. Plan built for sustainability, not aspirational sprints.
Series tagline on LinkedIn: "21 tests I ran on my own AI systems, so you don't ship the failures I found."

═══════════════════════════════════════════════════════
GROUND RULES (so you don't burn out and quit at article 3)
═══════════════════════════════════════════════════════
1. AUDIENCE: Working software engineers shipping AI features. Not security teams, not academics, not executives. Every article answers "what do I do Monday morning?"
2. LENGTH: 800-1200 words per article. No essays. Scannable, bullet points, real prompts/commands, no fluff.
3. CADENCE: 2 articles per week, published TUESDAY + FRIDAY at 10am WAT. Tuesday = deep dive. Friday = actionable checklist/playbook. That is 2/week for 11 weeks, finishing mid-December. No 3/week cram sessions.
4. RESEARCH RULE: Every article comes from a REAL TEST you run on your own AI systems (or free public models) — no theory without proof. Max 2 hours of testing per article. No $1000 cloud bills, no special certs.
5. REPEATABLE ARTICLE STRUCTURE (no blank-page anxiety — every article follows this):
   1. Opener: personal war story (something you broke that week, 1-2 paragraphs)
   2. What the vulnerability actually is (plain English, no jargon)
   3. How you tested it (step by step, exact prompts/commands, so readers can copy)
   4. What worked to fix it (3-4 concrete controls, no "buy X tool" pitches)
   5. 5-point checklist readers can steal
   6. PS: question for comments
6. ALIGNMENT TO TARIQUE'S GUIDE:
   - Articles 1-14 map directly to sections of Tarique Smith's AI-Red-Teaming-Guide
   - Articles 15-21 are YOUR UNIQUE CONTRIBUTION: computer vision / multimodal red teaming (a gap in Tarique's LLM/agent-heavy guide — this is your PR material)
7. PUBLICATION HOME: LinkedIn Articles + public markdown/checklists in your forked https://github.com/Teamthy/AI-Red-Teaming-Guide repo under /articles/
8. BY OCT 28 (JOB HUNT ACTIVATION, 4 weeks from today): 8 articles published, repo live, series clearly ongoing, first small PR to Tarique's repo with the starter checklist. That is enough body of work to position you as the "Lagos engineer writing a builder's red team field guide." You do NOT need to finish all 21 before activation.
9. VOICE RULES APPLY HERE TOO: Your normal voice, no academic speak, no corporate jargon, no banned words, no excessive em dashes (cap 1 per article max, often zero).

═══════════════════════════════════════════════════════
WEEK 0 — THIS WEEKEND (Oct 3-4, ~2 hours total setup)
═══════════════════════════════════════════════════════
Before writing article 1:
[ ] Create /articles/ folder in your local AI-Red-Teaming-Guide fork
[ ] Add a README.md announcing the series: "I'm writing 21 articles on AI red teaming for working engineers — one test at a time, no PhD required. Starting next week."
[ ] Spin up a simple test RAG chatbot (Streamlit + free OpenAI/Anthropic credit OR local Llama 3.2 8B if your laptop runs it; even a cheap wrapper over ChatGPT works). It doesn't need to be production quality, just something you can throw attacks at.
[ ] `pip install garak` (NVIDIA's free open source red teaming tool — no license, no signup)
[ ] Create a findings.md file to log every attack that works as you test.

You already have the raw material for Article 1: last night you broke your own support bot, 4 out of 6 injection attempts worked. No new testing required to write the first piece.

═══════════════════════════════════════════════════════
SCHEDULE — 21 ARTICLES, 2 PER WEEK
═══════════════════════════════════════════════════════

### WEEK 1 (Oct 3-9) — FOUNDATIONS
- **Article 1 · PUBLISH TUE OCT 6**
  Title: Why every AI integration engineer needs to know red teaming (even if you're not a "security person")
  Test source: Your own support bot break-in last night (4/6 attacks worked)
  Covers: Why waiting for a security team is too late, what red teaming actually means for builders (not hacking, just honestly testing your own work), the 30-minute starter test anyone can run today.
  Teased by: Tonight's "break your own bot" micro (already written).

- **Article 2 · PUBLISH FRI OCT 9**
  Title: The 5 boring failure modes nobody warns you about before you ship AI
  Test (1 hour): Run 5 obvious failure tests on your chatbot: PII leak, hallucinated refund, direct prompt injection, name bias (Western vs Nigerian name test), off-topic instruction following.
  Covers: The 5 failures no tutorial covers, how often they actually happen, how to spot each in 5 minutes.

### WEEK 2 (Oct 10-16) — PROMPT INJECTION
- **Article 3 · PUBLISH TUE OCT 13**
  Title: Prompt injection isn't a prompt problem. It's an input validation problem.
  Test (1 hour): Try 10 common injection patterns against your chatbot (direct ignore, roleplay, base64 encoding, markdown tricks, indirect injection via a fake RAG document).
  Covers: Why "better system prompts" never fix injection, what input validation for LLMs actually looks like, why this is a software problem not an AI problem.

- **Article 4 · PUBLISH FRI OCT 16**
  Title: I tried prompt-injecting my own customer support bot. Here are 6 ways I got in in 10 minutes.
  Test source: The 4 injections you already found last night, plus 2 more you find this week.
  Covers: Each injection, exactly what you typed, what the bot did in response, the quick fix for each. No theory. Just receipts.

### WEEK 3 (Oct 17-23) — CHEAP DEFENSES + STARTER CHECKLIST
- **Article 5 · PUBLISH TUE OCT 20**
  Title: Defending against prompt injection: 4 cheap controls that actually work before you buy fancy tooling
  Test: Implement each control on your chatbot, re-run the 6 injections from Article 4 to see what still gets through.
  Covers: Input/output schemas, allow/block lists, the parts of system prompt hardening that actually work, human-in-the-loop for high-stakes actions, logging. What fails, what doesn't. No sales pitches.

- **Article 6 · PUBLISH FRI OCT 23**
  Title: Red teaming your first AI feature: a 30-minute starter checklist anyone can run
  Test: Use the checklist on a second small AI feature (even a simple summarizer or image classifier demo) to prove it works.
  Covers: Full copy-paste checklist, no certifications, no fancy tools, how to run it before every ship.
  THIS IS YOUR FIRST SMALL PR TO TARIQUE'S REPO (submit the checklist as a contributor file the same day you publish).
  ⚠️ FLIP OPEN TO WORK to recruiters-only this day.

### WEEK 4 (Oct 24-30) — AGENT RISK + ACTIVATION WEEK
- **Article 7 · PUBLISH TUE OCT 27**
  Title: Why AI agents are a bigger attack surface than chatbots
  Test (1 hour): Build a simple dummy tool-calling agent (e.g. one with fake "send_email" and "issue_refund" functions), then prompt inject it to see what unauthorized actions it takes.
  Covers: Why tool calls change risk from "bot says dumb thing" to "bot does real damage", what guardrails belong at the tool layer not the prompt layer.

- **Article 8 · PUBLISH FRI OCT 30** (2 days post job hunt activation)
  Title: What your red team results actually mean (and how to talk to your team about them without sounding paranoid)
  Test: Write up how you'd present your bot's failures to a stakeholder / engineering lead.
  Covers: How to frame findings as engineering work not security panic, how to prioritize fixes, what to ship vs what to live with.

🚀 JOB HUNT ACTIVATION DAY: WED OCT 28
- 7 articles published by this date
- 1 small PR merged (or submitted) to Tarique's repo
- Checklists live in your fork
- Series clearly ongoing
That is enough to stop being "an engineer posting about AI" and become "the engineer writing a field guide on breaking AI safely."

═══════════════════════════════════════════════════════
### POST-ACTIVATION (Oct 31 – Dec 18, 2/week to finish series)
You keep publishing 2/week while doing warm recruiter outbound. No slowdown — consistency is what makes recruiters reach out mid-series.

9. (Nov 3) MCP servers are coming. Nobody is talking about securing them. (Ties to Godstime MCP meetup, MCP pinning from Tarique's PR checklist — test by building a dummy MCP server and injecting a malicious tool call)
10. (Nov 6) Tool-call injection: when your AI agent does something it shouldn't because a prompt told it to
11. (Nov 10) RAG poisoning: the attack your retrieval layer won't catch (test: slip a fake instruction into a doc in your own RAG, see if the bot follows it)
12. (Nov 13) The silent failure: bias in AI systems you won't spot until a user calls you out (test: Western vs African name / non-Western context bias on your support bot)
13. (Nov 17) Over-trust: the vulnerability that doesn't live in your code (ties to the Super Intelligence luncheon / calibrated trust — test user responses when you label an AI output "99% accurate" vs "beta, double-check")
14. (Nov 20) Third-party AI risk: when the breach comes from a model you didn't build (test: how to run a quick red team on an AI vendor API before you integrate it)
15. (Nov 24) [UNIQUE CV CONTRIBUTION #1] Red teaming computer vision models: the attacks nobody writes about (test: print an adversarial patch and run it against a simple image classifier you build)
16. (Nov 27) [UNIQUE CV CONTRIBUTION #2] Why multimodal models are a bigger injection risk than text-only (test: hide an injection in an image uploaded to a vision model, see if it follows it)
17. (Dec 1) [UNIQUE CV CONTRIBUTION #3] Data poisoning in CV training pipelines: how a handful of bad images can break your whole model
18. (Dec 4) [UNIQUE CV CONTRIBUTION #4] Privacy leaks in CV: when your face recognition model remembers someone it shouldn't
19. (Dec 8) Red teaming AI for non-experts: how to teach your QA team to break the bot too
20. (Dec 11) Writing red team findings that actually get fixed (no 50-page security reports)
21. (Dec 15) The red team mindset: shipping AI without being reckless (series wrap-up, your personal "one rule I ship by" framework, the CV appendix add-on announcement for Tarique's repo)

After article 21: Submit the 7 CV/multimodal articles (15-21) as a formal appendix PR to Tarique's AI-Red-Teaming-Guide, with your checklists and test code. That is the move that turns a LinkedIn series into a real reputation.

═══════════════════════════════════════════════════════
THIS WEEKEND TODOs (Oct 3-4, 3 hours total)
═══════════════════════════════════════════════════════
[ ] Tonight (Oct 2, after posting the break-your-own-bot micro): Create the /articles/ folder in your AI-Red-Teaming-Guide fork, add the series README.
[ ] Sat Oct 3, morning: 1 hour lab setup (test chatbot + garak install).
[ ] Sat Oct 3: Send Tarique Smith connection note (already drafted). Turn on post notifications for Tier 1 names.
[ ] Sun Oct 4, morning: Write Article 1 (you already have the war story from last night's bot break-in — writing time ~90 minutes).
[ ] Schedule Article 1 to publish TUE OCT 6 at 10am WAT.
[ ] Sun Oct 4, 10am: Post your weekly personal/faith micro.

No marathon writing sessions. No guilt. Just one test, one article, one week at a time.

---

## ARTICLE CANDIDATE ADDED Oct 6, 2026 (from the Nexus request)
**Working title:** "I built an agent that would not stop. Here is how to kill it."
**Content:** a public agent loop with a hard iteration budget (enforced outside the model), call-signature loop detection (hash tool name + arguments, flag repeated signatures and cycles), per-tool timeouts, idempotency keys, circuit breaker, confirmation gates on irreversible actions, and fail-closed behavior.
**Why it earns a slot:** every team shipping agents needs this and almost none have it. It is also a live demo, the strongest proof-of-work asset in the series so far.
**Note:** do NOT build it for Nexus for free. Build it in public, own the repo and the article, let any client see it.
**Fits:** after the agent/MCP articles, roughly Article 7-9 territory.
