# PROJECT CATALOG — one listing, 3 built-in pricing tiers (SEO-checked against Upwork's own docs)
The catalog is the client ladder from `STRATEGY/2026-10-02_90-day-10k-client-positioning.md` productized for search. Same three-tier logic, Upwork-priced to win the first reviews before raising toward the LinkedIn-side $1.5k-$3.5k engagement pricing.

## HOW THIS ACTUALLY WORKS ON UPWORK (confirmed live, 2026-10-11)
Upwork's Project Catalog does not create three separate listings for a three-tier ladder. One project supports **1 or 3 pricing tiers (Starter / Standard / Advanced) inside a single listing**, each with its own custom title (30 chars), custom description (80 chars), delivery days, and its own price per buyer company size (Small / Medium / Large). There's also an optional add-ons section. This is the structure to use, it gives one SEO'd title and URL instead of splitting search juice across three listings, and it puts the upsell path (Starter to Advanced) in front of every buyer automatically.

### Overview step (one listing covering all three tiers)
**Catalog title (exact, 59/75 chars incl. "You will get…"):**
```
You will get an AI red team test and prompt injection audit
```
**Category:** Development & IT > Cybersecurity & Data Protection > Other Cybersecurity & Data Protection (confirmed live suggestion; check "Not seeing the right fit?" for "Assessments & Penetration Testing" first, use it instead if it appears)
**Search tags (5, lowercase, same pattern confirmed working live):** ai security, prompt injection, red teaming, penetration testing, llm security
**Project attributes:**
- Cybersecurity Expertise (up to 3): Risk Assessment, Audit, AI Governance
- Technology Type (pick a few, not all 13): Web Application, SaaS, Database
- Cybersecurity Regulation (up to 5): GDPR, SOC 2, NIST Cybersecurity Framework, HIPAA, PCI DSS (use all 5 since the Advanced tier serves regulated buyers too)

**If you already completed the Overview step with the narrower "15-point AI prompt injection scan" title:** go back and change it now, before you publish. The project URL locks to whatever title is live the first time you hit publish, not the first time you save a step, so editing it now costs nothing.

### Pricing step — 3 tiers, priced by company size
Upwork lets you set a different price per tier per buyer company size. Use this table (base prices from the original single-price plan, scaled up for Medium/Large since bigger companies carry more budget and more risk exposure):

| Tier | Custom title (≤30 chars) | Custom description (≤80 chars) | Delivery days | Small co. | Medium co. | Large co. |
|---|---|---|---|---|---|---|
| Starter | `AI Quick Scan` | `15 injection attempts plus a one-page findings report in 3 days` | 3 | $150 | $200 | $300 |
| Standard | `AI Red Team Review` | `20+ vector red team test, findings report, and a live debrief call` | 7 | $600 | $800 | $1,200 |
| Advanced | `Pre-Launch Hardening` | `Full red team test, code fixes, a regression suite, 2 weeks of support` | 14 | $1,500 | $2,000 | $3,000 |

**Add-ons (optional, shown under all three tiers):**
- Rush delivery (cuts the stated timeline roughly in half): +$75
- Extra live debrief/walkthrough call (30 minutes): +$75
- Executive summary written for non-technical leadership/stakeholders: +$100

### Gallery step
Upwork's own gallery guidelines explicitly list "text-heavy images" as something to avoid, so don't rely on marketing-style covers alone. Use this mix:

**Project Images** (brand covers, now with tier-specific background concepts instead of a generic office photo):
- `gallery/catalog_tier1_quickscan.png` (Starter) — background is a cyan radar scan sweeping an abstract chat interface, flagging a couple of hits
- `gallery/catalog_tier2_redteamreview.png` (Standard) — background is 4 stacked translucent layers being probed by red attack-lines converging on a central AI chip
- `gallery/catalog_tier3_prelaunch.png` (Advanced) — background is a circuit-pattern padlock closing over a shield with a checkmark

**Sample Documents** (new Upwork feature, clients see the first 3 pages, use this for the least "marketing," most "real work" proof in the whole gallery):
- `gallery/sample_findings_report.pdf` — a clean 3-page PDF version of the real findings report (system prompt leak, fake refund trigger word, content-policy bypass), branded header/footer, ends with the 3-tier summary and the confidentiality line. This is the strongest trust-building asset in the gallery because it's an actual work sample, not a graphic.

**Project video:** skipped. No AI-generated video was produced for this (stock-style AI video reads as generic and is a weaker trust signal than real footage). If you want one later, the strongest option is a real 45-60 second screen recording: your terminal running a couple of the actual test prompts, the bot's broken response, the fix landing, then the regression suite passing green, closing on the one-page report. I can write a voiceover script and generate narration audio for you to lay under your own screen capture whenever you're ready to record it.

### Process step
1. You tell me which tier fits, then share access (staging link preferred) plus anything explicitly off-limits to test.
2. I run the testing scoped to your tier: 15 attempts (Starter), the full 4-layer/20+ vector test (Standard), or the full test plus code-level fixes (Advanced).
3. You get the findings report in the four-part format: exact repro, which layer failed, the fix, how it was verified.
4. Standard and Advanced buyers get a live debrief call; Advanced buyers also get 2 weeks of async support and a final verification pass.

### Description step (shared across all three tiers, tier differences live in the pricing table above)
```
I red team AI features, chatbots, RAG systems, and tool-calling agents, before your users find the holes. Pick the depth that fits where you are: a fast scan to know if there's an obvious problem, a full structured review across all four layers that break shipped AI (prompt injection, RAG poisoning, agent/tool-call abuse, policy bypass), or the complete loop with code-level fixes and a regression suite that keeps a closed hole from quietly reopening.

Every tier uses the same four-part findings format: exact repro, which layer failed, the fix, how it was verified. Your findings never leave our workspace. Nothing about your system, prompts, or results is shared, published, or reused without your written permission.
```

### Review step
Confirm title, category, attributes, all three tiers' pricing/delivery/custom copy, gallery images, and the shared description match the above before publishing. Double-check the title one more time here, it's the last checkpoint before the URL locks in.

### FAQ (applies across tiers, use in whichever step asks for it)
- **What if you don't find anything?** You still get the full report documenting every attempt and its outcome, proof of due diligence either way.
- **Will testing affect my live system or users?** No code changes happen in Starter or Standard. I only send test inputs and record results. Code changes only happen in Advanced, scoped with your team first.
- **Can I start at Standard or Advanced without buying Starter first?** Yes, every tier stands on its own. Starter is just the cheapest way to test the waters first.
- **Is this suitable for regulated industries like health or finance?** Yes, especially Advanced. Flag any specific compliance requirements (HIPAA, SOC 2, etc.) during scoping so testing and fixes account for them.
- **What do you need from me to start?** Access to the feature (staging preferred), any off-limits topics/actions, and confirmation you have authority to request testing (your own product, or your employer/client's permission).

## WHY THIS LADDER WORKS
- Starter is priced low enough to be an impulse "yes" for a buyer who just wants to know if there's a problem, the review-generation engine for weeks 1-3.
- Standard is the real service, same shape as the LinkedIn-side $3.5k starter engagement, priced for Upwork's colder/price-sensitive search traffic.
- Advanced upsells the buyers who want the full loop, without ever discounting Standard to get there.
- Company-size pricing captures more from larger buyers without changing the scope language, same deliverable, different price point based on who's asking.

## AFTER 5 REVIEWS
Raise Starter to $200-300 across sizes, Standard to $800-1,200, Advanced to $2,000-3,500+, and stop leading with Starter in proposals, lead with Standard.

---

## APPENDIX — original 3-separate-listing drafts (kept for reference, not the recommended structure)
Everything below was drafted before confirming Upwork's real 3-tier-in-one-listing mechanic above. The content (descriptions, FAQs, requirements, process steps) is still accurate and was reused in the single-listing version above; keep this section only if you ever want to split these into standalone listings later (for example, once Starter alone has enough reviews to stand on its own).

## CATALOG SEO NOTES (confirmed via support.upwork.com and upwork.com/resources — read before publishing)

- **Title field is 75 characters max, and Upwork auto-prepends "You will get…" to every title — that prefix counts toward the 75.** The titles below already include the prefix and are measured against the real limit.
- **Don't write the title as an instruction ("You will get a scan")** — Upwork's own guidance says say what you offer in a few words, don't repeat "You will get," use normal capitalization, and push extra keywords into search tags instead of cramming the title.
- **The project URL is generated from the FIRST title you publish and does not change even if you edit the title later.** Get each title close to final before you hit publish the first time — this is a one-shot SEO decision per listing, unlike the profile title which you can freely A/B test.
- **Search tags: up to 5 per listing, pulled from Upwork's standardized/autocompleted tag list** (same mechanic as profile skills). These are a separate discoverability lever from the title — use them for keywords that didn't fit in the 75 characters.
- **Category: choose the single closest match** (Upwork suggests categories based on your title as you type) — avoid "Other." This determines which category browse-pages and category-filtered searches the listing appears in.
- **Boosting (paid placement) exists but isn't worth using yet.** Boosting only pays off once JSS, Top Rated status, and 5+ recent reviews are in place — per `content_strategy.txt` Part 2, that's after the first 3-5 jobs, not at launch.

---

## TIER 1 — AI QUICK SCAN
**Catalog title (exact, 69/75 chars incl. "You will get…"):**
```
You will get a 15-point AI prompt injection scan with findings report
```
**Category:** AI Services (or closest Upwork-suggested match — likely nested under Cybersecurity & Data Protection)
**Search tags (5):** AI Security, Prompt Injection, Chatbot, Security Testing, LLM
**Listing nickname (internal use only):** AI Quick Scan
**Price:** $150
**Timeline:** 3 days
**Hook line:** Know if your bot is soft before you spend on a full audit.

**Description:**
```
I run 15 targeted prompt injection and jailbreak attempts against your live chatbot, agent, or RAG feature and send back a one-page findings summary: what broke, how, and the fastest fix for each. This is the low-risk way to find out if your AI feature has an obvious hole before you commit to a full engagement.

What you get:
- 15 manual + automated injection attempts (garak/promptfoo coverage) against your feature
- One-page findings summary: issue, severity, exact repro input, recommended fix
- Delivered as a PDF within 3 days of access/credentials being provided
- One round of clarifying questions by message, no live call required

Your findings never leave our workspace. Nothing about your system, prompts, or results is shared, published, or reused without your written permission.
```

**Cover image (1584x990):** `gallery/catalog_tier1_quickscan.png`

**Project attributes (confirmed live on Upwork under Dev & IT > Cybersecurity & Data Protection > Other Cybersecurity & Data Protection):**
- Cybersecurity Expertise (pick up to 3): Risk Assessment, Audit, AI Governance
- Technology Type (pick a few, not all 13): Web Application, SaaS, Database
- Cybersecurity Regulation (pick up to 5): GDPR, SOC 2, NIST Cybersecurity Framework
- Search tags (5, confirmed working on live Upwork autocomplete): ai security, prompt injection testing, penetration testing, llm agent development, chatbot development

**Process step (buyer-facing steps):**
1. You share access, a staging link preferred, or a production link plus anything explicitly off-limits to test.
2. I run the scan: 15 targeted prompt injection and jailbreak attempts against your feature, each one logged exactly as run.
3. You get the report: a one-page PDF within 3 days listing what broke, how, and the fastest fix for each issue found.
4. Optional next step: if something serious turns up, the $150 rolls straight into a same-week upgrade to the AI Red Team Review.

**What I need from you to start:**
- A working link to the chatbot, agent, or AI feature to be tested. A staging/test environment is preferred over production; if only production is available, say so and I'll scope the attempts to avoid any destructive action.
- Any topics, actions, or inputs that are explicitly off-limits for testing (so nothing gets tested that could cause real harm or a real transaction).
- Confirmation that you have the authority to request this test, either it's your own product, or you have your employer/client's permission to have it tested.

**FAQ:**
- **What if you don't find anything?** You still get the full one-page report listing all 15 attempts and their outcomes, so you have documented proof the feature was checked, not just a blank result.
- **Will testing affect my live system or users?** No code changes are made in this tier. I only send test inputs and record what comes back, nothing is fixed or altered.
- **Do you need my source code?** No. This tier only needs access to the running feature itself (a chat widget, an API endpoint, or a login to a staging build).
- **What happens if you find something serious?** You get the finding immediately, you don't have to wait for the full report if something looks urgent, and I'll tell you plainly if it's bad enough to escalate straight to the Tier 2 review.
- **Can this turn into the bigger review later?** Yes. If the scan turns up something worth digging into, the $150 counts toward a same-week upgrade to the AI Red Team Review.

---

## TIER 2 — AI RED TEAM REVIEW
**Catalog title (exact, 72/75 chars incl. "You will get…"):**
```
You will get an AI red team test: prompt injection, RAG, and agent abuse
```
**Category:** AI Services (or closest Upwork-suggested match)
**Search tags (5):** AI Security, Prompt Injection, RAG, AI Agents, Penetration Testing
**Listing nickname (internal use only):** AI Red Team Review
**Price:** $600
**Timeline:** 1 week
**Hook line:** The full test most teams skip until something breaks in production.

**Description:**
```
A structured red team pass across the four layers that actually break shipped AI features: prompt-level injection, RAG/retrieval poisoning, agent and tool-call abuse, and policy/output bypass. You get a prioritized findings report your engineers can act on the same day, plus a debrief call to walk through what matters most.

What you get:
- 20+ attack vectors across prompt injection, RAG poisoning, tool-call/agent abuse, and policy bypass
- Manual testing plus automated scanning (garak, promptfoo, or equivalent for your stack)
- Findings report in four-part format: exact repro, which layer failed, the practical fix, how to verify the fix holds
- Severity ranking (Critical/High/Medium/Low) so your team fixes the right thing first
- 30-minute debrief call to walk through findings and answer questions

Your findings never leave our workspace. Nothing about your system, prompts, or results is shared, published, or reused without your written permission.
```

**Cover image (1584x990):** `gallery/catalog_tier2_redteamreview.png`

**Project attributes (same category as Tier 1: Dev & IT > Cybersecurity & Data Protection > Other Cybersecurity & Data Protection):**
- Cybersecurity Expertise (pick up to 3): Risk Assessment, Audit, AI Governance
- Technology Type (pick a few, not all 13): Web Application, SaaS, Database
- Cybersecurity Regulation (pick up to 5): GDPR, SOC 2, NIST Cybersecurity Framework
- Search tags (5, try these lowercase, confirm each autocompletes before publishing): ai security, prompt injection, rag security testing, ai agent security, penetration testing

**Process step (buyer-facing steps):**
1. You share access plus a short description of your architecture (plain prompt-based, RAG, or agent/tool-calling) and anything off-limits to test.
2. I run the full 4-layer test: prompt injection, RAG/retrieval poisoning, agent/tool-call abuse, and policy/output bypass, 20+ vectors total.
3. You get the findings report: exact repro, which layer failed, the fix, how it was verified, with a severity rank on each issue.
4. We get on a 30-minute debrief call to walk through what matters most and answer your team's questions live.

**What I need from you to start:**
- A working link or access credentials to the chatbot, agent, or AI feature to be tested (staging/test environment preferred).
- A short description of how the system is built: plain prompt-based chatbot, RAG/retrieval-based, or agent/tool-calling, so the right 20+ vectors are selected for your actual architecture.
- Any topics, actions, or inputs that are explicitly off-limits for testing.
- Confirmation of your authority to request this test, and one point of contact available for the 30-minute debrief call.

**FAQ:**
- **How is this different from the Quick Scan?** The Quick Scan checks 15 common prompt-injection patterns. This tier covers all four layers a shipped AI feature can fail at: prompt injection, RAG/retrieval poisoning, agent/tool-call abuse, and policy/output bypass, roughly 20+ distinct vectors, plus a live debrief call.
- **Do I need to already have had a Quick Scan done?** No, this tier stands on its own. The Quick Scan is just a cheaper, narrower starting point if you want to test the waters first.
- **What does the debrief call cover?** We walk through the findings report together, I explain which issues to fix first and why, and answer any questions your engineers have in real time.
- **Will you tell me how to fix the issues, or just what's broken?** Each finding includes a recommended fix, written in enough detail for your team to act on it the same day. Implementing the fix is covered under Tier 3, not this tier.
- **What if my system changes mid-engagement?** Let me know as early as possible. Minor changes can usually be absorbed into the existing scope; a significant rebuild may need a short scope adjustment.

---

## TIER 3 — PRE-LAUNCH HARDENING
**Catalog title (exact, 74/75 chars incl. "You will get…"):**
```
You will get full AI red team testing with code fixes and regression suite
```
**Category:** AI Services (or closest Upwork-suggested match)
**Search tags (5):** AI Security, Red Teaming, Regression Testing, LLM, Risk Assessment
**Listing nickname (internal use only):** Pre-Launch Hardening
**Price:** $1,500
**Timeline:** 2 weeks
**Hook line:** Ship once, stay fixed. The full loop, not just a one-time test.

**Description:**
```
The complete pre-launch loop: full red team testing, code-level fixes scoped with your team (not just a PDF of problems), and a regression suite that runs on every future model or prompt change so a closed hole cannot quietly reopen. Built for teams launching AI into production, especially in health, finance, or other regulated workflows where a repeat incident is not an option.

What you get:
- Everything in the AI Red Team Review (4-layer testing, prioritized findings report, debrief call)
- Code-level gate recommendations scoped to your stack: input validation, output filtering, tool-call confirmation steps, rate/cost limits
- A regression test suite (automated) your team owns and runs on every future deploy or model swap
- 2 weeks of async Slack/email support during your fix sprint
- Final verification pass confirming each fix holds against the original repro

Your findings never leave our workspace. Nothing about your system, prompts, or results is shared, published, or reused without your written permission.
```

**Cover image (1584x990):** `gallery/catalog_tier3_prelaunch.png`

**Project attributes (same category as Tier 1 & 2: Dev & IT > Cybersecurity & Data Protection > Other Cybersecurity & Data Protection):**
- Cybersecurity Expertise (pick up to 3): Risk Assessment, Audit, AI Governance
- Technology Type (pick a few, not all 13): Web Application, SaaS, Database
- Cybersecurity Regulation (pick up to 5, use all 5 here since this tier targets regulated industries): HIPAA, PCI DSS, GDPR, SOC 2, NIST Cybersecurity Framework
- Search tags (5, try these lowercase, confirm each autocompletes before publishing): ai security, red teaming, regression testing, llm security, penetration testing

**Process step (buyer-facing steps):**
1. You share everything from the Red Team Review (access, architecture summary, restrictions, point of contact) plus repo/codebase access or a technical contact on your side.
2. I run the full 4-layer test and scope code-level fixes with your team: input validation, output filtering, tool-call confirmation steps, rate/cost limits.
3. I build the regression suite: an automated test that reruns every original attack plus reworded variants on every future deploy or model swap.
4. You get 2 weeks of async support while your team ships the fixes, then a final verification pass confirming each fix holds.

**What I need from you to start:**
- Everything listed under the AI Red Team Review (access/credentials, architecture summary, testing restrictions, a point of contact).
- Repository or codebase access, or a technical contact on your side who can implement the scoped fixes alongside me.
- CI/CD pipeline details if you want the regression suite wired directly into your existing deploy process; otherwise it's delivered as a standalone runnable suite.
- Team availability for the 2-week async support window (a shared Slack channel or email thread works).

**FAQ:**
- **Do you write the fixes yourself, or just tell me what to change?** Both are possible. The code-level gates are scoped with your team first, then I can implement them directly if you want hands-on work, or hand off clear specs if your team prefers to build them in-house.
- **What exactly is in the regression suite?** An automated test suite that re-runs every original attack (plus reworded variants) against your system on every future deploy or model swap, so a fix that worked today can't silently break six weeks from now without someone noticing.
- **What happens after the 2 weeks of support end?** You own the regression suite outright and can keep running it indefinitely. If you want ongoing retesting after a major model or feature change, that's a separate follow-up engagement.
- **Can I start here without doing Tier 1 or Tier 2 first?** Yes. Tier 3 includes the full Tier 2 testing scope, you don't need to buy the smaller tiers first.
- **Is this suitable for regulated industries like health or finance?** Yes, this tier is built specifically for teams where a repeat incident isn't an option. Tell me about any specific compliance requirements (HIPAA, SOC 2, etc.) during scoping so testing and fixes account for them.

---

## WHY THIS LADDER WORKS
- Tier 1 is priced low enough to be an impulse "yes" for a buyer who just wants to know if there's a problem — this is the review-generation engine for weeks 1-3.
- Tier 2 is the real service, same shape as the LinkedIn-side $3.5k starter engagement, priced for Upwork's colder/price-sensitive search traffic.
- Tier 3 upsells the ~20% of Tier 1/2 buyers who want the full loop, without ever discounting Tier 2 to get there.
- All three reuse the same four-part findings format and confidentiality line, so the brand reads consistent whether a buyer sees $150 or $1,500.

## AFTER 5 REVIEWS
Raise Tier 1 to $200-250, Tier 2 to $800-1,000, Tier 3 to $2,000+, and stop selling Tier 1 as the default entry point in proposals — lead with Tier 2.
