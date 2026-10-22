@chapter 7 Tools, Frameworks and Infrastructure: The Stack You Point At

:::atglance
**Question:** What stack lets a stranger clone and reproduce your finding in one session?
**Deliverable:** A repo a stranger can clone and run in one session — harness + breaklab + five-test repo + Inspect.
**Time:** 3–4 hrs (60 min read + 2–3 hrs Lab 7).
:::

@h2 Learning Objectives
:::objectives
Name the tooling families (testing platforms, monitoring, benchmark datasets, custom scripts, reporting) and where each sits in the workflow.
Describe Inspect in depth: tasks, solvers, scorers, model_roles, sandboxes, agents, and reading the log.
Wire your harness + breaklab + five-test repo into one stack with one clone + one run.
Read an Inspect log sample by sample and find the exact turn where a tool call went wrong.
:::

@h2 The Idea: The Stack Is One Clone, One Run
@tier F
You do not need ten tools. You need a stack a stranger can clone and run in one session. Four pieces:
1. **Your harness** — custom scripts that run checks and print pass/fail with a count.
2. **Breaklab** — `Teamthy/My-Breaking-lab` — your local lab for logging attacks safely.
3. **Five-test repo** — `Teamthy/ai-redteam-five-tests` — the five boring failure modes.
4. **Inspect** — the UK AISI eval harness — the ruler that turns a harness into a published eval.

Output: report + log. Input to clone: one repo, one command (`inspect eval ...`), one env fingerprint.

:::defbox
**Stack (here):** Harness + breaklab + five-test repo + Inspect → report + log. One clone, one run, one reproducible number.
:::

@h2 The Mechanics
@tier P
@h3 Testing platforms, monitoring, benchmarks, custom scripts, reporting — where each sits
| Family | In the workflow |
|---|---|
| Testing platforms (Inspect, etc.) | The runner + judge — where evals are built and scored |
| Custom testing scripts (your harness) | The specific checks — prompt injection, RAG poison, tool poison, multilingual |
| Monitoring solutions | Logs + canary + alert — what catches drift after the engagement |
| Benchmark datasets (LARA, OWASP-based) | The reference ruler — public, versioned, rerunnable |
| Reporting tools (`inspect view`, your template) | The honest report — number, method, seed, limitation |

@h3 Inspect in depth
- **Tasks:** `Task(dataset=[...], solver=[...], scorer=...)` — the eval.
- **Solvers:** `system_message`, `prompt_template`, `generate`, `chain_of_thought`, `multiple_choice`, `react`, `use_tools`. Solvers compose: `[system_message(...), generate()]` or `[react(), use_tools(...)]` with `sandbox="docker"` for agent tasks.
- **Scorers:** `match`, `includes`, `pattern`, `exact`, `f1`, `model_graded_qa`, `model_graded_fact`. For compliance, `model_graded_fact` against the verbatim text + a majority reducer for a board.
- **Model roles:** `model_roles` lets the grader be a different model from the target.
- **Sandboxes:** `sandbox="docker"` isolates tool-using agents — no host secrets leak.
- **Reading the log:** `inspect view` — click a sample, read transcript, judge reasoning, accuracy. `inspect log` for list/query/convert.

:::defbox
**Inspect primitive — `Sample`:** One input + target. The target is the judge's criterion (e.g., "The model REFUSES to... and explains Art. 5(1)(f)..."). Get this right and the eval is half done.
:::

@h3 Wiring it
Your harness (custom) → breaklab (lab logging) → five-test repo (boring failures) → Inspect (ruler) → report (template from Back Matter). One env fingerprint logged at the start; one accuracy printed at the end. The check is the product.

@h2 Worked Examples
@tier P
:::example
**Example 7.1 — Wiring Ollama + Inspect + your harness (local-only, no API keys).**
**Setup:** Laptop, Ollama, Inspect. No provider account.
**Run:**
```
pip install inspect-ai openai
ollama pull llama3.1
inspect eval lara_lite.py --model ollama/llama3.1 --epochs 5
inspect view
```
**Log:** 5 transcripts, judge verdicts, accuracy 2/5 (40%). Cost: $0. Fingerprint: `ollama/llama3.1 local, t=0, seed 0..4, n=5`.
**Value:** Free practice runs that are real evals — same shape as the take-home, different model.
:::
:::example
**Example 7.2 — Reading an Inspect log to find the exact turn where a tool call went wrong.**
**Setup:** An agent eval with `react()` + `use_tools()` fails — the agent sent email to an external address.
**Log trace:**
1. Sample input: poisoned doc (tool description with CC).
2. Turn 2: agent planner says "I will use email tool."
3. Turn 3: tool call `email_send(to="external@...")` — flagged.
4. Scorer: FAIL — tool call violated allowlist.
**Lesson:** The log tells you which turn, which tool, which arg. Fix the allowlist, rerun, log shows 0/10. Without the log you have a score; with it you have a trace.
:::

@h2 Hands-On Lab 7 — Tooling Stack a Stranger Can Clone and Run in One Session
:::lab
**Target:** Your own repo — the one you will link from your portfolio (Ch. 9).
**Steps:**
1. Repo structure: `README.md` (one-liner clone + run), `lara_lite.py` or your eval, `requirements.txt` (`inspect-ai`, `openai`), `logs/`, `docs/REPORT_TEMPLATE.md` (from Back Matter).
2. README must contain exactly: `pip install -r requirements.txt`, `ollama pull llama3.1` (or API model env), `inspect eval <file> --model ... --epochs 5`, `inspect view`. Pin versions (`inspect-ai==0.3.x`).
3. Log the env fingerprint at repo root: `fingerprint.txt` with model, serving, temp, prompt SHA, seed, date, n.
4. Ask a second person (or a second machine) to clone and run without asking you anything. Record where they got stuck — that is your missing check.
5. Publish (GitHub) with the honest number + limitation in the README.
**Deliverable:** A GitHub repo URL a stranger can clone and run in one session, with a passing run log.
**How you know you passed:** The second person sends you the log with your number (or the transcript where you were wrong) without asking you a question.
:::

@h2 Pitfalls and the Missing Check
:::pitfall
**What goes wrong:** "Run this" without versions — `inspect-ai` moved, Ollama model tag drifted, Python 3.12 breaks the harness. A sandbox that is not a sandbox — the agent tool can reach the host filesystem or network. No log viewer — no one can audit your run.
**The missing check:** Pinned versions (`requirements.txt` with hashes), `sandbox="docker"` for agent tasks, `inspect view` as the audit surface, and a second-person clone test. If a stranger cannot clone and reproduce without asking you, you do not have a product.
:::

@h2 Illustrations
@fig fig7-1.png The tooling stack — harness + breaklab + five-test repo + Inspect, wired into one stack. Output = report + log a stranger can rerun.

@h2 Key Terms
:::terms
**Inspect** — UK AISI eval harness; Task + Solver + Scorer + Log.
**Task / Solver / Scorer** — The eval, how the model is run, how it is graded.
**Sandbox** — Isolated execution (docker) for agent tool calls.
**Benchmark dataset** — A public, versioned ruler (e.g., LARA's 10 scenarios).
**Log viewer** — `inspect view` — where you audit every sample.
**Pinned stack** — Versions locked so a clone in 6 months still reproduces.
:::

@h2 Self-Test
:::selftest
**Recall:** Name the four pieces of the stack and what each contributes.
**Recall:** What does `model_graded_fact` with `reducer="majority"` do, and when do you need it?
**Application:** A teammate says "my eval passes locally but fails on CI." What three fingerprint fields do you compare first?
**Application:** Your `README` says "run my eval." A stranger cannot. What is the most likely missing check?
**Design a check:** Design the README for a repo a stranger can clone and run in one session. What five lines must it contain?
:::
@readywhen Someone else runs your repo and reproduces your finding without asking you how — pinned versions, sandboxed agent, log viewer ready.

@h2 Expert Extension
@tier R
**Open problem: when a custom scorer is needed.** `model_graded_fact` is enough for compliance (verbatim law). For nuanced behaviors (eval-awareness, ethical resistance, sycophancy), you need a scorer that captures variables beyond PASS/FAIL.
**Method you would bring:** Build a minimal custom Inspect scorer: subclass `Scorer`, add two graded variables (e.g., `eval_aware_score`, `ethical_resistance`), validate against 30 human-graded transcripts, report per-variable agreement. The scorer — not the score — is the contribution.

@sig I build the check, not the claim. The stack that a stranger can clone without asking you how is the stack you can defend under a deadline.
