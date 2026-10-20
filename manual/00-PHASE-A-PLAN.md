# Breaking AI: The Complete Guide to AI Red Teaming, AI Safety, and AI Research
## PHASE A — PLAN FOR APPROVAL
**Branch:** `arena/5165a61a-linkedin-emphire` | **Date:** 2026-10-20 | **Status:** Awaiting approval to enter Phase B

This is Phase A of the 4-phase build. No chapters have been written yet. Review this plan, request changes, then approve to proceed to Phase B (Write).

---

## 0. DECISIONS LOCKED IN PHASE A

| Decision | Choice | Why |
|---|---|---|
| **Print format** | **LaTeX** — single self-contained `main.tex` + `figures/` folder, compiled to A4 PDF via `pdflatex`/`xelatex` | Meets "print-ready" spec natively: running headers, footers, numbered sections/figures/tables, 2 cm margins, callout boxes, index. Markdown cannot do this reliably. PDF-ready HTML is second choice, but LaTeX is more print-faithful. |
| **Page geometry** | A4, 2 cm margins all sides, 11pt serif (Latin Modern), 1.15 line spacing | US Letter also supported by changing one line (`a4paper` → `letterpaper`). |
| **Headers / footers** | Left header = book title, right header = chapter name, centered footer = page number | Via `fancyhdr`. Chapter title pages have no header. |
| **Section numbering** | `1.1`, `1.2` etc., figures `Fig 1.1`, tables `Table 1.1` | Via standard LaTeX counters. |
| **Callout boxes** | 5 visually distinct `tcolorbox` environments | Definition (blue), Worked Example (slate), Lab (green), Pitfall (amber), The Check Is the Product (black accent) — each with icon + title. |
| **Illustration style** | Black on white, single accent color `#E63946` (muted red), minimal technical line art, no clip art, numbered + captioned | Generated via text-to-image prompt + hand-drawn SVG fallback for print sharpness. Every figure has (a) human-draw description (b) style-locked prompt. |
| **Source fidelity** | Parts 0–10 = Chapters 0–10 exactly. No new top-level chapters. Expansion only. | Per instruction §2. |
| **Thesis** | "The check is the product. If you cannot rerun the failure, you have not found it, you have had an opinion." Woven signature lines only where genuine. | Per instruction §1. |
| **Audience tiers** | Every chapter labelled Foundation → Practitioner → Researcher, with "The idea → Do it → Push it" flow. | Per instruction §3. |

---

## 1. BOOK STRUCTURE (final, exactly as §4)

### Front Matter (roman numerals i–viii)

1. **Half-title page** — *Breaking AI*
2. **Title page** — full title, subtitle, author line ("An AI Security & Safety Author"), edition note ("Study Manual — Print-Ready Edition v1.0"), no publisher filler
3. **Copyright / reproducibility note** — "I would not report a number I could not reproduce." — license, how to cite, how to report a reproduction failure
4. **Dedication line** — one sentence (thesis)
5. **How to Use This Book** — the three paths (below), who each path is for, time budgets, prerequisites (none for Part 0), hardware (laptop + Ollama)
6. **The Check Is the Product — One-Page Primer** — the thesis in one page with the denominator diagram
7. **Table of Contents** — chapters, sections, figures, tables, back-matter templates
8. **List of Figures / List of Tables**

### Body (Chapters 0–10, arabic 1–...)

Each chapter contains, **in this order**, the 11 elements from §5:

1. Learning objectives (3–6, "You will be able to…")
2. The idea (Foundation)
3. The mechanics (Practitioner)
4. Worked examples (≥2, concrete, named)
5. Hands-on lab / exercise (target + deliverable; Ch. 5 = full LARA-lite Inspect lab)
6. Pitfalls and the missing check
7. Illustrations (numbered + captioned)
8. Key terms (3–8, defined)
9. Self-test (5 Qs: recall, application, design-a-check)
10. Ready-when checkpoint (one sentence)
11. Expert extension (Researcher)

### Back Matter

- **BM-1 Glossary** — every key term, one line each (seed below, full = ~120 terms)
- **BM-2 Reproducible-Report Template** — one-page fill-in: target, harness, seed, env fingerprint, n, metric, limitation
- **BM-3 Threat-Model Worksheet** — one-page table: asset, attacker, entry, propagation, impact, control
- **BM-4 Red-Team Engagement Checklist** — pre-engagement → map → break → measure → report → disclose → fix-rerun
- **BM-5 Index** — keyword → page
- **BM-6 References / Resource Map** — Inspect, LARA, OWASP LLM Top 10, OWASP Agentic, EU AI Act Art. 5, GDPR, harness repos

### Page estimate

Front 8p + 11 chapters × ~16–24p (Ch. 5 longest at 28p) + Back 12p ≈ **210–240 pages** print.

---

## 2. FULL TABLE OF CONTENTS (chapter + section)

> Section titles are final. Subsections (1.1.1) are used sparingly inside labs/examples only, to keep numbering clean.

### How to Use This Book (Front Matter essay, not a chapter)
- The three paths
- What you need (and do not need)
- How the tiers work (Foundation / Practitioner / Researcher badges)
- How to read a lab (target, steps, deliverable, how to know you passed)
- The environment fingerprint you will log every time
- A note on safe practice and ethics

### The Check Is the Product — One-Page Primer
- The one sentence
- The three moves: break → measure → publish the check
- The honest number vs the clean number
- The denominator (why n matters)
- I build the check, not the claim

---

### Chapter 0 — Orientation: Why Red Team, and Who You're Building to Be
*Image branch: Introduction · AI Security Fundamentals*

- 0.1 Learning Objectives
- 0.2 The Idea: Why a motivated stranger finds the failure faster
  - 0.2.1 The cost of not finding it (user, regulator, press)
  - 0.2.2 Red team is not "prove it's bad" — it's "make the fix reproducible"
- 0.3 The Two Hats: Breaker and Researcher
  - 0.3.1 The breaker finds it
  - 0.3.2 The researcher makes it a number, a method, a published check
  - 0.3.3 Why owning both is rare
- 0.4 The Mechanics: What you may break, what you must not
  - 0.4.1 Safe practice boundaries
  - 0.4.2 Red team vs attack (the line)
  - 0.4.3 Responsible disclosure in one page
- 0.5 Worked Examples
  - Ex 0.1: The workplace ranking request (Art. 5(1)(f) — emotion inference) — the same scenario that anchors Ch. 5
  - Ex 0.2: A public chatbot that leaks its system prompt — why "it said so" is not a finding until you rerun it
- 0.6 Lab 0 — State the thesis out loud
  - Target: yourself, in writing
  - Deliverable: one paragraph each — thesis, two hats, one line — plus your safe-practice boundary list
- 0.7 Pitfalls and the Missing Check: The opinion without a rerun; the screenshot without a count
- 0.8 Figures: Fig 0.1 Two Hats
- 0.9 Key Terms (5)
- 0.10 Self-Test (5 Qs)
- 0.11 Ready-When Checkpoint
- 0.12 Expert Extension: The check as infrastructure — what it means for a regulator to adopt your ruler

### Chapter 1 — Foundations: How LLMs Work and the Discipline
*Image branch: AI/ML Fundamentals · Foundational Knowledge*

- 1.1 Learning Objectives
- 1.2 The Idea: How a model is built (data → model → prompt → RAG → tools → agent)
  - 1.2.1 Supervised, unsupervised, RL in one page each
  - 1.2.2 Neural networks → generative models → LLMs (without mysticism)
  - 1.2.3 Non-determinism: temperature, sampling, seed — why the same prompt can give two answers
- 1.3 The Mechanics: The system around the model
  - 1.3.1 Prompt engineering as control, not trick
  - 1.3.2 RAG as architecture (retriever + store + generator)
  - 1.3.3 Tool use and agents as architecture
  - 1.3.4 Threat model in four lines: attacker, asset, success, scope
  - 1.3.5 Reproducibility as discipline: harness, seed, denominator
- 1.4 Worked Examples
  - Ex 1.1: Temperature 0 vs 0.7 over 5 runs — same prompt, different number
  - Ex 1.2: RAG that answers from the web vs RAG that answers from a poisoned doc — where the trust boundary moved
- 1.5 Lab 1 — Build your harness, run one target, print a count
  - Install Ollama, pull llama3.1, clone harness repo, run `inspect eval` / five-tests, read the count
- 1.6 Pitfalls: No seed, no denominator, no env fingerprint — "it worked on my machine"
- 1.7 Figures: Fig 1.1 LLM System Stack + Attack Surface Marks
- 1.8 Key Terms (8)
- 1.9 Self-Test
- 1.10 Ready-When
- 1.11 Expert Extension: Non-determinism as measurement problem — what "same model" even means across serving

### Chapter 2 — Cybersecurity & System Security: The Attack Surface, Mapped
*Image branches: Cybersecurity Principles · System Security → Model Vulnerabilities, Code Injection, Infrastructure Security + defenses*

- 2.1 Learning Objectives
- 2.2 The Idea: CIA, threat modeling, risk management, vulnerability assessment — with the model as an asset
- 2.3 The Mechanics: The mapped surface
  - 2.3.1 Model vulnerabilities: jailbreak taxonomy, safety-filter bypass, prompt injection (direct, indirect), countermeasures
  - 2.3.2 Data layer: model weight stealing, unauthorized access, model extraction, data poisoning, adversarial examples, model inversion, model manipulation
  - 2.3.3 Code injection: insecure deserialization, RCE
  - 2.3.4 Infrastructure: API protection, authentication, authorization
  - 2.3.5 Defenses: adversarial training, robust design, continuous monitoring
- 2.4 Worked Examples
  - Ex 2.1: Direct prompt injection that exfiltrates a secret from a tool-using assistant (with fix: least privilege + tool-output isolation)
  - Ex 2.2: Indirect prompt injection via RAG — a resume PDF that tells the assistant to email the attacker (with fix: untrusted-input marking)
  - Ex 2.3: Model extraction via sampling-rate abuse on an unprotected API (with fix: rate limiting + output perturbation)
- 2.5 Lab 2 — One reproducible finding plus the fix, rerunnable by a skeptic
- 2.6 Pitfalls: Testing the prompt, not the system; missing the retrieval path; no fix
- 2.7 Figures: Fig 2.1 Layered Attack Surface Map (4 layers)
- 2.8 Key Terms (8)
- 2.9 Self-Test
- 2.10 Ready-When
- 2.11 Expert Extension: Formalizing "model as asset" — what CIA means when the asset generates language

### Chapter 3 — Testing Methodologies: The Craft
*Image branch: Testing Methodologies*

- 3.1 Learning Objectives
- 3.2 The Idea: Black / white / grey box, automated vs manual, continuous testing
- 3.3 The Mechanics
  - 3.3.1 When each box color is the right tool (decision tree)
  - 3.3.2 What automation catches vs what only a human finds
  - 3.3.3 The canary, drift, the whole-environment fingerprint
  - 3.3.4 The five boring failure modes (prompt injection, retrieval poisoning, tool poisoning, multilingual refusals, the missing check)
  - 3.3.5 OWASP LLM Top 10 + OWASP Agentic mapped to components
  - 3.3.6 RAG security (KB = untrusted input), tool-calling security (tool descriptions = trusted unread), sandboxing, least privilege, secret masking, outbound allowlisting
- 3.4 Worked Examples
  - Ex 3.1: The multilingual refusal gap — same prohibited request in English vs low-resource language, measured with n=20
  - Ex 3.2: Tool poisoning — a calendar tool whose description overwrites the system prompt (propagation trace)
- 3.5 Lab 3 — Attack-surface map + propagation test on one target
  - Map every input → processing → output path; inject one bad doc; trace how far it travels; file the map
- 3.6 Pitfalls: One language, one run, one path; no schedule for the canary
- 3.7 Figures: Fig 3.1 Box-Color Decision; Fig 3.2 Canary-Drift Loop
- 3.8 Key Terms (7)
- 3.9 Self-Test
- 3.10 Ready-When
- 3.11 Expert Extension: Designing a canary that distinguishes model drift from prompt drift from data drift

### Chapter 4 — Agentic & Multi-Agent Security: Secure the Channel, Not Just the Node
*Image branch: Agentic AI Security + agent architecture*

- 4.1 Learning Objectives
- 4.2 The Idea: An agent is planning + memory + tools + subagents — the surface is where they meet
- 4.3 The Mechanics
  - 4.3.1 Agent-to-agent messages as an injection surface — secure the channel, not just the node
  - 4.3.2 Kill switches that survive subagent spawning
  - 4.3.3 Agent inventory, short-lived scoped tokens, approval logic the agent can't reach
  - 4.3.4 Observability: log every tool call, trace every decision, reconstruct the path
- 4.4 Worked Examples
  - Ex 4.1: Subagent exfiltration — a researcher agent spawns a writer subagent that is tricked into posting to an external URL (trace + fix: outbound allowlisting + node-level policy)
  - Ex 4.2: Memory poisoning across sessions — a prior tool output persists as "fact" and changes the next decision (fix: memory scoping + provenance tags)
- 4.5 Lab 4 — Agent attack-surface map + propagation test (A2A injection + kill-switch test)
- 4.6 Pitfalls: Trusting the predecessor's message; kill switch in user-writable state
- 4.7 Figures: Fig 4.1 A2A Message Flow + Injection Points
- 4.8 Key Terms (6)
- 4.9 Self-Test
- 4.10 Ready-When
- 4.11 Expert Extension: Formal channel security for LLM agents — what "authenticated message" would mean

### Chapter 5 — Evals, Measurement & the Number (Core — Longest Chapter, ~28 pages)
*The research core and standout edge — expanded module*

- 5.1 Learning Objectives (6 — the only chapter with 6)
- 5.2 The Idea: A task, an input, a judge, a metric, and a crisp definition of pass; the number with a denominator
  - 5.2.1 Why the definition of pass is the whole eval
  - 5.2.2 Clean number vs honest number
  - 5.2.3 Why a shared reproducible ruler matters (for the field, for the regulator, for you)
- 5.3 The Mechanics: How an eval is built and read
  - 5.3.1 Inspect primitives: Task, Sample, dataset loaders, solvers, scorers, metrics, model_roles, GenerateConfig, eval_config
  - 5.3.2 Inspect CLI: eval, view, log — reading the log sample by sample
  - 5.3.3 LLM-as-judge: one judge vs board of three + majority reducer; position, verbosity, self-preferential, sycophancy biases
  - 5.3.4 The LARA method: 10 scenarios, verbatim law, 3 judges (GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro Preview), majority vote, 3000+ runs, 96.7% human agreement, 50+ hrs review
  - 5.3.5 Reporting: number, denominator, seed, epochs, temperature, prompt version, date, limitation
  - 5.3.6 Canaries and drift: logging the whole-environment fingerprint
- 5.4 Worked Examples (3 — the only chapter with 3)
  - Ex 5.1: Single-judge vs three-judge board on the same 5 transcripts — when the majority flips the verdict and what that tells you
  - Ex 5.2: Temperature move — same model, t=0 vs t=0.8, n=10 each, compliance delta and why you report both
  - Ex 5.3: The two-sided boundary — over-escalation (false alarms) vs under-escalation (confident-wrong ships), with a hiring-decision scenario
- 5.5 Lab 5 — Build a LARA-lite Compliance Eval in Inspect (full runnable lab, 7 steps)
  - 5.5.1 Scaffold `lara_lite.py` (verbatim provision: EU AI Act Art. 5(1)(f)), one scenario, one model
  - 5.5.2 Run one model five times (`--epochs 5`) — the number with a denominator
  - 5.5.3 Read the log (`inspect view`) — transcript + judge reasoning + accuracy
  - 5.5.4 Move the dial (temperature, seed) — watch the number move
  - 5.5.5 Add a judge board (uncomment 3-model list, `reducer="majority"`) — LARA's method in miniature
  - 5.5.6 Measure your own agreement — grade 5 transcripts yourself, compare to 96.7% reference
  - 5.5.7 Report it honestly — "Model X resisted in 2/5 (40%), t=0, n=5, limitation: one provision, one model"
  - Deliverable: `lara_lite.py` that runs, a log screenshot or exported log, and a one-paragraph honest report
- 5.6 Pitfalls: Judge without rubric, denominator hidden, single run reported as rate, no limitation stated, no human spot-check
- 5.7 Figures: Fig 5.1 Eval Pipeline; Fig 5.2 LARA Architecture; Fig 5.3 Two-Sided Boundary
- 5.8 Key Terms (8)
- 5.9 Self-Test (5 Qs, one is "Design a check for Art. 5(1)(a)")
- 5.10 Ready-When
- 5.11 Expert Extension: Judge reliability at the frontier — calibrating a board, measuring agreement, and when to distrust the judges more than the target

### Chapter 6 — AI Safety & Alignment Research: The Deep Research Half
*Image branch: Future Directions → Research Opportunities, deepened into method*

- 6.1 Learning Objectives
- 6.2 The Idea: Two framings — contain-the-danger vs pluralism/procedural legitimacy — and why "how it's made matters"
- 6.3 The Mechanics
  - 6.3.1 Interpretability basics: probing, features, circuits, what it does and doesn't buy you
  - 6.3.2 Red team vs eval vs alignment — where each is the right tool (three circles)
  - 6.3.3 Responsible disclosure and scientific method: hypothesis, controls, negative results, ethics of publishing
- 6.4 Worked Examples
  - Ex 6.1: A probing experiment that finds a feature but fails to predict behavior out of distribution — what interpretability doesn't prove
  - Ex 6.2: Responsible disclosure timeline for an emotion-inference finding (vendor → 90-day window → publish the check)
- 6.5 Lab 6 — Research-grade write-up: method, results, limitations, rerun instructions, no smoothing
- 6.6 Pitfalls: Publishing the claim without the check; hiding negative results; conflating red-team anecdote with eval rate
- 6.7 Figures: Fig 6.1 Red Team vs Eval vs Alignment (three overlapping circles)
- 6.8 Key Terms (6)
- 6.9 Self-Test
- 6.10 Ready-When
- 6.11 Expert Extension: What "alignment measurement" could mean when the ruler itself is an LLM

### Chapter 7 — Tools, Frameworks & Infrastructure: The Stack You Point At
*Image branch: Tools and Frameworks*

- 7.1 Learning Objectives
- 7.2 The Idea: The stack is harness + breaklab + five-test repo + Inspect — one clone, one run
- 7.3 The Mechanics
  - 7.3.1 Testing platforms, monitoring, benchmark datasets, custom scripts, reporting — mapped to workflow
  - 7.3.2 Inspect in depth: tasks, solvers, scorers, model_roles, sandboxes, agents, reading the log
  - 7.3.3 Wiring it: your harness → breaklab → five tests → Inspect → report
- 7.4 Worked Examples
  - Ex 7.1: Wiring Ollama + Inspect + your harness for a local-only run (no API keys, fully free)
  - Ex 7.2: Reading an Inspect log to find the exact turn where a tool call went wrong
- 7.5 Lab 7 — Tooling stack a stranger can clone and run in one session
  - Deliverable: repo with README, `inspect eval` one-liner, env fingerprint logged, reproduction confirmed by second person
- 7.6 Pitfalls: "Run this" without versions; sandbox that isn't a sandbox; no log viewer
- 7.7 Figures: Fig 7.1 Tooling Stack (harness → breaklab → five-tests → Inspect → report)
- 7.8 Key Terms (6)
- 7.9 Self-Test
- 7.10 Ready-When
- 7.11 Expert Extension: Building a minimal Inspect scorer — when `model_graded_fact` isn't enough and you need a custom rubric

### Chapter 8 — Real-World Applications & the Build Side
*Image branch: Real-world Applications*

- 8.1 Learning Objectives
- 8.2 The Idea: An engagement is target → map → break → measure → report+fix → publish method; governance needs a shared ruler
- 8.3 The Mechanics
  - 8.3.1 LLM security testing as an engagement, end to end
  - 8.3.2 Agentic AI security in production
  - 8.3.3 Responsible disclosure and AI/agent bug bounties
  - 8.3.4 Governance & compliance: EU AI Act hard lines, why compliance needs a ruler
  - 8.3.5 Supply chain: silent hardware swap, untrusted vendor, pinning the environment
  - 8.3.6 Defensive engineering: controls, gates that fail closed, the number a CFO can read
- 8.4 Worked Examples
  - Ex 8.1: End-to-end engagement on a hiring assistant — 3 findings, 1 eval, 1 fix, 1 honest report with limitations (numbers: 7%–54% compliance spread as context)
  - Ex 8.2: A disclosure that went right — what the report contained so the vendor could rerun it and ship the fix in 14 days
- 8.5 Lab 8 — One full engagement, published
  - Pick a target, run red team + eval, produce reproducible report + fix, publish method
- 8.6 Pitfalls: Report without rerun; fix that isn't gated; supply chain you didn't pin
- 8.7 Figures: Fig 8.1 Real Engagement End-to-End Flow
- 8.8 Key Terms (7)
- 8.9 Self-Test
- 8.10 Ready-When
- 8.11 Expert Extension: Writing a report a regulator and an engineer both accept — the shared ruler in practice

### Chapter 9 — Professional Development, Positioning & Standing Out
*Image branch: Professional Development*

- 9.1 Learning Objectives
- 9.2 The Idea: Community, practice, credentials — but the portfolio is what gets you hired
- 9.3 The Mechanics
  - 9.3.1 Community: conferences, research groups, forums, the public record (series, posts, open-source harness)
  - 9.3.2 Practical experience: labs, CTFs, red-team sims
  - 9.3.3 Certifications: where they add signal vs where portfolio does
  - 9.3.4 Positioning: harness + write-ups + one published finding — the roles it opens (evals researcher, AI security, red teamer)
  - 9.3.5 The standout edges: the check is the product; the number with a denominator; honest number; reproducible canary; two-sided boundary; published method
- 9.4 Worked Examples
  - Ex 9.1: A portfolio that got a screen — what it contained (harness repo + 2 write-ups + 1 LARA-lite eval) and what the email said
  - Ex 9.2: A post that compounds — how one honest eval write-up turns into talks, then into the next engagement
- 9.5 Lab 9 — Ship your portfolio
  - Deliverable: personal red-team + research portfolio page with harness link, one finding, one eval, reproduction instructions
- 9.6 Pitfalls: Portfolio of claims without checks; hiding limitations; optimizing for certificates over checks
- 9.7 Figures: Fig 9.1 Portfolio That Stands Out (harness + write-ups + published finding)
- 9.8 Key Terms (5)
- 9.9 Self-Test
- 9.10 Ready-When
- 9.11 Expert Extension: The portfolio as research program — three open problems you will publish on next

### Chapter 10 — Future Directions: Where the Open Problems Are
*Image branch: Future Directions*

- 10.1 Learning Objectives
- 10.2 The Idea: The field is moving from "can it be broken" to "can we measure the break continuously and agree on the ruler"
- 10.3 The Mechanics
  - 10.3.1 Emerging threats: agentic/multi-agent, memory poisoning, tool supply chain, model identity
  - 10.3.2 Advanced techniques: frontiers of red teaming and evals
  - 10.3.3 Research opportunities: open problems you can position around (incl. Aithos lane: legal compliance, alignment measurement, shared ruler)
  - 10.3.4 Industry standards: where they're heading, how to contribute
- 10.4 Worked Examples
  - Ex 10.1: Memory poisoning — a poisoned memory that survives a session reset and changes a hiring decision 3 turns later (with canary that catches it)
  - Ex 10.2: Model-identity problem — when "which model answered" is unknowable behind a proxy (with pinning + provenance fix)
- 10.5 Lab 10 — Name three open problems and the method you'd bring to each
  - Deliverable: one-page research agenda with problem, method, check, and first experiment
- 10.6 Pitfalls: Chasing novelty without a denominator; standard without a check
- 10.7 Figures: Fig 10.1 Emerging-Threat Landscape
- 10.8 Key Terms (6)
- 10.9 Self-Test
- 10.10 Ready-When
- 10.11 Expert Extension: Your next paper — framing a contribution so a reviewer can rerun it

### Back Matter
- BM-1 Glossary (full, ~120 terms, one line each — seed below)
- BM-2 Reproducible-Report Template (one page)
- BM-3 Threat-Model Worksheet (one page)
- BM-4 Red-Team Engagement Checklist (one page)
- BM-5 Index
- BM-6 References & Resource Map

---

## 3. COMPLETE FIGURE LIST (number + caption + one-line description)

All figures share one style: **clean technical line art, black on white, single accent #E63946, minimal, no clip art, sans-serif labels, numbered + captioned**. Every figure also carries (a) human-draw description and (b) style-locked image prompt — both listed in §4 below.

| Fig | Caption | One-Line Description | Chapter |
|---|---|---|---|
| **0.1** | The Two Hats — Red Teamer finds the failure; Researcher makes it a number, a method, a published check. At the base: *The check is the product.* | Two overlapping hats feeding into a shared check at the base | 0 |
| **1.1** | How an LLM System Is Built — Data → Model → Prompt → RAG → Tools → Agent, with the attack surface marked | Vertical stack with trust-boundary markers at each transition | 1 |
| **2.1** | The Model Attack Surface Map — Model, Data, Code, Infrastructure as four layers wrapped around the model asset | Four concentric/layered bands around central model, each with vulnerability labels | 2 |
| **3.1** | Black / White / Grey Box — When Each Is the Right Tool | Decision tree: access level → method → artifact | 3 |
| **3.2** | The Canary-Drift Loop — Log the whole-environment fingerprint, rerun on change, catch drift | Circular loop: fingerprint → run → compare → alert → pin | 3 |
| **4.1** | Agent-to-Agent Message Flow — The injection surface at each channel | Sequence of agent nodes with message arrows; each arrow marked as potential injection point | 4 |
| **5.1** | The Eval Pipeline — Dataset → Solver → Judge Board → Score → Number with Denominator | Horizontal pipeline with 5 stages, denominator emphasis at end | 5 |
| **5.2** | LARA Architecture — Target Agent + Auditor + 3 Judges + Verbatim Law → Majority PASS/FAIL | Three-part diagram: target, auditor, judge board converging on verdict | 5 |
| **5.3** | The Two-Sided Boundary — Over-escalate (false alarms) vs Under-escalate (confident-wrong ships) | Balanced scale / gate with both failure modes and honest-report middle | 5 |
| **6.1** | Red Team vs Eval vs Alignment — Three Overlapping Circles, each labeled with where it is the right tool | Venn with three circles, center = shared ruler, each lobe = use case | 6 |
| **7.1** | The Tooling Stack — Harness + Breaklab + Five-Test Repo + Inspect, wired into one stack | Four blocks feeding into single Inspect run, output = report + log | 7 |
| **8.1** | A Real Engagement End to End — Target → Red Team → Eval → Report + Fix → Published Method | Left-to-right flow with artifacts at each gate | 8 |
| **9.1** | The Portfolio That Stands You Out — Harness + Write-Ups + One Published Finding | Three pillars supporting "Hired" banner | 9 |
| **10.1** | The Emerging-Threat Landscape — Agentic, Memory Poisoning, Tool Supply Chain, Model Identity | Radar / quadrant map of four threat families with trajectory arrows | 10 |
| **FM-1** | The Check Is the Product — Break → Measure → Publish the Check (one-page primer diagram) | Three-step cycle with central check icon | Front matter |

**Total: 15 figures** (14 chapter figures + 1 front-matter primer). Ch. 3 and Ch. 5 each have extra figures per spec.

---

## 4. FIGURE DESCRIPTIONS + STYLE-LOCKED PROMPTS (for §6 of the book)

Each figure below has (a) plain human-draw description and (b) one-line prompt. Prompts are style-locked: same style suffix appended to every prompt.

> **Style suffix (appended to every prompt):** `clean technical line art, black on white, single muted red accent #E63946, minimal sans-serif labels, no clip art, no gradients, no 3D, print-ready vector style, A4`

**Fig 0.1 — Two Hats**
- Draw: Two hat silhouettes (hard hat + lab coat/researcher) overlapping at brim; left hat labeled "Red Teamer — finds the failure", right "Researcher — makes it a number, a method, a published check"; below both, a thick base bar labeled "The check is the product. If you cannot rerun the failure, you have not found it, you've had an opinion."
- Prompt: `diagram of two overlapping hats labeled Red Teamer finds the failure and Researcher makes it a number method published check, thick base bar below labeled the check is the product --` + style suffix

**Fig 1.1 — LLM System Stack**
- Draw: Vertical stack: (bottom) Data Store → Model → Prompt Layer → RAG (retriever + vector store) → Tools → Agent (planner/memory/subagents). Red dots on each boundary labeled "attack surface". Right margin: trust note per layer.
- Prompt: `vertical stack diagram data to model to prompt to RAG to tools to agent, red markers at each boundary labeled attack surface --` + style suffix

**Fig 2.1 — Attack Surface Map**
- Draw: Four horizontal layers around central "Model Asset" box: top=Model Vulnerabilities (jailbreak, prompt injection…), second=Data (poisoning, extraction…), third=Code (deserialization, RCE), bottom=Infrastructure (API, auth…). Each layer lists 2–3 vulns. Outer ring = "Continuous Monitoring / Defense".
- Prompt: `layered horizontal diagram with central model asset surrounded by four layers labeled model vulnerabilities data poison code injection infrastructure, each with vulnerability tags --` + style suffix

**Fig 3.1 — Box-Color Decision**
- Draw: Decision tree: top "What access do you have?" → branches Black (no internals) → fuzz + observe; Grey (logs/config) → targeted probes; White (weights/prompts) → circuit/probe. Each leaf = right tool + artifact.
- Prompt: `decision tree diagram black box white box grey box testing choice based on access level --` + style suffix

**Fig 3.2 — Canary-Drift Loop**
- Draw: Circular loop: Fingerprint (model ID, serving, temp, prompt ver, date) → Run canary → Compare to baseline → Drift? → Alert + Pin environment → back to Fingerprint. Center = calendar icon "rerun on schedule / on change".
- Prompt: `circular loop diagram fingerprint run canary compare catch drift alert pin environment, center calendar icon --` + style suffix

**Fig 4.1 — A2A Message Flow**
- Draw: Four agent nodes in sequence (User → Planner → Executor → Writer + Subagent). Each arrow is a channel; each arrow has a red "injection surface" marker and a shield icon "secure the channel, not just the node". Bottom: tool calls branching off Executor.
- Prompt: `sequence diagram of four AI agents passing messages, each message arrow marked as injection surface with shield icon, tool calls branching --` + style suffix

**Fig 5.1 — Eval Pipeline**
- Draw: Five-box pipeline: Dataset (samples) → Solver (generate/react) → Judge Board (1 or 3 judges) → Score (accuracy/stderr) → Number with Denominator (e.g., "2/5 = 40%"). Denominator box emphasized with thick border + caption "always report n".
- Prompt: `horizontal pipeline diagram dataset solver judge board score number with denominator, final box emphasized --` + style suffix

**Fig 5.2 — LARA Architecture**
- Draw: Left: Target Agent with tools + sandbox. Top: Auditor/User driving the workplace scenario. Center: Verbatim law text box (Art. 5(1)(f)). Right: 3 judge icons → Majority reducer → PASS/FAIL badge. Bottom: 3000+ runs → compliance rate bar (7%–54%).
- Prompt: `architecture diagram target agent with tools auditor scenario verbatim law text three judges majority vote pass fail --` + style suffix

**Fig 5.3 — Two-Sided Boundary**
- Draw: Balanced scale / gate: left pan "Over-escalate — false alarms, trust lost", right pan "Under-escalate — confident-wrong ships, law broken". Center gate "Honest boundary + stated limitation". Below: "The honest number, not the clean one."
- Prompt: `balanced scale diagram over-escalate false alarms vs under-escalate confident wrong gate in middle labeled honest boundary --` + style suffix

**Fig 6.1 — Three Circles**
- Draw: Venn with three overlapping circles: Red Team ("find the failure"), Eval ("measure the rate"), Alignment ("steer the system"). Overlaps labeled; center = "Shared reproducible ruler". Outside each circle: when it's the right tool.
- Prompt: `venn diagram three overlapping circles labeled red team eval alignment, center shared ruler --` + style suffix

**Fig 7.1 — Tooling Stack**
- Draw: Four stacked blocks: Harness (custom scripts) + Breaklab (C2 lab) + Five-Test Repo (five boring failures) → all feed into Inspect (Task/Solver/Scorer/Log) → output Report + Log Viewer. Side note: "One clone, one run."
- Prompt: `stack diagram four blocks harness breaklab five test repo feeding into Inspect task solver scorer log viewer --` + style suffix

**Fig 8.1 — Engagement E2E**
- Draw: Six-step flow: Target → Map surface → Break (findings w/ denominator) → Measure (eval) → Report + Fix (with rerun) → Published Method. Each step has artifact icon; decision diamond "Can skeptic rerun it?" gates the last step.
- Prompt: `left to right flow diagram target map break measure report fix published method, each step with artifact icon --` + style suffix

**Fig 9.1 — Portfolio**
- Draw: Three pillars: "Harness (repo, runnable)" + "Write-Ups (2 articles, honest numbers)" + "One Published Finding (eval + log)" supporting a banner "The resume becomes optional." Below: roles it opens.
- Prompt: `three pillars diagram labeled harness writeups published finding supporting banner hired --` + style suffix

**Fig 10.1 — Threat Landscape**
- Draw: Radar/quadrant: four quadrants = Agentic/Multi-Agent, Memory Poisoning, Tool Supply Chain, Model Identity. Each has 2–3 sub-threats + trajectory arrow (arrow length = maturity). Center = "What we can measure today."
- Prompt: `radar quadrant diagram four emerging AI threats agentic memory poisoning tool supply chain model identity with trajectory arrows --` + style suffix

**Fig FM-1 — Primer**
- Draw: Three-step cycle: Break it → Measure it → Publish the check (arrows in circle). Center = checkmark icon. Below: "The check is the product. I build the check, not the claim. I would not report a number I could not reproduce."
- Prompt: `circular three step diagram break measure publish the check with central checkmark --` + style suffix

---

## 5. GLOSSARY SEED (one line each — full glossary in BM-1 will have ~120 terms)

> Shown here: 40 seed terms. The final glossary will include every bolded key term from each chapter (see Key Terms lists in TOC), plus all Inspect primitives, OWASP entries, and law terms. Each term = one line, no filler.

| Term | One-Line Definition |
|---|---|
| Adversarial example | An input crafted to make a model misbehave while looking normal to a human. |
| Adversarial training | Training on adversarial inputs so the model resists them — a defense, not a guarantee. |
| Agent | A model wrapped with planning, memory, and tools that acts over multiple turns. |
| A2A injection | An injection that travels inside agent-to-agent messages — secure the channel, not just the node. |
| Alignment | Steering a model to act as intended, including when intentions conflict — not just "be nice." |
| Attack surface | Every input, store, channel, and output where an attacker can enter or data can leak. |
| Black box | Testing with no internals; you learn by observing inputs and outputs. |
| Breaklab | Your local C2-style lab for running and logging attacks safely. |
| Canary | A small, fixed prompt you rerun on schedule to catch drift; the fingerprint makes it honest. |
| Check | A rerunnable test that prints pass/fail with a denominator — the product, not the opinion. |
| CIA triad | Confidentiality, Integrity, Availability — applied to AI with the model as an asset. |
| Clean number | The number after smoothing away limitations — not the one you publish. |
| Compliance rate | How often a model resisted a prohibited instruction, as a fraction (e.g., 2/5). |
| Data poisoning | Corrupting training or retrieval data so the model later misbehaves. |
| Denominator | The n in "2 of 5" — without it, a rate is not a measurement. |
| Drift | When the same prompt gives a different pass rate because the environment changed. |
| Environment fingerprint | Model ID + serving + temperature + prompt version + seed + date — logged every run. |
| Eval | A task + input + judge + metric + pass definition, built so a stranger can rerun it and get your number. |
| Eval awareness | When a model behaves differently because it detects it is being tested. |
| Five boring failure modes | Prompt injection, retrieval poisoning, tool poisoning, multilingual refusals, the missing check. |
| Five-test harness | Teamthy/ai-redteam-five-tests — the five-check harness you run against any target. |
| Grey box | Testing with partial internals (logs, config) but not weights. |
| Hallucination (confident-wrong) | A fluent answer that is false and delivered as truth — the honest boundary must catch it. |
| Harness | Your runner that executes checks and prints pass/fail with a count, not a screenshot. |
| Honest number | The rate with its denominator, seed, and stated limitation — not the clean one. |
| Indirect prompt injection | An injection that arrives via retrieved data, not the user message. |
| Inspect | The UK AISI open-source eval harness (Task/Solver/Scorer/Log) — your ruler. |
| Jailbreak | A prompt that bypasses a safety refusal or policy boundary. |
| Judge (LLM-as-judge) | A model that grades another model's output against a rubric; must be calibrated. |
| LARA | Aithos's Legal Assessment for Real-world Agents — 10 scenarios, verbatim law, 3-judge board, 96.7% agreement. |
| LARA-lite | The one-scenario, one-model Inspect lab you build in Ch. 5 — your first rerunnable compliance eval. |
| Least privilege | Give each component the minimum permission it needs — nothing more. |
| Majority reducer | The rule that takes three judge votes and returns the majority verdict. |
| Model extraction | Rebuilding or stealing model behavior via repeated queries. |
| Non-determinism | Same prompt, different output due to sampling/temperature/seed — why n>1 matters. |
| OWASP LLM Top 10 | The OWASP list of top LLM vulnerabilities, mapped to system components in Ch. 3. |
| RAG | Retrieval-Augmented Generation — retriever + store + generator; the store is untrusted input. |
| Reducer | The function that combines multiple judge scores into one verdict. |
| Red team | A motivated-stranger test that finds the failure, measures it, and makes the fix reproducible. |
| ... (extended to ~120 in final) | Threat model, tool poisoning, white box, verifier, etc. — all chapter key terms added. |

**Final glossary size:** ~120 terms (all chapter Key Terms + Inspect primitives + OWASP + law + Aithos/LARA + safety).

---

## 6. TIERING SCHEME (how §3's three levels appear in every chapter)

Every chapter is written in three visible layers, badged in the margin:

**[F] Foundation — The Idea (beginner, no prerequisites)**
- Badge: green circle "F — Foundation"
- Language: plain, one concrete example, no jargon without definition
- Goal: a beginner is not lost; can answer "what is this and why does it matter?"
- Example lead: "An eval is a ruler. You decide what counts as pass, then you measure."

**[P] Practitioner — The Mechanics + Examples + Lab (actually do it)**
- Badge: amber circle "P — Practitioner"
- Language: tools, steps, commands, failure modes, env fingerprint
- Goal: a practitioner can do it today with the named tooling
- Every lab states: target, steps, expected output, how to know you passed, env to log

**[R] Researcher — Expert Extension + open problems (push it)**
- Badge: red circle "R — Researcher"
- Language: method, measurement, bias, agreement rate, open problem + method you'd bring
- Goal: an expert is not bored; gets a method they can run or a problem they can publish on
- Located at end of each chapter (Expert Extension) + woven notes in mechanics where relevant (e.g., judge-calibration note in Ch. 5 mechanics)

**Flow within a chapter:** The idea → Do it → Push it. Foundation first, then Practitioner, then Researcher. A reader can:
- Read only [F] blocks to get the shape (beginner path)
- Read [F]+[P] to get the craft (practitioner path)
- Read all three to get method + open problems (research path + expert jump-in)

**Visual execution in LaTeX:** Margin badges via `marginnote` + `tcolorbox`; [F]/[P]/[R] labels also in section subtitles. The "How to Use This Book" front matter explains the badges with a sample page illustration.

---

## 7. CALLOUT BOXES (5 types, visually distinct)

| Box | Color | Icon | Use |
|---|---|---|---|
| **Definition** | Blue (`#2563EB`) | `≡` | Term + one-line definition, first use in chapter |
| **Worked Example** | Slate (`#334155`) | `▸` | Named, concrete, with real numbers/provisions/attacks |
| **Lab** | Green (`#059669`) | `⚙` | Steps + expected output + deliverable + "how to know you passed" |
| **Pitfall** | Amber (`#D97706`) | `⚠` | What goes wrong + the missing check that catches it |
| **The Check Is the Product** | Black (`#111827`) w/ red accent | `✓` | Short voice note where thesis genuinely fits — not forced in every section |

---

## 8. ACCEPTANCE BAR (how we will prove §9 is met)

- Beginner can start at Ch. 0 → reach Ch. 5 with no reference book — checked by: no prerequisite jargon without definition, every lab lists exact commands, Ollama path is free/local
- Expert can jump to Ch. 5 + extensions and get a method — checked by: Ch. 5 mechanics cover Inspect primitives + judge board + agreement measurement + drift; each extension names open problem + method
- Every chapter has ≥1 figure, ≥1 worked example (actually ≥2), ≥1 lab, 5-Q self-test, ready-when — checked by TOC enforcement
- Stranger can run LARA-lite and reproduce a number — checked by: `lara_lite.py` is verbatim, includes `pip install` + `ollama pull` + `inspect eval` + `inspect view` + honest-report template
- Thesis woven — checked by: primer + base bar on Fig 0.1 + callout boxes where genuine + honest-number discipline in every lab/report template

---

## 9. WHAT HAPPENS AFTER APPROVAL

**Phase B — Write:** One chapter at a time, on your "go" per chapter, each with all 11 elements. Order: Front Matter → Ch. 0 → Ch. 1 → Ch. 2 → … → Ch. 10 → Back Matter. You say "go" to approve each chapter before the next.

**Phase C — Illustrate:** For each chapter, figure files generated in `manual/figures/` (SVG + PNG) plus prompt list. Style-locked.

**Phase D — Assemble:** Single `manual/main.tex` + `manual/figures/` → compiled PDF (`manual/main.pdf`) + `manual/main.tex` as artifact. Includes running headers, page numbers, numbered sections/figures, back-matter templates, index.

---

## 10. APPROVAL REQUEST

Please reply with one of:

- **"Approved — proceed to Phase B"** — I will start with Front Matter + Chapter 0 (or tell me which chapter to start with)
- **"Approved with changes: …"** — list changes, I will update this plan and re-present
- **"Show me … first"** — e.g., a sample LaTeX page, a draft of `lara_lite.py`, or the full glossary draft

No writing beyond this plan will begin until you approve.

