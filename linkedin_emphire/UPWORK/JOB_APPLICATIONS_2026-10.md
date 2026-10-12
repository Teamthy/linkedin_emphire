# Job Applications Tracker, October 2026

Workflow: owner pastes best-match job postings (Upwork and LinkedIn) with full details; agent verifies (a) real or bait, (b) relevant to the named company via keyword search, (c) worth applying against the two listing shapes and the AI red-teaming / RAG security niche. One verdict per posting: APPLY (with proposal angle), ADJUST, or SKIP.

## Rules

- Cap: 3 applications per day, batched into one sitting; never on a morning with a pending article publish.
- Every application is custom: first two lines specific to the posting, proof from real deliverables only (the 21-part series, the live break-and-fix record, the portfolio pipeline). No template proposals.
- Owner's paste is the source of truth for Upwork client-card data (agent sandbox cannot open upwork.com or linkedin.com). Unverifiable claims are marked unverified, never assumed.
- Standing Upwork policy rule: all communication and payment on-platform. Any off-platform contact request is an automatic red flag.
- Log outcomes (viewed / interview / offer / no response) so the posting type that converts can be read after two weeks.

## Red flag quick list

Upwork: payment verification missing; new client account with large budget and urgency; budget below market for the stated scope; off-platform contact request; free "test task" gate; client name inconsistent with posting content; hourly range and fixed budget contradict each other.
LinkedIn: company with no public product matching the role; Easy Apply funnel from a recruiting agency for a "direct" role; stale repost (months old); salary band incompatible with the stated level; role keywords do not appear anywhere in the company's public work.

## Verdict schema

- Verdict: APPLY / ADJUST / SKIP
- Real: yes / no / unverified (with the evidence used)
- Company relevance: what the keyword search found, one line
- Fit: match to which listing shape and which skills
- Angle: first two proposal lines, paste-ready (APPLY/ADJUST only)
- Effort: low / med / high (proposal length, revisions likely)
- Risks: named red flags, if any

## Log

| Date | Source | Title | Company / client | Budget | Verdict | Why (one line) | Angle | Status |
|---|---|---|---|---|---|---|---|---|
| 2026-10-12 | LinkedIn (aggregator post) + official page fetched | Associate, Full Stack Developer (Req R260054, posted 2026-10-07) | BlackRock, Mumbai (Nesco IT Park Tower 4) | Not disclosed; third-party estimate 11-18 LPA (unverified) | SKIP | Real and active, but Mumbai hybrid with at least 4 office days/week (relocation from Lagos required), junior level, Angular-first generalist frontend for the Global Marketing digital team, pay far below the consulting trajectory | n/a (skip) | Verified against careers.blackrock.com, no application |
| 2026-10-12 | Upwork (owner paste, posted ~37m before paste) | AI-assisted RE of a SaaS with REA MCP, rebuild 6 Instagram audience-intelligence features in Next.js/Supabase | ARE, Dubai (5.0/9 reviews, 32 jobs, $4.5K total spent, 69% hire rate, payment+phone verified, member since Aug 2025) | $900 fixed (M1 $150, 2-3 days; M2-3 "priced from your estimate") | SKIP | Real client and real tool (morluto/rea verified on GitHub: 119k stars, MIT, pushed same day), but budget below market for 6 modules on a ~$180/hire client, must-have "hands-on Instagram Graph API or Meta webhooks" cannot be claimed without violating the no-fabrication rule, M1 is permissionless RE of a third-party SaaS which contradicts the public brand (test only what you own or have written permission for), and the core features cannot run on the official IG API (verified 2026 sources: first-party only, no cross-account data, no follower lists, stories gone after 24h), so the rebuild inherits unofficial-data ban risk; 50+ proposals with 3 already interviewing; M1's 2-3 days collide with the Article 2 publish (tracker rule: no applications on a publish morning) | Override angle held in chat (data-source truth as the differentiator), not used | Not applied |
