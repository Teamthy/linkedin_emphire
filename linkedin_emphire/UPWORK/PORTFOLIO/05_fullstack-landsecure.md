# Portfolio Item 5 — Nigeria LandSecure (Full-Stack Project)

**Project title:**
```
Nigeria LandSecure: Digital Land Vault and Verification
```
**Your role:** Full-Stack Engineer (Go, Next.js, PostgreSQL)
**URL:** (none needed, unless a live demo/repo link exists)
**Skills/tags:** Full Stack Development, Golang, Next.js, PostgreSQL, API Development

**Description:** full text in `../portfolio_item5_fullstack.md`, paste directly, no changes needed.
**Image (landscape, 1584x990):** `../gallery/05_photoreal_landsecure.png`
**Image (square, 1080x1080):** `../gallery/05_photoreal_landsecure_square.png`

## The Full Story — What, Why, How

**What was done:** Built the document storage and verification layer for Nigeria LandSecure, a digital land-records platform, including role-based permissions controlling exactly who can view or approve a given land document.

**Why it was done:** Land fraud and illegal resale are real, documented problems in Nigeria's land market, largely because paper land documents are easy to forge, duplicate, or quietly resell to a second buyer. Making land-document verification checkable and permissioned, instead of relying on physical paperwork, directly targets that failure mode.

**How it was done:**
1. Used Go for the backend, Next.js for the frontend, and PostgreSQL for storage.
2. Designed role-based access so only the correct party for a given record, such as the owner or an assigned verifier, could view or approve it, rather than a flat model where any logged-in user sees everything.
3. Identified concurrency as the real engineering risk in the system: multiple verification requests could hit the same record at the same time and corrupt its state if handled naively.
4. Solved it with controlled transaction handling and row-level locking in Go, so simultaneous requests against the same record resolve correctly in sequence instead of racing each other and leaving the record in a bad state.
