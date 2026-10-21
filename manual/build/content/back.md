@back Glossary
@small Every key term, one line each. Terms that appear as chapter Key Terms are included; Inspect, OWASP, and law terms added.

| Term | Definition |
|---|---|
| **A2A injection** | Injection that travels inside agent-to-agent messages. |
| **Adversarial example** | Input crafted to make a model err while looking normal. |
| **Adversarial training** | Training on adversarial inputs to resist them — a defense, not a guarantee. |
| **Agent** | Model + planning + memory + tools + subagents acting over multiple turns. |
| **Agent inventory** | Count of every agent, capability, and delegation path — you cannot secure what you do not inventory. |
| **Agentic threat** | Failure that appears only when agents delegate, remember, or chain tools. |
| **Alignment** | Steering a system to act as intended under conflict, including governance legitimacy. |
| **Approval gate** | Control outside the model that denies by default; the agent cannot rewrite it. |
| **Attack surface** | Every input, store, channel, and output where entry or leak is possible. |
| **AuthN** | Authentication — who called. |
| **AuthZ** | Authorization — what they may do; the agent may not rewrite it. |
| **Black box** | Testing with no internals; learn by observing inputs/outputs. |
| **Breaklab** | Your local lab (`Teamthy/My-Breaking-lab`) for safe logging of attacks. |
| **Canary** | Small, fixed, scheduled check with a logged fingerprint to catch drift. |
| **Check** | A rerunnable test that prints pass/fail with a denominator — the product. |
| **CIA triad** | Confidentiality, Integrity, Availability — with the model as a first-class asset. |
| **Clean number** | Number after smoothing away limitations — not the one you publish. |
| **Compliance rate** | How often a model resisted a prohibited instruction, as a fraction (e.g., 2/5). |
| **Contain-the-danger** | Alignment framing: contain powerful AI so it does not harm. |
| **Continuous monitoring** | Logging every prompt/tool/output + alerting on drift. |
| **Continuous testing** | Canary + fingerprint + rerun on schedule — what makes a number stay honest. |
| **Data poisoning** | Corrupting training/retrieval data so the model later misbehaves. |
| **Denominator** | The n in "2 of 5" — without it, a rate is not a measurement. |
| **Drift** | Same prompt, different pass rate because the environment changed. |
| **Environment fingerprint** | Model ID + serving + temperature + prompt version + seed + date + n. |
| **Ethical resistance** | A model's ability to refuse a prohibited instruction and offer an alternative. |
| **Eval** | Task + input + judge + metric + crisp pass definition, built to be rerun. |
| **Eval awareness** | Model behaves differently when it detects it is being tested. |
| **Exfiltration** | Sending data to a recipient outside scope — must be blocked by allowlisting. |
| **Fail-closed** | Deny by default; the agent cannot override. |
| **Five boring failure modes** | Prompt injection, retrieval poisoning, tool poisoning, multilingual refusals, missing check. |
| **Five-test harness** | `Teamthy/ai-redteam-five-tests` — the five-check harness. |
| **Foundation** | Tier F — the idea in plain language, no prerequisites. |
| **GDPR** | EU data protection regulation — transparency, minimisation, purpose limitation. |
| **Grey box** | Testing with partial internals (logs/config) but not weights. |
| **Hallucination (confident-wrong)** | Fluent false answer delivered as truth — must be caught by the two-sided boundary. |
| **Harness** | Runner that executes checks and prints pass/fail with a count, not a screenshot. |
| **Hard line** | EU AI Act Art. 5 prohibited practice — no justification crosses it. |
| **Honest number** | Rate with denominator, seed, and limitation — not the clean one. |
| **Indirect prompt injection** | Injection arriving via retrieved data, not the user message. |
| **Infrastructure security** | API protection, authN/authZ, rate limits, audit logs. |
| **Insecure deserialization** | Code-injection via deserializing untrusted data. |
| **Inspect** | UK AISI open-source eval harness (Task/Solver/Scorer/Log). |
| **Instruction hierarchy** | System > Developer > User > Tool output — who wins on conflict. |
| **Interpretability** | Probing, features, circuits — what a model represents/computes (needs evals to pair). |
| **Jailbreak** | Prompt that bypasses a safety refusal or policy boundary. |
| **Judge (LLM-as-judge)** | Model grading another model against a rubric; must be calibrated. |
| **Judge biases** | Position, verbosity, self-preferential, sycophancy — four to name. |
| **Kill switch** | Orchestration-level stop that survives subagent spawning; not in the prompt. |
| **LARA** | Aithos Legal Assessment for Real-world Agents — 10 scenarios, verbatim law, 3 judges, 96.7% agreement. |
| **LARA-lite** | One-scenario, one-model Inspect lab — your first rerunnable compliance eval. |
| **Least privilege** | Give each component the minimum permission it needs. |
| **LLM** | Generative model for text trained to predict the next token at scale. |
| **Majority reducer** | Rule that takes 3 judge votes and returns the majority verdict. |
| **Memory poisoning** | Poisoned persisted fact that changes future decisions. |
| **Model extraction** | Rebuilding/stealing model behavior via repeated queries. |
| **Model identity** | Which model answered — may be unknowable behind a proxy without pinning. |
| **Model inversion** | Reconstructing what a model learned or memorized. |
| **Model manipulation** | Steering what a model learned toward an attacker goal. |
| **Negative result** | Where the system did pass — still data, still published. |
| **Non-determinism** | Same prompt, different output due to sampling/temperature/seed. |
| **Observability** | Logging every tool call, delegation, and message with provenance. |
| **Outbound allowlisting** | Agent may only call approved domains — a control outside the model. |
| **OWASP LLM Top 10** | Known LLM vulnerability families, mapped to components. |
| **Pass definition** | What counts as pass/fail — the whole eval. |
| **Pluralism / Legitimacy** | Alignment framing: how AI is made/governed legitimately, whose values are included. |
| **Practitioner** | Tier P — how to do it with tooling, steps, failure modes. |
| **Prompt engineering** | Control via prompt — a system, not a trick; version it. |
| **Prompt injection (direct)** | User-written injected instruction. |
| **Probing / Features / Circuits** | Interpretability methods — correlation, not yet a behavioral guarantee. |
| **Provenance** | Where a message/fact/doc came from, when, via whom. |
| **RAG** | Retrieval-Augmented Generation — retriever + store + generator; the store is untrusted input. |
| **RCE** | Remote code execution — the agent must be sandboxed. |
| **Reducer** | Function combining multiple judge scores into one verdict. |
| **Red team** | Scoped authorized test by a motivated stranger returning a rerunnable check. |
| **Researcher** | Tier R — method, measurement, open problems, contribution. |
| **Responsible disclosure** | Owner first, time to fix, check shared, then publish the method (not the weapon). |
| **Risk management** | How likely, how bad, what fix and its cost. |
| **Robust design** | Validation, hierarchy, allowlisting — architecture defense. |
| **Sample (Inspect)** | One input + target (the judge criterion). |
| **Sandbox** | Isolated execution (docker) for agent tool calls. |
| **Score** | The graded outcome + metrics (accuracy, stderr). |
| **Scorer (Inspect)** | How the answer is graded (`match`, `includes`, `model_graded_fact`…). |
| **Seed** | Randomness pin — must be logged. |
| **Serving** | How the model is hosted (local Ollama, API, proxied) — part of the fingerprint. |
| **Shared ruler** | Versioned rerunnable eval a vendor, regulator, and researcher all accept. |
| **Solver (Inspect)** | How the model is run (`system_message`, `generate`, `react`…). |
| **Supply-chain pinning** | Inventory + fingerprint that alerts on a silent vendor/model swap. |
| **Task (Inspect)** | The eval: dataset + solver + scorer. |
| **Temperature** | Sampling parameter; higher = more variation. |
| **Threat model** | Attacker, asset, success, scope — four lines bounding any test. |
| **Tool poisoning** | Tool description that overwrites safety/approval logic. |
| **Tool supply chain** | Vendor tools/plugins whose descriptions are an attack surface. |
| **Two-sided boundary** | Over-escalate (false alarms) vs under-escalate (confident-wrong ships). |
| **Vulnerability assessment** | Where, how, and how far one bad input travels. |
| **White box** | Testing with full internals (weights/prompts/configs). |

@back Reproducible-Report Template
@small Fill one page per finding. The honest number goes here, not the clean one.

**Title:** ____________________

**Target + Scope:** ____________________ **Date:** ____________

**Threat model (4 lines):**
| | |
|---|---|
| **Attacker** | |
| **Asset** | |
| **Success (attacker)** | |
| **Scope (out of scope)** | |

**Environment fingerprint (log every field):**
| | |
|---|---|
| **Model ID** | |
| **Serving** | |
| **Temperature** | |
| **Prompt version** | |
| **Seed** | |
| **Date** | |
| **n / epochs** | |

**Check: what is pass/fail?**
____________________

**Harness (how to rerun):**
____________________

**Result — honest number (rate + n + stderr):**
| | |
|---|---|
| **Before fix** | |
| **After fix** | |
| **Controls (lawful side)** | |

**Transcripts / log:** ____________ (`inspect view` or attached log)

**Limitation (what you did NOT test):**
____________________

**Fix (control outside the model where possible):**
____________________

**Disclosure:** ____________ **Canary scheduled:**  Yes  No

@small I would not report a number I could not reproduce. A skeptic can rerun: ____________

@back Threat-Model Worksheet
@small Fill before any test. One row per asset/entry.

| **Asset** | **Attacker** | **Entry (prompt / RAG / tool / A2A)** | **Propagation (how far does one bad input travel?)** | **Impact if success** |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

**Controls (outside the model where possible):**
| **Control** | **Where it lives (channel / gate / allowlist)** | **How you test it (n, pass)** |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

:::check
**How to use this sheet**
1. List every asset (data, behavior, control, compliance status, reputation).
2. For each, name the attacker and entry — especially retrieval, tool, and A2A channels, not just the prompt.
3. Trace propagation: if the entry is poisoned, which outputs and tool calls are affected? Mark the hops.
4. Add a control outside the model for each row. Test each control with a count (n ≥ 10).
:::

@back Red-Team Engagement Checklist
:::box
**ENGAGEMENT — Target to Published Method**
1. **Pre-engagement** — Scope in writing: target, window, data handling, out-of-scope, contact. Consent filed.
2. **Map** — Attack surface (Fig 2.1) + agent architecture (Fig 4.1 if agentic). Trust boundaries marked. Inventory every agent/tool.
3. **Harness + canary baseline** — Ran the five boring failure modes + built the canary (Fig 3.2) with fingerprint logged. Baseline stored.
4. **Break** — Found at least one failure that should be refused/blocked but is not. Denominator ≥ 10. Traced how far one bad input traveled.
5. **Measure** — Built the Inspect eval for the critical prohibition. Judge rubric = verbatim text. Single judge or a board of 3 + majority. Human spot-check done.
6. **Report the honest number** — Rate + n + seed + temp + model + serving + date + limitation. Both sides of the boundary tested (prohibited + lawful). Traces + transcripts (redacted).
7. **Fix** — A control outside the model (allowlist, gate, channel policy, input marking) that fails closed. Before/after numbers shown.
8. **Disclose** — Owner notified with the check + logs + fix idea. Window given (often 90 days).
9. **Fix-rerun** — Reran the same harness after the fix, same n, same seed. Canary now scheduled.
10. **Published method** — Repo public, pinned versions, one-liner run, log via `inspect view`. Write-up shared. Limitation stated. No PII, no weaponized variant.
:::
@small Gate at every step: Can a skeptic rerun it? If no, you are not done. The check is the product.

**CFO-readable line (fill one sentence):**
____________________

**Supply-chain pin:** Model ID ________ Serving ________ Vendor ________ Date pinned ________

@back Index
@small Key terms, figures, and labs.

| Entry | Chapters / Figures |
|---|---|
| A2A injection | Ch. 4, Fig 4.1 |
| Adversarial training | Ch. 2 |
| Agent (architecture) | Ch. 1, 4, Fig 4.1 |
| Agentic threats | Ch. 10, Fig 10.1 |
| Art. 5(1)(f) (emotion inference) | Ch. 0, 5 Lab, 6, 8 |
| Attack surface map | Ch. 2, Fig 2.1; Ch. 3 Lab |
| Black / white / grey box | Ch. 3, Fig 3.1 |
| Breaklab | Ch. 1, 7 |
| Canary / drift / fingerprint | Ch. 3, Fig 3.2; Ch. 5, 7, 8; checklist |
| Channel (secure the channel) | Ch. 4, Fig 4.1 |
| Check (the check is the product) | Primer, Ch. 0, Fig 0.1; all labs |
| CIA / threat model | Ch. 1, 2 |
| Clean vs honest number | Primer, Ch. 5, Fig 5.3 |
| Data poisoning / RAG poison | Ch. 2, 3 |
| Denominator | Primer, Ch. 5; every report template |
| EU AI Act / GDPR | Ch. 5, 8 |
| Evals (Inspect) | Ch. 5, Fig 5.1; Ch. 6, 7, Fig 7.1 |
| Five boring failure modes | Ch. 3 |
| Five-test harness | Ch. 1, 7 |
| Inspect (Task/Solver/Scorer/Log) | Ch. 5, 7 |
| Interpretability | Ch. 6 |
| Jailbreak / prompt injection | Ch. 2, 3 |
| Judge (LLM-as-judge, board, biases) | Ch. 5, Fig 5.2 |
| Kill switch | Ch. 4 |
| LARA / LARA-lite | Ch. 5, Fig 5.2; Lab 5 |
| Memory poisoning | Ch. 4, 10, Fig 10.1 |
| Model extraction / identity | Ch. 2, 10 |
| OWASP LLM Top 10 | Ch. 3 |
| Portfolio (harness + write-ups + finding) | Ch. 9, Fig 9.1 |
| RAG / tool security | Ch. 1, 2, 3 |
| Red team vs eval vs alignment | Ch. 6, Fig 6.1 |
| Responsible disclosure | Ch. 0, 6, 8 |
| Supply chain / pinning | Ch. 8, 10 |
| Threat-model worksheet | Back matter |
| Tool supply chain | Ch. 10, Fig 10.1 |
| Two-sided boundary | Ch. 5, Fig 5.3 |

@back References and Resource Map
@h2 Frameworks
- **Inspect** — `inspect.aisi.org.uk` (tutorial, tasks, solvers, scorers, sandboxing, agents, log viewer). Source: `github.com/UKGovernmentBEIS/inspect_ai` (MIT). Install: `pip install inspect-ai`.
- **LARA** (Legal Assessment for Real-world Agents) — `aithos.org/article/Aithos-LARA/`; leaderboard `lara.aithos.org`. Method: 10 scenarios, verbatim law, 3 judges (GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro Preview), majority vote, 3000+ runs, 96.7% human agreement.

@h2 Law
- **EU AI Act** — EUR-Lex; Article 5 (prohibited practices), Art. 5(1)(f) emotion inference in workplace/education.
- **GDPR** — transparency, data minimisation, purpose limitation, lawful processing (indicators).

@h2 Red teaming
- **OWASP LLM Top 10** — `owasp.org` (`LLM01`–`LLM10`, mapped in Ch. 3). OWASP Agentic Security.

@h2 Your stack
- `Teamthy/ai-redteam-five-tests` — five-test harness.
- `Teamthy/My-Breaking-lab` — breaklab.
- **Ollama** — `ollama.ai` — local models for free practice runs.

@h2 Judge reliability
- LLM-as-judge guidance: position, verbosity, self-preferential, sycophancy bias — LARA's 96.7% as the reference point.

@h2 How the roadmap folds in
| Roadmap branch | Chapters |
|---|---|
| Introduction / AI Security Fundamentals | Ch. 0 |
| AI/ML Fundamentals + Foundational Knowledge | Ch. 1 |
| Cybersecurity Principles + System Security | Ch. 2 |
| Testing Methodologies | Ch. 3 |
| Agentic AI Security | Ch. 4 |
| Tools and Frameworks | Ch. 7 |
| Real-world Applications | Ch. 8 |
| Professional Development | Ch. 9 |
| Future Directions | Ch. 10 |
| Four roadmap roles (Data Scientist / AI Engineer / Analyst / NLP) | Ch. 1 (base), Chs. 5–6 (research), Chs. 2–4 (engineer/security) |

@sig The check is the product. If you cannot rerun the failure, you have not found it, you have had an opinion.
@small Manual v1.0 — print-ready A4 — 2 cm margins — 2026
