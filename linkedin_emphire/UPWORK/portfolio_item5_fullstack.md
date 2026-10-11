# Full-Stack Project — Portfolio Item 5 (ready to paste as a portfolio project)
Verified facts only, pulled from RESUME/2026-10-06_resume-audit_and-rewrite-plan.md and build_resume.py. No invented metrics, concurrency volume and document counts were explicitly flagged as unconfirmed, so they're left out rather than guessed.

**Title (for the portfolio entry):** Nigeria LandSecure — Digital Land Vault & Verification
**Role:** Full-stack engineer (Go, Next.js, PostgreSQL)

**Description:**
```
Built the document storage and verification layer for a digital land records platform: role-based permissions so only the right party can view or approve a given land document, aimed at cutting down land fraud and illegal resale.

The real engineering problem was concurrency. Multiple verification requests could hit the same record at the same time and corrupt state. I fixed it with controlled transaction handling and row-level locking in Go, so simultaneous requests resolve correctly instead of racing each other.

Same discipline I bring to AI red teaming: find exactly where a system breaks under real conditions, then fix the layer that actually failed, not just the symptom.
```

**Outcome line (if the portfolio field asks for one):** Stable verification flow under concurrent access, the same instinct that drives the red teaming side of this profile.
