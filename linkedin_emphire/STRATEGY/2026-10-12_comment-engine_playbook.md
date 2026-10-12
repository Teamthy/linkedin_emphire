# Comment Engine: playbook, metrics, frame library

- Written 2026-10-12 from a full export of ~30 external comments over the prior 5 days plus their visible metrics.
- Purpose: make the pattern that earned two replies from Tanya Janca (and threads with St Louis, Cavello, Hassid, Rachitsky, Miller, Qureshi) repeatable, and raise the ceiling on it.

## 1. What the metrics say (from the 2026-10-12 export)

Top by impressions:
- 8,877: group job-application comment ($65/hr AI code review, Aforo Okraku post)
- 8,153: Ruben Hassid, 23-minute master class
- 4,790: Allie K. Miller, ultrafast AI meetings
- 2,779: Lenny Rachitsky, AI simulations trend
- 1,757: Iyinoluwa Aboyeji, Moove Nigeria exit
- 1,088: Satya Nadella, Microsoft-Decision-1
- 504: Jesse Zhang, PACT protocol
- 465: own group post (ML group, article 1)

Top by engagement:
- 13 reactions / 4,790 impressions: Allie Miller, the "work shifts from fetching to verifying" frame
- 8 reactions / 1,088: Nadella Decision-1, "the model is half the product"
- 7 reactions / 2,779: Lenny Rachitsky, "the confirmation trap wearing a new coat"
- 4 reactions / 76: Christian St Louis, planted-flaw eval critique

Reads:
- Impressions are set by the host account's size, not comment quality. Same quality, ~580x spread (8,153 vs 14). Optimize placement first, content second.
- Conversation rate: roughly 1 in 3 comments produced an OP reply or a second-degree reply. The converting ones end with a direct, answerable question to a named person or a low-friction offer. The non-converting ones end on a statement.
- Own posts underperform own comments (21 to 465 impressions vs comments on 100K+ accounts). The comment discipline is stronger than the post discipline; ports over directly.

## 2. The comment spec (what a good one looks like)

- 3 to 8 lines. No emojis, no hashtags, no link to own profile, no opening praise.
- Structure: acknowledge the OP's frame in one clause, then "one addition from the field" plus a mechanism, then close.
- Close, pick one:
  a) a direct, answerable question only the OP can answer about their own system, or
  b) a low-friction offer ("if a write-up would be useful, say the word"), or
  c) a one-line frame with nothing after it (use sparingly; converts less).
- Evidence rule: cite a primary source (a disclosure, a paper, a named incident) at least once in two comments. The Anthropic four-cases disclosure is the current workhorse.
- Place on the target list only (below). If a post is off-list, the comment is optional.

## 3. Target list (four tiers, comment within 2 hours of post for the big ones)

Named accounts for every tier come from the 2026-10-12 network snapshot: NETWORKING/network-asset-map.md (Tier A = 20 named AI-security accounts, Tier B rotation, Tier C Nigeria nodes, Tier D ambient, plus a follow-back shortlist).

1. AI security leaders: Tanya Janca and her orbit (OWASP, appsec, secure coding). Max 1 to 2 per week per person, substantive only.
2. Agentic-AI founders and launches: YC launches, product announcements in fintech, healthcare, government-adjacent. 2 to 3 per week. Format: one pre-scale risk, specific, plus implied offer. This tier closes pre-launch reviews.
3. Evals, LLM ops, and AI infrastructure people: the people discussing harnesses, MCP, A2A, guardrails. Rotate.
4. African tech and talent ecosystem: Aboyeji, Talent Nation, Lagos builders. Doubles as home-base credibility; the Lagos positioning line works here.

Volume cap: 8 to 10 comments per week total, all on-list. Repetition on a small list beats coverage on 25 accounts.

## 4. Frame library (bank one per week; all seeded from real published comments, 2026-10-06 to 2026-10-12)

1. "It behaves like a confident intern with far too much access to the wrong things."
2. "Findings become permanent tests, not closed tickets."
3. "The work doesn't disappear. It shifts from fetching to verifying."
4. "Scale proof, not voice."
5. "Cheap intelligence is an opportunity. It is also a cheaper weapon. Both stay true."
6. "The bar for breaking an AI feature is lower than the bar for building one."
7. "Mechanisms do not quit."
8. "A bad read gives you a wrong answer. A bad write gives you a wrong state, and it outlives the session."
9. "If a control has to hold, it cannot live in the prompt."
10. "Security review is what makes it 40 (days), not 7."
11. "The model is half the product."
12. "The confirmation trap wearing a new coat."
13. "Claims without instruments are marketing."
14. "Renaming it will not make it safer. It will just make the failures sound more impressive."
15. "The embarrassing detail is usually the useful one."

## 5. Weekly ritual (30 minutes, e.g. Monday and Thursday)

1. Scan the four tiers. Pick 2 to 3 posts per session that are under 6 hours old.
2. Write the comment against the spec. Bank any new frame in section 4.
3. Check threads started last week. If the OP asked a question, answer it same-day.
4. One own post per week max, structured as a comment would be: one frame, one proof, one question.

## 6. Scorecard (log weekly in this file's tail)

Per week: comments sent (target 8 to 10), OP replies received, second-degree replies, new frames banked, inbound DMs attributed to a comment, profile visits from comments (LinkedIn shows source).

KPI ranking: conversations started, then inbound DMs, then impressions. Impressions are a byproduct of placement.

## 7. Hygiene

- Proofread before publishing on big-placement posts. Known miss: the Aboyeji comment (1,757 impressions) shipped with a stray word ("smart break proof Si systems from Lagos"). Not fixable post-publish; noted so it does not repeat.
- No pitching services or Upwork in any comment. The offer, when it appears, is value-shaped (a write-up, a stress test, a demo), never price-shaped.
- The job-application comment ($65/hr AI code review gig) stays a one-off; it is an income action, not brand content.

## Weekly log

- 2026-10-06 to 2026-10-12: baseline export analyzed. ~30 external comments, 1 in 3 started a conversation. Tanya Janca replied twice. No inbound DMs logged yet.
- 2026-10-12: network snapshot (398 following / 485 followers, partial export) mapped into NETWORKING/network-asset-map.md. Tier A now has 20 named accounts; follow-back shortlist of 4. Tanya confirmed as follower (mutual); Sudhir confirmed as follower (no public engagement mention).
- 2026-10-12: first full engine conversion. The Lenny simulation comment (2,782 impressions, 7 reactions, direct-question close) produced two builder replies: Julia Kingsley (Twinning Labs) offered an architecture walkthrough and moved to email Oct 8 (Article 1 link sent Oct 9); she requested Mon-Wed ET availability Oct 9. Availability email due today. Angela Xu (atypica.AI) engaged in substance. Confirms the close rule: the direct, answerable question on the window's highest-impression comment converts. Record: NETWORKING/julia-kingsley-twinning-labs.md.
- 2026-10-12: SpaceX/Cursor story in the owner's feed (AI News World post recycling Musk's "data, talent, compute" framing). Verified real via independent news: $60B all-stock acquisition of Anysphere (Cursor), SEC filing June 16, closed Aug 14 2026, largest venture-backed startup acquisition in history; Musk's comments date from an Oct 10-11 interview. Decision: no comment (aggregator host, recycled 48h-old story, follow-CTA post, zero relationship equity). Saved counter-frame for conversations with new connections: data is the training-side moat; the unlisted fourth input is the verification side, the team that knows which behaviors break in production and has them pinned as tests. Dietrick Hardwick (Interveil Labs, AI provenance) added to the asset map Tier 2 rotation; his "thinking" reaction to the story fits his evidence-and-lineage thesis; comment-first on substantive posts only.
- 2026-10-12: second engine conversion in one week. Owner commented on Dietrick Hardwick's (Interveil Labs, 1st degree, AI provenance) post with the verification-side frame; he replied in substance within minutes (lineage makes evidence inspectable, does not prove a behavior held; failures become traceable cases that inform regression tests; "an audit layer, yes, but also a feedback path into verification"). The thread ran to five messages (owner three, his two); he extended it twice and ended describing "the bridge I want to build" (inspectable path from observation to test to revised claim, uncertainty visible). Owner closed with comment 3 (probabilistic defenses, observed versus reproduced, an anonymized worked-example offer, no question). Rule set: no further public extension; compare-notes DM (no pitch) on Thu 2026-10-15 if the thread is quiet from him through Wed. Counter-frame ("data gets you a model, tests get you a product") now has a live in-niche echo; reuse in builder conversations this week. Relationship record and DM draft: NETWORKING/dietrick-hardwick.md.
- 2026-10-12: third engine conversion. Darren Thomson (off-list exception: topic was the owner's niche verbatim, ICP audience, transcript substance) comment shipped at ~3 min post (objective-channel addition, memorable line "a scoped identity with a poisoned objective is still fully authorized while doing the wrong thing", close = question about his next episode). Host replied in-thread within the hour validating the exact addition ("Issues in both the privs AND the goal.. Stay tuned"). Off-list exceptions are valid when niche fit is verbatim; the host's reply converts the comment into a standing relationship with the Beyond The Breach audience. Reply draft (one memorable line, no question, close on a line): delivered in chat 2026-10-12.
- 2026-10-12: first own post of the week shipped: the seam post (stolen frame from Sam Illingworth's 1900 Vanegas Arroyo template-letters post, which was SKIPped as a comment: off-list, audience not ICP, best off-list post of the day). Post live with the known apostrophe-drop defect ("isnt"); owner to decide on the one-word live edit. ~1h in: 23 impressions, 1 reaction, and a direct question from Sam Illingworth himself ("How can we make those seams more visible now though?") plus a third-degree (Birgit Bonde Jensen) adding the human-absence angle that Sam picked up. Rule confirmed: banked frames posted as own content convert better than comments do on the original author's feed. Reply draft (mechanism answer, "chosen, not toggled" line, no question): delivered in chat 2026-10-12.
- 2026-10-12: Nanna Inie comment SENT (owner: "nanna inie done"). Source: today's new-contacts connect queue item 10 (NVIDIA; co-author of the LLM red-teaming definition study with Leon Derczynski, top Tier 1 account after Tanya). The comment answers her fourth research question (strategies that demonstrably counteract the effects) from the application side, with the RAG bot evidence (six probes, four worked, all fixed and pinned), close = low-friction offer of her own published online slot (Mon 16th or Tue 17th, week 47, Copenhagen or online). Comment 2 of 8-10 used this week. Sequence per plan: comment first, then connect with the pre-drafted note (#10: "The LLM red-teaming definition study you co-authored is the paper I keep coming back to..."). Watch for her in-thread reply this week; if she takes the slot, timezone is convenient (Copenhagen is UTC+1, same as owner).
- 2026-10-12: Neil Sahota comment SENT (owner: "neil done"), comment 3 of 8-10 this week. Tier 2 priority-six slot filled. ROI-metrics post (RSM survey, 99% measure AI ROI, three backward-looking measures, Netflix 2007 close). Draft shipped: third-gap frame (model answer looks the same grounded or not, decision quality stays a gut metric until answers are logged with source and override), memorable line "It's short on answers that can say 'I don't know, here's where I looked'", close on a line not a question. 4th comment on his posts in 4 weeks (bourbon Sep 15, invisible cleanup Oct 5, two-rooms Oct 7 superseded, this); cadence acceptable for a deliberate Tier G November-connect build. Awaiting his reply; the seam own post and the MCP own post ship the same thesis to his audience today, so a Neil reply that touches on verifiability cross-echoes the week.
- 2026-10-12: profile-visit signal from a named target. Apostol Vassilev (NIST, Adversarial AI research team; today's new-contacts connect queue item 6, note pre-drafted) viewed the owner's profile 25 minutes ago, 2nd degree, 3 mutuals. Most likely pull source: the MCP protocol-pivoting own post (adversarial AI at the protocol layer is his beat) or the seam post. Action: send the bare connect request immediately (note-capable requests still Premium-gated per owner plan, Premium at 1k followers; note text stays banked in connect-list item 6 for the first DM after acceptance). Named-target profile visit is scorecard KPI 3 (profile visits from comments); this one may be the first attributable to own content instead of comments. Rest of the day's viewer list is noise (3rd+ anonymous, non-niche).
