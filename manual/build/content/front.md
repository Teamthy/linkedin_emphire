@cover

@fh2 Reproducibility Notice
This manual is built on one rule: **I would not report a number I could not reproduce.** Every lab, every worked example, and every figure in this book is meant to be rerun. Where a number appears, its denominator appears with it. Where a claim appears, its check appears with it.

If you rerun a lab and get a different number, that is not failure. It is the finding. Log the whole-environment fingerprint (model ID, serving, temperature, prompt version, seed, date) and report the delta.

**License:** Creative Commons CC BY-SA 4.0 for text and figures you produce from the templates. Inspect, LARA, OWASP, EU AI Act text, and third-party trademarks remain with their owners.

**How to cite:** `Breaking AI: The Complete Guide to AI Red Teaming, AI Safety, and AI Research — Study Manual v1.0. The check is the product.`

**How to report a reproduction failure:** Open an issue with target, fingerprint, n, and the transcript where the judge and you disagree. That disagreement is data.

@sig I build the check, not the claim.

@small Nairobi · Lagos · Remote — 2026

@frontchapter How to Use This Book
This book has one spine and three ways to walk it. Pick the path that matches your deadline. All three end with a check a stranger can rerun.

@fh2 The three paths
:::path1
**For:** You have a screen or take-home in about 14 days.
**Read:** Front Matter → Chapter 0 → Chapter 1 → Chapter 5 (the evals core, longest chapter) → the Aithos Sprint summary at the end of Ch. 5 → Chapter 9 (positioning).
**Do:** Lab 5 (LARA-lite) end to end. Run it on Ollama. Get 2/5 or 4/5. Report it honestly.
**Budget:** 1 hr study + 1.5 hr hands-on per day, 14 days. The hands-on is non-negotiable.
**You are ready when:** A stranger can run your `lara_lite.py` and get your number, or find the exact line where you were wrong.
:::
:::path2
**For:** You want the whole craft — break, measure, publish.
**Read:** Front Matter → Chapters 0–10 in order. Do every lab. Artifacts stack into a portfolio.
**Budget:** One chapter per week. Each lab is 90–180 min.
**You are ready when:** The Ch. 8 lab is done — one full engagement (target → map → break → measure → report + fix → published method).
:::
:::path3
**For:** You already break systems; you want to publish checks.
**Read:** Primer → Ch. 5 Mechanics + Lab 5 → Ch. 6 → Ch. 7 (Inspect deep dive) → every Expert Extension across Ch. 0–10.
**Budget:** 2–3 focused days.
**You are ready when:** You can name three open problems and the method you would bring to each (Ch. 10 Lab).
:::

@fh2 What you need (and do not need)
- **You need:** A laptop, Python 3.10+, `pip install inspect-ai`, Ollama (`ollama pull llama3.1`), a text editor. No API keys for the free path — Ch. 5 runs locally. For the judge board, add up to 3 provider keys when you have them.
- **You do not need:** A frontier-lab account, a GPU cluster, a formal ML degree, or permission to start. Ch. 0 explains safe boundaries.
- **Cost:** $0 for the local path. Provider-judge runs cost cents per eval if you use APIs.

@fh2 How the tiers work
Every chapter is marked with three tiers. Read the tier that matches you: a beginner reads **[F] Foundation**, a practitioner reads **[F] + [P]**, a researcher reads everything.

| Badge | Tier | What you get |
|---|---|---|
| **F** | Foundation | The concept in plain language, one concrete example, no prerequisites |
| **P** | Practitioner | The steps, the tooling, the failure modes, the env fingerprint to log |
| **R** | Researcher | The measurement, the bias, the open problem, how to contribute |

Flow in every chapter: **The idea → Do it → Push it.** Beginner not lost. Expert not bored.

@fh2 How to read a lab
Every lab has: **Target** (what you test), **Steps** (what you run), **Expected output** (what you should see), **Deliverable** (what you ship), **How you know you passed** (the check). Log the environment fingerprint every time.

| Field | Example |
|---|---|
| Model ID | `ollama/llama3.1` or `openai/gpt-4o` |
| Serving | local Ollama 0.5 / API |
| Temperature | 0 or 0.7 |
| Prompt version | git SHA or date |
| Seed | 0, 1, 2 … (Inspect sets this) |
| Date | 2026-10-20 |
| Epochs / n | 5 |

@fh2 A note on safe practice and ethics
What you may break: systems you own, local models, authorized targets, published sandboxes. What you must not: production data, real users, unauthorized infrastructure. The line between red team and attack is consent and scope. Ch. 0 §0.4 gives the full boundary. When in doubt, use Ollama locally.

@pull Break before users do. Secure the channel, not just the node.

@frontchapter The Check Is the Product — One-Page Primer
:::check
The check is the product. If you cannot rerun the failure, you have not found it, you have had an opinion.
:::

Most people can break a demo. Few can turn a break into a reproducible number anyone can rerun and question. You will do both. That is the scarce skill.

@fh2 The three moves
1. **Break it.** Find the failure. One input that should be refused, but is not. One tool call that should be blocked, but goes through.
2. **Measure it.** Turn the anecdote into a rate. *The number with a denominator:* 2 of 5 (40%), 7 of 20 (35%), 0 of 10 (0%). No denominator, no measurement.
3. **Publish the check.** Ship the harness, the seed, the env fingerprint, the judge rubric, and the limitation. A skeptic reruns it and gets your number — or finds the exact line where you were wrong. Either way, the field moves forward.

@fh2 The honest number, not the clean one
The clean number hides the limitations. The honest number names them: "Model X resisted the Art. 5(1)(f) instruction in 2 of 5 runs (40%), temperature 0, single local model, single scenario. Limitation: one provision, one model, n=5." I would not report a number I could not reproduce. I build the check, not the claim.

@fh2 The denominator
A rate without n is a vibe. "It mostly resists" means nothing. "3/10 = 30%" means you ran ten times and it resisted three. Same model, different temperature or seed, different number — and that is expected. Log it, report it, let the reader decide.

@fh2 Break before users do — secure the channel, not just the node
A system fails where trust is misplaced: a retrieved doc treated as instruction, a tool description read as permission, an agent message trusted because it came from another agent. The fix is not a better prompt. It is a check that fails closed, a channel that is secured, a boundary that is tested on a schedule.

@fig figFM-1.png Break → Measure → Publish the check. The loop only closes when the check is runnable by a stranger.

@sig I build the check, not the claim. Every chapter ends with a deliverable a skeptic can rerun. That is the standard. The rest is talk.

@toc
@lof
