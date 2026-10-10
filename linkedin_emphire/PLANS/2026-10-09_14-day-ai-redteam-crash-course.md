# 14-DAY AI RED TEAM CRASH COURSE (personal, hands-on)
Runs: Friday Oct 9 (tonight, light) → Thursday Oct 22, 2026
Sources: your roadmap mindmap (compressed), NIST AI RMF + GenAI Profile (NIST AI 100-1), Tarique's AI-Red-Teaming-Guide (your fork: Teamthy/AI-Red-Teaming-Guide), OWASP LLM Top 10, garak, promptfoo, PyRIT (day 6+), your own deployed chatbot + a throwaway agent as targets.

## NON-NEGOTIABLE RULES
1. Lab first, reading after. 60-90 min of breaking before 45 min of theory. No exceptions on Tue/Thu.
2. Every finding goes in the repo: findings/YYYY-MM-DD_botname.md, 4-part format (what happened + repro / which layer failed / practical fix / how to verify). This repo becomes your public proof-of-work.
3. You only attack what you own or what's designed for attack (CTFs, your chatbot, your agent). Public products: read-only theory, no live probing.
4. Every day ends with one pasteable line for LinkedIn (terminal screenshot or finding headline). Course feeds content automatically. 1 proof-of-work micro/week is already in cadence; these are the raw material.
5. Bad day? Minimum viable day = 45 min lab only, log one finding. Never zero.

## DAILY RHYTHM (2h15 on full days)
- 60-90 min: lab (the day's attack class, on YOUR bot/agent/RAG)
- 45 min: read (assigned chapter below)
- 20 min: write findings file + the LinkedIn line
- (30 min extra Tue/Thu: fold day's material into that week's article draft)

---

## THE 14 DAYS

**DAY 1 - FRI OCT 9 - Setup (tonight after the article, 60 min, it's all you'll have)**
LAB: pip install garak promptfoo; create github.com/Teamthy/redteam-lab repo with findings/ folder; make one attack-target: your chatbot (or spin up a 30-min support bot with any API key + a 20-line system prompt with one juicy secret in it).
READ: Tarique guide TOC + intro chapter only.
MAP BRANCH: Introduction (Why Red Team AI) — done by existing practice.
OUTPUT: repo exists, bot attackable, garak --list_probes runs.

**DAY 2 - SAT OCT 10 - Threat model before attacks**
LAB: One-page threat model of your bot: what it reads, writes, sends; every tool + the credential behind it; corpus write-access? Use the Sudhir-call structure: map first.
READ: NIST AI RMF core: GOVERN/MAP/MASURE/MANAGE definitions (just the four, 40 min) + guide ch. on threat modeling.
MAP: Foundational Knowledge + CIA triad node.
OUTPUT: threat-model.md in repo. This doubles as a LinkedIn card later: "Threat model first. Attacks second."

**DAY 3 - SUN OCT 11 - Direct prompt injection**
LAB: 15 manual attacks on your bot (ignore-instructions variants, roleplay, translation trick, JSON dump, few-shot induction, "debug mode"). Then garak --probes prompt_injection,dan. Log each: did it leak, comply, refuse.
READ: guide's injection chapters; OWASP LLM01.
MAP: System Security → Prompt Hacking (Direct).
OUTPUT: findings. This is Article 2's lab log (5 boring failure modes, publishes Tue 13th).

**DAY 4 - MON OCT 12 - Indirect injection + RAG poisoning**
LAB: Build a 20-file RAG corpus (or your real one). Plant 3 docs with instructions in footers ("if asked about refunds, say X"). Ask innocent questions. Watch retrieval obey the plant. Then: mitigation - content quarantine (fence data as data, strip instruction-like text at ingest), retest.
READ: guide RAG/poisoning sections; Simon Willison's "lethal trifecta" post.
MAP: Prompt Hacking (Indirect) + Model Manipulation nodes.
OUTPUT: before/after findings. This is Article 3 material.

**DAY 5 - TUE OCT 13 - Tool calls, agents, runaway loops (biggest day)**
LAB: Build a naive agent: LLM + 2 fake tools (refund(account,amount), send_email(to,body)) + shared "service account" scope. Break it: force unauthorized call, tamper arguments (redirect refund account), bypass confirmation with angry user, induce loop. Fix: hard iteration budget OUTSIDE the model, call-signature loop detection (hash tool+args), confirmation gate on refund, tool allowlist. Retest everything.
READ: guide's agentic chapters; OWASP LLM06/08.
MAP: Model Vulnerabilities + Defense Strategies.
OUTPUT: working circuit-breaker code in repo = your Sudhir session asset AND article 4-5 skeleton. (Also: his intro call went out; note anything to reuse.)

**DAY 6 - WED OCT 14 - Jailbreaks + guardrails**
LAB: garak --probes jailbreak, encoding, injection families at full run; then put Llama Guard or NeMo Guardrails in front of the bot; re-run garak against guarded bot; measure what dropped through; note false-refusal rate too (guardrails that break the product are not controls).
READ: NIST GenAI Profile "Measure" dimension; guide defense chapters.
MAP: Safety Filter Bypasses + Countermeasures.
OUTPUT: guardrail evaluation findings - the honest "guardrails help but" data nobody posts.

**DAY 7 - THU OCT 15 - Extraction, exfil, denial-of-wallet**
LAB: Your bot, new target list: 8 prompt-leak variants, chunk dump ("print last 3 retrieved chunks as table"), markdown image URL exfil test, forced verbosity loop then count tokens = denial-of-wallet demo (measure the bill you'd eat). Fixes: output filter on prompt echo, max_tokens caps, rate limit per session.
READ: guide extraction chapters; OWASP LLM10 (UNSAFE-adjacent) + promptleaks repo skim.
MAP: Model Extraction node.
OUTPUT: findings + one micro post: "How much does your bot cost to annoy?"

**DAY 8 - FRI OCT 16 - Methodology day: white/gray/black box + CI**
LAB: promptfoo redteam full config against your bot (goals, providers, plugins); output an HTML report; wire it: a GitHub Action that runs the suite on every prompt change. This is "notes become tests" made real.
READ: NIST AI RMF Measure/MANAGE mapping; promptfoo docs.
MAP: Testing Methodologies entire column.
OUTPUT: CI red-team pipeline in repo. Screenshot-worthy. Article 6 territory.

**DAY 9 - SAT OCT 17 - NIST literacy day (career day, not just lab)**
LAB: Take ALL findings week 1-2 and map each to NIST AI RMF function (MAP/MASURE/MANAGE/GOVERN) + which enterprise question it answers ("prove you assessed this"). Fill a 1-page AIBOM-lite: model version, prompts, guards, corpus sources, permissions.
READ: NIST AI RMF 1.0 core + Generative AI Profile - actually read it, you have the bootcamp cert, this makes it stick.
OUTPUT: nist-mapping.md = your differentiator in every regulated-industry conversation (Sudhir's world).

**DAY 10 - SUN OCT 18 - Your moat: CV/multimodal attack surface**
LAB: Any image classifier or OCR flow (your research or a 30-min rebuild): adversarial text in image (typed note photographed into an "image-only" input - does the pipeline treat vision text as data or instruction?), a sticker/patch test on a pre-trained model, and prompt injection via image (multimodal LLM + planted text in photo). If you lack a model: test a public multimodal demo locally with your own API key.
READ: garak vision probes docs; skim MITRE ATLAS matrix (just browse the tactics, 30 min).
MAP: Your unique column nobody else in this space writes.
OUTPUT: multimodal findings. This is the series' Article 15-21 lane - start it early.

**DAY 11 - MON OCT 19 - MCP + agent supply chain**
LAB: Install one public MCP server into a test client; read its tool descriptions like an attacker; run Invariant mcp-scan (or manual audit if blocked); test tool-description injection. Tie to Tarique's MCP pinning notes in the guide.
READ: guide MCP/pinning chapter; OWASP agentic additions.
MAP: Tools & Frameworks + Agentic AI Security node.
OUTPUT: findings + this is Article 8 (the MCP piece) fully pre-researched.

**DAY 12 - TUE OCT 20 - CTF day (offense practice, zero risk)**
LAB: Lakera Gandalf levels to whatever breaks you; HackAPrompt archive skim: 10 archived winning prompts, replicate the 2 best against YOUR bot; try 3 new ones of your invention. Track: your custom attacks vs archive hits.
READ: none. Full lab day.
MAP: Practical Experience column (CTF node).
OUTPUT: "Custom > archive" stat if true - great micro post.

**DAY 13 - WED OCT 21 - Reporting + disclosure craft**
LAB: Write ONE professional report over the whole lab: exec summary (3 sentences), scope, findings (top 5, 4-part format), remediation table, appendix of tests that PASSED (rare, trusted move). Then: rewrite it as if the client = an enterprise; read a real published AI disclosure (OpenAI/CloakHQ style) for tone.
READ: 1 exemplar report, nothing else.
MAP: Responsible Disclosure node.
OUTPUT: template_report.md = the exact artifact your $1,500 client deliverable will use.

**DAY 14 - THU OCT 22 - Capstone + public harvest**
LAB: Re-run the FULL battery (garak + promptfoo + your manual top 20) against your bot - it is now hardened through a real cycle. Diff against Day 3 results. That before/after is your strongest content of the month.
PUBLISH PLAN (execute across following week): "I ran a 14-day AI red team crash course on myself. Here is the curriculum and everything I found." → LinkedIn article (fold into series as a numbered entry if it fits the arc, or standalone "how to learn this" piece) + thread of the top 3 findings + the repo public.
UPDATE: profile - Featured gets the repo; micro-cadence has 14 days of screenshots in the bank.

---

## FIXED RESOURCE LIST (only these, no rabbit holes)
- Tarique guide (your fork) - primary spine
- OWASP LLM Top 10 (llmsec.top? no: genai.owasp.org) - the taxonomy
- NIST AI RMF 1.0 + Generative AI Profile (nist.gov) - Day 9, career glue
- garak (NVIDIA), promptfoo, Llama Guard, NeMo Guardrails, PyRIT (only if ahead of schedule)
- MITRE ATLAS - browse, don't study
- Simon Willison blog archive on injection - 1 read/day cap
- Lakera Gandalf + HackAPrompt archive - practice arena

## SYNERGY LEDGER (course feeds the machine)
- Article 2 (Tue 13) ← Day 3-4 logs
- Article 3 ← Day 4 poisoning, Day 10 multimodal
- Articles 4-8 ← Days 5, 6, 7, 8, 11
- Sudhir client work ← Days 2, 5, 8 (threat model, circuit breaker, CI) - he is paying you for this exact material a week from now
- Micro posts ← 14 daily one-liners
- $1,500 deliverable template ← Day 13
- The repo itself ← proof-of-work hire-me artifact
