# GitHub profile shell kit (2026-10-12)

Status: ALL STEPS ARE OWNER-ONLY. The sandbox token can push to linkedin_emphire only; it cannot create repos, edit repo settings, change descriptions, or change visibility (verified 2026-10-12). Paste everything below on github.com. About 25 minutes total.

Why now: the AEC client is active, has two candidates interviewing, and the proposal names a red-team harness. He can search your GitHub in 30 seconds. Today the public profile leaks the full client operation (CLIENTS/, UPWORK/, OUTREACH/, PLANS/, LEADS/ in linkedin_emphire main) and breaklab history contains client names. The shell below fixes the story; the two visibility flips fix the leak.

## Step 0 (2 min, do first): the two visibility flips

1. github.com/Teamthy/linkedin_emphire > Settings > General > Danger Zone > Change repository visibility > Make private > type the repo name.
2. github.com/Teamthy/Red-Team-Harness-My-Breaking-AI-lab- > same > Make private.
   This is audit item D1. D2 (delete and recreate clean) and D3 (rename) stay queued.
   Neither flip affects the Arena session: this branch keeps pushing to linkedin_emphire as normal.

## Step 1 (3 min): profile fields

Profile photo > Edit profile (or Settings > Public profile):

- Name: OLUSANYA TIMOTHY (keep)
- Bio (158/160 chars, paste exactly):
  AI application developer, Lagos. I build deterministic LLM systems: retrieval, tools, and failing tests that prove they hold. I break what I ship, on purpose.
- Company: Teamthy
- Location (14/50): Lagos, Nigeria
- Website (40/100): https://linkedin.com/in/olusanya-timothy

## Step 2 (3 min): the profile README repo

The profile page renders a repo named exactly like the username.

1. New repository > name it exactly `Teamthy` (case-sensitive) > Public > create.
2. Add file > Create new file > name it `README.md` > paste exactly:

```markdown
# Olusanya Timothy

**AI application developer. Lagos, Nigeria. UTC+1.**

I build LLM systems that hold up under adversarial use. The same pattern repeats across everything below: the model interprets and explains, deterministic code validates and calculates, and every acceptance claim ships with a pinned test that fails when the behavior breaks.

## Proof, not promises

- [Red-team harness for LLM apps](https://github.com/Teamthy/Red-Team-Harness-My-Breaking-AI-lab-): config-driven, 62 pinned adversarial tests, stable IDs, structured evidence, CI gating.
- [Ykay College EduPortal](https://github.com/Teamthy/ykay_eduport-): multi-tenant education platform, web plus mobile, row-level security, 663+ tests passing.
- [VisionForge](https://github.com/Teamthy/VisionForge): computer-vision inference platform: Go services, Python workers, object storage, observability, load tests.
- [Olasco Autos](https://github.com/Teamthy/olasco): request platform for a Lagos car fleet: Next.js, Zod validation, Prisma and Postgres, documented to the data model.
- Nigeria LandSecure: document platform in Go, Next.js, and Postgres with role-based permissions and revision-correct state under simultaneous writers. Case study in the portfolio.

## How I work

- Failing test before feature. A requirement I cannot express as a test is not a requirement I understand.
- The model never does the math. Untrusted content never changes permissions or approvals.
- I red-team my own builds. The RAG support bot I wrote is the same bot I broke with six injection attempts, four of which worked. All four are fixed and pinned.

## Currently

Taking a small number of fixed-scope AI builds and writing about breaking AI in public.

[LinkedIn](https://linkedin.com/in/olusanya-timothy) · [Portfolio](https://github.com/Teamthy/main-port)
```

Every claim in that file is verified against a live repo README or a public post. After breaklab gets its D2 rename, update the one harness link line to the new repo name.

## Step 3 (5 min): pins

Profile > Pinned > Edit. Up to six, in this order (first slot is top-left, the one people read first):

1. Red-Team-Harness-My-Breaking-AI-lab- (the differentiator; after D2 it becomes the renamed repo)
2. ykay_eduport-
3. VisionForge
4. main-port
5. i-confess
6. olasco

Remove the current pins (mastergo_pr, main-port, ykay-virtual, ykay_eduport-empty). main-port stays but moves to slot 4. The empty ykay_eduport (size 0) should not be pinned; ykay_eduport- is the real one.

## Step 4 (5 min): repo descriptions

Settings > General > About > Description for each (all under 100 chars, paste exactly):

- Red-Team-Harness-My-Breaking-AI-lab-: Red-team harness for LLM apps: 62 pinned tests, stable IDs, structured evidence, CI gating.
- ykay_eduport-: Education platform: Next.js, Expo, Postgres with row-level security. 663+ tests passing, CI gated.
- VisionForge: CV inference platform: Go, Python workers, object storage, observability, load testing.
- main-port: Portfolio site: Next.js 15, React 19, TypeScript. Case studies, articles, SEO static generation.
- i-confess: Daily audio-session and habit platform. Go backend, scheduled sessions, phases 0 to 8 closed.
- olasco: Request platform for a Lagos car fleet: Next.js, Zod, Prisma, Postgres, WhatsApp handoff.

## Step 5 (later, not today): prune the wall

The other ~100 public repos (one-commit exercises, 28 learning forks, typo names) are the junior wall behind the pins. Archive or privatize the ones you never want seen. Ten that matter: the six pins, CDRL, assetflowserver, ykay-virtual, linkedin_emphire (private by then). Do this in an evening, never the morning of a client conversation.

## What the owner does after (in order)

1. Steps 0 to 2 now (8 min). The leak is closed and the profile page reads as a senior AI developer.
2. Steps 3 to 4 today (10 min).
3. Send the AEC proposal (paste-ready in UPWORK/PROPOSALS/2026-10-12_aec-construction-estimating-mcp.md) when the owner is ready; it is 0 of 3 on the daily cap.
4. Tuesday 10-13 critical path unchanged: run the four lab tests before 09:00 WAT, the agent fills the four [LAB RESULT] slots, publish 10:00 WAT, Tanya DM 2 only after confirmed publication.
5. St Louis thread same-day answer check and the Monday Tier 1 ritual are still open from the week plan.
