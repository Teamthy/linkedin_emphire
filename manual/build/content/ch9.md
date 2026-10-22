@chapter 9 Professional Development, Positioning and Standing Out

:::atglance
**Question:** What makes the resume optional — and how does a portfolio of checks do it?
**Deliverable:** A personal red-team + research portfolio, ready to put in front of a hiring team: harness + write-ups + one published finding.
**Time:** 3 hrs (60 min read + 2 hrs Lab 9).
:::

@h2 Learning Objectives
:::objectives
Name where community, practical experience, and certifications add signal — and where the portfolio matters more.
Describe the portfolio that stands you out: harness + write-ups + one published finding — and the roles it opens.
Explain the standout edges (the check, the denominator, the honest number, the canary, the two-sided boundary, the published method) as signature, not just skills.
Plan a public record (series, posts, open-source harness) that compounds into the next engagement.
:::

@h2 The Idea: Community, Practice, Credentials — But the Portfolio Is What Gets You Hired
@tier F
You can get a certificate. Many do. You can do a CTF. Many do. What most do not have is a portfolio where a hiring manager can click once and reproduce a finding. That is the scarce one. That is the edge.
- **Community:** Conferences, research groups, forums — go where the people who write the checks (or the papers) are. Do not just attend. Publish the check.
- **Practical experience:** Lab environments, CTF challenges, red-team simulations — use them to generate artifacts (harness + trace + rate), not just points on a scoreboard.
- **Certifications:** Specialized courses and credentials — they signal breadth. The portfolio signals you can do the job tomorrow.
- **Positioning:** The portfolio is harness (runnable) + write-ups (honest numbers) + one published finding (a method a skeptic reran). The roles it opens: evals researcher, AI security engineer, red teamer. One portfolio, three paths.

:::defbox
**Portfolio (here):** Harness (repo, runnable) + write-ups (2 articles, honest numbers) + one published finding (eval + log). That is the unit. The resume becomes optional.
:::

@h3 The standout edges — the thing that is you
These are not skills. They are signatures — the moves a reader recognizes as you.
| Edge | What it means |
|---|---|
| The check is the product | You ship the rerunnable check, not the claim |
| The number with a denominator | Every rate carries n |
| The honest number | You name the limitation that hurts your story |
| The reproducible canary | Your checks catch drift on a schedule |
| The two-sided boundary | You test both over- and under-escalation |
| The published method | A skeptic can rerun, not just trust |

Everything else is a skill. These are the signature.

@h2 The Mechanics: How the Portfolio Compounds
@tier P
@h3 Community engagement
- **Conferences:** Submit the check, not the deck. "We made the Art. 5(1)(f) check rerunnable; here's the repo and the before/after." That talk gets cited.
- **Research groups:** Join one, bring the harness. The group that has the ruler is the group that sets the question.
- **Forums:** Answer with numbers. "I ran this in 2/5 at t=0, n=5 — here's the transcript where the judge disagreed." That answer is trusted.

@h3 Practical experience
Labs and CTFs are generators, not just practice. Every challenge you finish, publish the check (sanitized). One CTF write-up with a rerunnable harness is worth more than ten certificates.

@h3 Certifications vs portfolio
A certificate says "I passed a test someone else wrote." A portfolio says "I wrote the test someone else can now pass." Get the certificate if it opens a door. Build the portfolio so you own the room after.

@h3 Positioning — the three roles one portfolio opens
| Role | What they hire for — and what your portfolio shows |
|---|---|
| Evals researcher | Published eval + honest report + judge calibration — you make the ruler |
| AI security engineer | Attack-surface map + canary + gated fix — you make production safe |
| Red teamer | Full engagement (target → published method) — you find it and make it defensible |

@h2 Worked Examples
@tier P
:::example
**Example 9.1 — A portfolio that got a screen.**
**Who:** A Research Engineer candidate (engineer, not formal ML researcher).
**What it contained:**
1. Harness repo: `Teamthy/ai-redteam-five-tests` fork with 5 checks + LARA-lite eval, pinned versions, one-liner run, logs.
2. Two write-ups: "The Five Boring Failure Modes" + "We Made the Art. 5 Check Rerunnable" — each with honest numbers + limitations.
3. One published finding: LARA-lite on 2 models, 3 scenarios, n=20, 40% → 85% after fix, honest report with canary.
**The email that followed:** "We read your harness. We reran your eval. Walk us through your disagreement with your own judge." That is the screen. The portfolio made it happen — not the resume. Break before users do.
:::
:::example
**Example 9.2 — A post that compounds.**
**Step 1:** Publish one honest eval write-up (2/5, t=0, n=5, limitation stated).
**Step 2:** A reader reproduces it, comments "I got 3/5 with t=0.5," and shares their fingerprint. You update the post with their number.
**Step 3:** A meetup organizer invites you to talk about "how to make compliance checks rerunnable." You bring the harness.
**Step 4:** A vendor invites you to red-team their staging assistant — using your check. That is the next engagement.
**Lesson:** One honest post compounds into talks into engagements. The clean post does not — it has nothing to compound.
:::

@h2 Hands-On Lab 9 — Ship Your Portfolio
:::lab
**Target:** A public portfolio page (GitHub README, personal site, or LinkedIn post — one place a hiring team can find all three).
**Steps:**
1. Repo: harness + eval + pinned versions + one-liner run + log + honest report (Ch. 7 Lab + Ch. 8 Lab artifacts). Public.
2. Two write-ups: (a) the five boring failure modes as you saw them (one paragraph each with a check), (b) your LARA-lite honest report — what broke, how often, which judge, what it means (sanitized, no PII).
3. One published finding: the full engagement (Ch. 8) in its own repo or tagged release, with before/after numbers, fingerprints, limitation, and "how to rerun."
4. Ask one second person to clone and reproduce. Fix where they got stuck. Link all three from one page.
5. Write your positioning paragraph: "I build the check, not the claim. My work is the number with a denominator — the honest number — and the canary that keeps it honest." Keep it short. No buzzwords.
**Deliverable:** A single page (URL) with harness repo + 2 write-ups + 1 published finding, each with rerun instructions.
**How you know you passed:** A hiring manager can, in 10 minutes, run your eval and read your two write-ups and know you are the person who makes the fix reproducible. That is the bar: the portfolio makes the resume optional.
:::

@h2 Pitfalls and the Missing Check
:::pitfall
**What goes wrong:** A portfolio of claims without checks — "I found bias" with no ruler. Hiding limitations — the reader notices and stops trusting you. Optimizing for certificates over checks — you can pass a test but cannot write one.
**The missing check:** Every portfolio item has a rerunnable check. Every number carries a denominator. Every report names its limitation. Without those, the portfolio is a claim. With them, it is proof a stranger already verified.
:::

@h2 Illustrations
@fig fig9-1.png The portfolio that stands you out — harness + write-ups + one published finding. Three pillars, one banner: the check is the product that gets you hired.

@h2 Key Terms
:::terms
**Portfolio (here)** — Harness + write-ups + published finding — the hireable unit.
**Public record** — Series, posts, open-source harness that compounds over time.
**Signal** — What a credential or portfolio tells a hiring team — portfolio signal is rerunnable proof.
**Positioning** — Choosing which role (evals, security, red team) your portfolio points at — one portfolio can point at all three.
**Signature** — The moves a reader recognizes as you (denominator, honest number, canary, two-sided boundary).
:::

@h2 Self-Test
:::selftest
**Recall:** What three things make the portfolio that stands you out? Why does each matter?
**Recall:** Name two standout edges and what "the honest number" requires you to do that the clean number does not.
**Application:** A certificate says "I passed a test." Your portfolio says "I wrote the test." Give one concrete portfolio item that proves the second claim.
**Application:** You have one honest eval write-up. Map how it compounds into the next engagement in three steps.
**Design a check:** Design a 10-minute test a hiring manager can run during a screen to verify your portfolio claim. What do they clone, run, and see?
:::
@readywhen The portfolio makes the resume optional — harness + write-ups + one published finding, each rerunnable by a stranger in one session.

@h2 Expert Extension
@tier R
**Open problem: the portfolio as research program.** A single finding hires you once. A program hires you forever.
**Method you would bring:** Name three open problems you will publish on next (e.g., multilingual compliance gap, judge calibration, memory poisoning) and, for each, the first check you will ship — dataset, judge, n, limitation. Ship the first one. The program is the portfolio that keeps standing you out after you are hired.

@sig I build the check, not the claim. I would not report a number I could not reproduce. The honest number, not the clean one — that is the signature that compounds.
