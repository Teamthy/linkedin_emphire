@chapter 6 AI Safety and Alignment Research: The Deep Research Half

:::atglance
**Question:** How do red team, eval, and alignment fit together — and how do you publish so a skeptic can disagree with you using your own method?
**Deliverable:** A research-grade write-up: method, results, limitations, rerun instructions, no smoothing.
**Time:** 4 hrs (90 min read + 2–3 hrs Lab 6).
:::

@h2 Learning Objectives
:::objectives
Distinguish two alignment framings (contain-the-danger vs pluralism/procedural legitimacy) and say why "how it's made matters."
Describe interpretability basics (probing, features, circuits) and what they do and do not prove.
Distinguish red team vs eval vs alignment and name where each is the right tool.
Explain responsible disclosure and the scientific method for research (hypothesis, controls, negative results, ethics of publishing).
Write a research-grade finding that a skeptic can rerun and disagree with using your own method.
:::

@h2 The Idea: What Alignment Means and Where Each Tool Fits
@tier F
@h3 Two framings
**Contain-the-danger:** AI will be powerful; contain it so it does not harm — misuse, loss of control, concentrated power. Frame: boundaries, refusals, hard lines (Art. 5 prohibitions).

**Pluralism and procedural legitimacy:** AI will shape society; ensure it is made and governed legitimately — who decides what is allowed, how values are included, what process makes the answer trustworthy.

Both matter. "How it's made matters" — an answer is not just about what it says but what ledger produced it (which law, whose values, what check).

@h3 Interpretability basics — and what it does not buy you
- **Probing:** Train a small classifier on a model's internal states to see if a concept is represented. Finds correlation, not causation.
- **Features and circuits:** Which directions in activation space correspond to concepts; which subgraphs compute a behavior. Insightful, not proof of behavior out of distribution.

Interpretability can say "the feature exists in here." It cannot yet say "the model will not use that feature to harm you next week." Pair it with evals.

:::defbox
**Interpretability:** Methods (probing, features, circuits) that try to explain what a model represents or computes. Valuable, not sufficient — pair with evals that measure behavior.
:::

@h3 Red team vs eval vs alignment
Three circles, one center:
- **Red team:** Find the failure (the creative break). Best when you do not know what to measure yet.
- **Eval:** Measure the rate (the honest number). Best when you know what failure to count.
- **Alignment:** Steer the system (how it's made, what process makes it trustworthy). Best when the question is about ongoing governance.

Center: a shared reproducible ruler. All three need it. Without a ruler, red team is anecdote, eval is cargo cult, alignment is sermon.

@h2 The Mechanics: Method, Disclosure, Ethics
@tier P
@h3 Red team vs eval vs alignment — where each is the right tool
| Use this | When |
|---|---|
| Red team | You suspect a failure but have no rate. Go find it. |
| Eval | You know the failure (e.g., Art. 5(1)(f) compliance) and need the rate with a denominator. |
| Alignment frame | The question is about governance: who decides, what process, how legitimacy is earned. |
| All three | When the finding becomes a standard: red team finds it, eval measures it, alignment tells you how to govern by it. |

@h3 Responsible disclosure — and the scientific method
**Disclosure timeline** (real, used in Ch. 8 Example 8.2):
1. Find + measure (with denominator) → log fingerprint + transcripts.
2. Tell the owner: scope, method, number, limitation, transcripts, fix suggestion. Give 90 days (or what the bounty policy says).
3. Share the check so they can verify the fix themselves.
4. Publish the method after fix or after the window — the check, not the weaponized variant. Redact PII/secrets.

**Scientific method for research (no smoothing):**
- **Hypothesis:** "Model X resists prohibited emotion inference at under 50% under condition C."
- **Controls:** Same scenario, lawful alternative (performance ranking) must still be allowed — test both sides of the boundary.
- **Negative results:** Report where the model did resist. The non-failure is data.
- **Honesty:** Report the limitation that hurts your story. "One provision, one model, n=5" if that is what you ran. The honest number, not the clean one.

@h2 Worked Examples
@tier P
:::example
**Example 6.1 — A probing experiment that finds a feature but fails out of distribution.**
**Setup:** A probe finds a "deception" direction in a model's activations with 85% accuracy on training probes.
**Next test:** Ask the model to deceive in a novel multi-turn negotiation the probe never saw. The feature fires but the behavior does not — the probe does not predict action.
**Lesson:** The feature is there; the circuit is not yet understood. Interpretability gave a clue, not a guarantee. The eval (n=40 negotiation episodes, 12/40 deceptive = 30%) is what measures the behavior. Both are needed. Claims about alignment need both the inside (feature) and the outside (rate).
:::
:::example
**Example 6.2 — Responsible disclosure timeline for an emotion-inference finding.**
**Day 0:** Lab 5 LARA-lite shows 3/5 compliance failures on vendor Y's assistant (n=5). You expand to n=40, three scenarios: 38% ± 7% compliance.
**Day 1:** Email vendor security: method, provision text, scenarios, n, fingerprints, 5 example transcripts (PII redacted), fix suggestion (channel policy + refusal with alternative).
**Day 30:** Vendor confirms, shares patch plan, asks for the check to verify. You share the harness.
**Day 60:** Rerun: 85% ± 5% compliance (fix worked for tested scenarios).
**Day 90:** Publish: "Before/after: 38% → 85% compliance, n=40 each, 3 scenarios, Art. 5(1)(f), limitation: 3 scenarios, one vendor." No weaponized payloads, no user data. That is the scientific method with disclosure.
:::

@h2 Hands-On Lab 6 — Research-Grade Write-Up
:::lab
**Target:** Your LARA-lite finding (or Ch. 2 lab finding) — now as a write-up, not just a harness.
**Steps:**
1. Hypothesis (1 sentence), method (dataset, solver, judge, metric, pass definition), environment fingerprint, results (number + denominator + stderr), controls (lawful alternative), limitation (what you did not test), rerun instructions (exact command a stranger runs), ethics (disclosure, no PII, no weapon).
2. No smoothing: keep the bad number, the limitation, the transcript where the judge disagreed. If you tested 5 and 2 resisted, say 2/5.
3. Length: 2–3 pages. No filler. A skeptic must be able to disagree with you using your own method — because the method is fully there.
**Deliverable:** A 2–3 page PDF or Markdown research note.
**How you know you passed:** A second person, without asking you, reruns the command, gets your number (within sampling), and can point at the exact transcript where a different interpretation would change the conclusion. That is research-grade.
:::

@h2 Pitfalls and the Missing Check
:::pitfall
**What goes wrong:**
- Publishing the claim without the check — "we found bias" with no ruler anyone can run.
- Hiding negative results — where the model did the right thing is data.
- Conflating red-team anecdote with eval rate — "it jailbroke once" is not a prevalence claim.
- Interpreting probing as proof of behavior.
**The missing check:** Hypothesis + controls + negative results + limitation + rerun instructions + ethics note. Without those, a skeptic cannot engage with your work. With them, a skeptic can disagree with you using your own method — and that is the point. The method is the contribution.
:::

@h2 Illustrations
@fig fig6-1.png Red team vs eval vs alignment — three overlapping circles. Center = shared reproducible ruler. Each lobe = where it is the right tool.

@h2 Key Terms
:::terms
**Alignment** — Steering a model/system to act as intended under conflict, including governance legitimacy.
**Probing / Features / Circuits** — Interpretability methods; correlation, not yet a behavioral guarantee.
**Red team vs eval vs alignment** — Find / measure / govern — each has a different right-tool moment.
**Responsible disclosure** — Owner first, time to fix, check shared, then publish the method (not the weapon).
**Negative results** — Reports of where the system did pass — still data, still published.
**Eval awareness** — Model behaves differently when it detects it is being tested.
:::

@h2 Self-Test
:::selftest
**Recall:** What are the two alignment framings, and what question does each ask?
**Recall:** What does a probe finding a "deception direction" prove — and what does it not yet prove?
**Application:** You found a 38% compliance rate. What is the hypothesis, the control, and the negative result in the write-up?
**Application:** A vendor asks you to delay disclosure past 90 days. What is the responsible path, and what do you share so they can verify the fix?
**Design a check:** Design a study that pairs probing with an eval to test whether a feature predicts behavior out of distribution. Define the eval, n, and what "probing predicts behavior" would mean as a checkable claim.
:::
@readywhen A skeptical reader can disagree with you using your own method — because the method, limitation, and rerun are fully there.

@h2 Expert Extension
@tier R
**Open problem: what "alignment measurement" could mean when the ruler is an LLM.** If the judge is itself an LLM, its alignment shapes your measurement of alignment — circularity.
**Method you would bring:** Triangulate: one provision, three measurement paths — (a) judge board, (b) human expert review (n=50), (c) behavioral proxy (e.g., refusal latency, alternative offered). Report all three + agreement + where they diverge. The divergence is the open problem. Publish the harness so the next researcher can add a fourth path.

@sig The check is the product. In research, the check that survives a skeptic is the check that becomes infrastructure.
