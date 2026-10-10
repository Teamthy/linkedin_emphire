# Target: Sajida Abid Malik / Nexus Automation Agency
Date: 2026-10-03
LinkedIn: https://www.linkedin.com/in/sajida-abid-malik/
Source: hiring post in "STARTUP SPECIALISTS NETWORK GROUP" (Oct 3) — "Software & Tech Developers" + BDE, fully remote, "slide into my DMs"

## DUE DILIGENCE (done Oct 3)
- GitHub org exists: github.com/Nexus-Automation-Agency ("Nexus-Accelerator-Showcase")
- Repo is a README only. No code, no releases, marketing language ("high-velocity automation engine").
- Contact: gmail address. No website found. No company LinkedIn page found in search.
- Verdict: unverified early-stage or aspirational agency. Not proven scam, but zero evidence of real enterprise clients or paying work yet.

## SEND RULES (before investing any time)
1. Ask pay range + payment method in the first exchange. No answer = walk.
2. Any request to pay for training, tools, or onboarding = walk immediately. Classic pattern.
3. Unpaid "test task" longer than 2 hours = walk. A short bounded task is fine.

## PATH (updated Oct 3 — DM was blocked)
DM blocked because not connected (3rd+) and free accounts have no InMail.
DO NOT buy Premium for this target.

Step 1: Send BLANK connection request (no note — her post invites connections, accept rate will be high, and it saves the monthly note quota).
Step 2: When accepted, send the DM below.
Step 3 (optional): comment on the hiring post for group visibility:

```
Software engineer here (AI integrations + red teaming, remote from Lagos). Sent a DM about the dev role. What's the stack for the AI work?
```
This is optional but the thread has other people hiring. A comment that names a specialty stands out against 200 "interested" replies.

Step 3 size caution: only post it if the DM went out. Don't comment about a DM that isn't sent.

## DM (send after she accepts)
```
Thanks for connecting, Sajida. Quick version: I'm a software engineer in Lagos. I build AI integrations (chatbots, RAG, tool-calling agents) and I red team them before launch. I write the Breaking AI series on LinkedIn and my code is on GitHub.

Two questions about the role: what's the current stack, and is the AI work internal or client-facing?

One thing worth saying: agencies that ship AI to enterprise clients almost never test what they shipped before the client finds the holes. That's the part I do. Happy to show you what that looks like.
```

## STATUS
- Connection request: PENDING (send blank, no note)
- DM: blocked until accepted
- Note quota: NOT spent on this target (deliberate)

---

## TIMELINE
- Oct 3: DM blocked (3rd+, no InMail on free). Blank connection request sent.
- Oct 3, 11:40 PM: Connected. DM sent (the "what's the stack" version).
- Oct 4, 2:24 PM: Sajida replied. Dodged the stack question ("no single tech stack"), said solutions are client-facing for global enterprise, asked a screening question about RAG red teaming + tool-calling loops.
- Oct 5, 8:01 AM: Reply drafted (below).

## SIGNAL READ (Oct 4 reply)
- She skipped naming any stack, any client, or any rate. Still no evidence of real enterprise work.
- The screening question is technically literate. Either a real agency or an AI-generated screen. Either way, answering well costs little and buys information.
- PAY STILL UNANSWERED. Per the rule: no rate = walk. The drafted reply asks directly.

## REPLY DRAFT (send Oct 5, plain text, no markdown asterisks)
Hi Sajida, thanks for the detail. Here is the structure I use.

1. Scope the system before testing it.
Map what the retriever can read, what each tool can do, and which credentials the agent inherits. An agent does not get its own permissions, it inherits the service account's, so that scope is the real attack surface. I write down the blast radius of every tool before I run a single test.

2. Test four layers.
- Retrieval: poisoned documents, indirect injection hidden inside PDFs or web pages, conflicting context, cross-tenant leakage
- Input: direct injection, obfuscated payloads, non-English inputs, oversized and malformed input
- Action: tool-call injection, unauthorized tool invocation, argument tampering, confirmation bypass
- Output: exfiltration through responses, policy drift, commitments the system has no authority to make

3. Runaway and tool-loop prevention, which is your specific question.
- Hard iteration budget, enforced outside the model. Never as a prompt instruction.
- Loop detection: hash the tool name plus arguments, flag repeated signatures and cycles in the call graph.
- Idempotency keys, per-tool timeouts, circuit breakers.
- Confirmation gates on anything irreversible. Dry-run mode for testing.
- Fail closed. Escalate to a human instead of retrying, and never let a retry loop reach a write path.

After testing I convert the findings into an eval suite, so every prompt or model change gets regression tested before release. Automated runs first, then a manual creative pass, because the attacks that actually work tend to be boring ones.

One process question before we go deeper: what contract arrangement and rate are you working with for this role? Remote is fine on my side, I just want expectations clear both ways.

Happy to walk through any of this on a short call.

## GUARDRAILS
- If she asks for a free "test assessment" on their system: cap at 2 hours, get scope in writing first, or decline.
- If she never answers the rate question: walk, politely.
- Do not accept any arrangement that requires payment from Timothy (training, tools, onboarding fee).

## CONTENT REUSE
- "An agent does not get its own permissions, it inherits the service account's." → card-worthy line, article 4/5 material
- Tool-call loop prevention (iteration budget, call-graph cycle detection, fail closed) → Article section, plus a standalone micro post candidate

---

## TIMELINE UPDATE — Oct 6, 2026 (evening)
- Oct 6: Sajida replied again. Called the security breakdown "solid." Then asked for a FREE PRACTICAL TASK as a "final evaluation step":
  1. Build a modular agent loop with hard iteration budget + circuit breaker / loop detection
  2. Record a 3-5 min Loom with voice + screen: architecture walkthrough, live demo of catching a recursive loop, plus how input validation, error boundaries, and security were handled
  3. Send repo link + Loom link
  4. "Once we review this and everything looks good, we can immediately discuss contract arrangements and rates"

## ASSESSMENT: crosses the guardrail. Do not complete the full free task.
Realistic effort: 4-8 hours (working system + live demo + rehearsed client-facing video). The stated cap in this file was 2 hours.
Six tells, stacked:
1. Rate still unstated after three exchanges, now deferred until AFTER the free deliverable
2. The build spec is exactly what Timothy already outlined in writing (iteration budget, loop detection by hashing tool name + args, circuit breaker, fail closed). The evaluation is "implement the spec you gave us for free."
3. The Loom is a client-facing explainer asset. Normally a paid deliverable.
4. Unverifiable company: gmail contact, README-only GitHub org, no website, versus "high-grade enterprise systems for global clients"
5. Bulk hiring post: no stack, no pay, DM funnel, two unrelated roles
6. Sequencing inverted: work first, money later. Professional standard is money first.

## PATTERN TO REMEMBER (applies to every future lead)
Legit paid trial: bounded, small, and the rate is already agreed. Or paid pilot.
Extraction pattern: unbounded custom build + client-facing video, rate deferred to "after we review."
Test question: "What rate and contract arrangement are we working with?" If that is answered with anything other than a number, stop.

## RESPONSE A: COUNTER-OFFER (send this)
Hi Sajida, glad the breakdown was useful. Before I put a few hours into the build and the walkthrough, one thing still needs settling: what rate and contract arrangement are we working with? You mentioned it earlier and it is still open, and it decides how I scope this.

Two ways to see me work, pick whichever suits you:

Option A, existing work. I have a red team test harness and a loop-protection pattern from systems I have already shipped. I will send the repo and walk you through that real code live in 5 minutes. No charge, and it shows you exactly how I build.

Option B, the custom build you described. Agent loop with a hard iteration budget, circuit breaker, loop detection, live demo, plus the explainer video. That is a real deliverable, and sending it free to everyone in the pipeline is not something I do. I will build it as a paid pilot: $400 fixed, delivered in 3 days, and it comes off my first invoice if we sign.

Either way I want the rate settled before I start. I take client work seriously and I would rather be aligned than assume.

Which one do you want?

## RESPONSE B: IF THEY REFUSE TO PAY
Send repo + 5-min Loom of EXISTING code only. Warm close: "Happy to stay in touch. If a paid engagement comes up, I am here." Then stop responding to unpaid asks. Keep the contact, drop the labor.

## RESPONSE C: HARD WALK (only if they get pushy or evasive about money)
"Understood. I only take on custom builds under contract. If that changes on your side, reach out. Wishing the agency well."

## SALVAGE PLAY (do this regardless)
The loop-detection + circuit-breaker system is strong content. Build it PUBLICLY as part of Breaking AI, on Timothy's own terms:
- Repo: agent loop with iteration budget, call-signature loop detection, circuit breaker, confirmation gates, fail closed
- Article: "I built an agent that would not stop. Here is how to kill it."
- Value: his asset, his demo, his article. Any client can see it forever. Converts this risk into Series content.
- Bonus: it doubles as the portfolio artifact for the micro1 pipeline and other AI roles.

## STATUS
- [ ] Send RESPONSE A
- [ ] Await rate answer
- [ ] If paid pilot offered: scope it, 3 days, 50% deposit
- [ ] Regardless: log the public build as an article candidate
