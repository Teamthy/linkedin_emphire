# DRAFT PROPOSAL (not sent)

Job: Senior AI Application Developer, AI Native Construction Estimating (MCP inside Claude or ChatGPT)
Client: USA, Mountain View, real estate, 5.0/2, $4,000 fixed, 4 weeks, contract-to-hire potential
Connects: 26 (owner has 85)
Date: 2026-10-12
Status: DRAFT, owner to fill [BRACKETED] items with real specifics before sending

## Verification notes (agent)
- Posting data from owner paste (source of truth per tracker rule). Sandbox cannot open upwork.com.
- Attached PRD (314 KB) NOT read by agent: mark as unverified. Owner must build Section 3 against the PRD's pilot scope and acceptance criteria, not the posting's full feature list.
- Market context (web, 2026): this is a real, active category. Exayard (MCP server for takeoff/bidding from Claude), JobTread AI Connector (open MCP, Claude/ChatGPT into live job data), conmcp (open-source plan-reading MCP server), Togal.AI + CLE benchmark (general models score 2-34% on plan-reading tasks). Differentiator: general LLMs fail the measurement core (no scale, hallucinated quantities, no audit trail). Deterministic layer for math, model for judgment, source citations on every quantity.
- Honest gaps (do not claim beyond these):
  1. No AEC construction estimating experience. Screening question handled with transparent redirect.
  2. No MCP server build on record in the workspace (breaklab is a CLI harness). If owner has real MCP server work elsewhere, name it in Section 1. If not, the approach below covers it and the draft does not claim it.
- Real assets referenced (all verified in workspace): Nigeria LandSecure (portfolio item 5: Go/Next.js/Postgres, RBAC, row-level locking), RAG support chatbot (Article 1, built then broken: 6 attempts, 4 breaks), breaklab (62 pinned tests, CI gate). No invented metrics.

## Proposal text (adapt, then send)

The hard part of this build is not the chat UI. It is the part where the estimate has to be right: quantities measured at the correct scale, prices pulled from the right source, and every number traceable back to a sheet or a supplier. That is exactly where a general-purpose model inside Claude or ChatGPT fails, and it is the part I design for first.

I build LLM tooling the deterministic way. My red-team harness runs 62 pinned tests with evidence-based verdicts that gate CI. The RAG support bot I built is the same app I then broke with six injection attempts, four of which worked. I ship software I have already tried to break, and I send back the tests that prove it.

**1. Relevant projects**

- Nigeria LandSecure: full-stack document verification platform (Go, Next.js, Postgres). Role-based permissions so the right party views and approves each record, and concurrent write handling with row-level locking so simultaneous requests resolve instead of racing. Closest analog to the workspaces, permissions, and document handling in your PRD.
- RAG support chatbot: retrieval over a real corpus with structured extraction and tool calls. The retrieval and extraction layer this job needs, built by me and tested against real inputs.
- Breaklab: config-driven LLM testing harness, 62 deterministic checks, CI gate. Proof of the "reliable calculations plus automated testing" bar your post asks for.
- [REAL MCP SERVER WORK, if it exists. Name it with one line of evidence. If not, delete this line entirely.]

**2. Proposed approach and stack**

Next.js 14 and TypeScript on the front end, Node/TypeScript backend, Postgres (Supabase) for project data and estimate history, Google Drive API for historical estimates, PDF and Excel generation for exports. The app exposes an MCP server as the integration surface for Claude and ChatGPT, and the cost and supplier connectors plug in as configurable MCP endpoints.

The architectural decision that determines whether your estimators trust the output: the model never does the math. A deterministic layer owns quantities, scale, pricing, and totals. The model owns judgment and language, reading scope, flagging gaps, drafting the written proposal. Every extracted quantity carries its source (sheet and element) and a confidence flag, and nothing enters an estimate without estimator approval. General-purpose models score in the single digits to low tens of percent on plan-reading benchmarks; the pattern that holds under a real bid is deterministic measurement with model-assisted review, and that is how I build everything.

**3. Fixed-price quote and weekly milestones (4 weeks, against the PRD pilot scope)**

$4,000 fixed, four weekly milestones, each paid on Upwork at acceptance:

- Week 1: workspaces, auth, database schema, MCP server scaffold, Google Drive connector spike against real historical estimates
- Week 2: document ingestion, extraction with source citations, editable estimate tables
- Week 3: historical estimate comparison, subcontractor bid requests and quote comparison, lead-estimator approval loop
- Week 4: version history, PDF/Excel exports, full test suite, deployment and handoff documentation

[Milestone boundaries above are a first cut from the posting. Re-read the PRD today and realign them to its pilot acceptance criteria before sending. If the PRD pilot is narrower, say so in one line here.]

**4. Availability, dependencies, and scope concerns**

- Availability: [REAL availability window]
- Dependencies: Google Drive access plus two or three sample historical estimates, sample plan PDFs for takeoff testing, and the cost/supplier data source you want in the MCP connections.
- Scope concerns (you asked, so two honest flags):
  1. The posting lists the full vision; the PRD defines the pilot. I quote the pilot's acceptance criteria and defer the rest, exactly as the PRD itself does.
  2. AI takeoff from raster plans is the highest-risk component in this space. I would keep pilot quantities in a human-approved flow with full source citations and defer fully automated raster takeoff to a later release, where it can be done properly.
  3. [OPTIONAL] Multi-user collaboration is what usually slips week 4. I would ship single-project with version history and move multi-user roles to release 2.

**Screening question (AEC experience):**

No direct construction estimating background, and I would rather be straight about that than pad it. What I bring instead: I have built and run AI features on top of domain data (a RAG support bot over a real corpus, a document platform with permissions and concurrent write handling), and I close domain gaps the disciplined way. Week one is the PRD, your historical estimates in Drive, and your estimating workflow, and the domain rules become the spec.
