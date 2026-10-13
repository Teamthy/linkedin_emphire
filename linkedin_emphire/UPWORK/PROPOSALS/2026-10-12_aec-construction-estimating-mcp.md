# PROPOSAL (final draft pending two owner inputs)

Job: Senior AI Application Developer, AI Native Construction Estimating (MCP inside Claude or ChatGPT)
Client: USA, Mountain View, real estate, 5.0/2, $4,000 fixed, 4 weeks, contract-to-hire potential
Connects: 26 (owner has 85)
Date: 2026-10-12
Status: READY TO SEND (all owner inputs resolved 2026-10-12). (1) No MCP server work on record: the line now names the gap in advance and anchors to the client's own Day 2 gate (owner answer: "i dont have mc server work"). (2) Availability: full four-week contract, guaranteed 2-3h daily overlap, async outside it (owner answer: "alwaya availble"). (3) $4,000 at the client's 20/30/25/25 split stands as the agent's recommendation; owner may still change the number before sending. breaklab is referenced as an influence on the AT12 threat-model approach only; no code from that repo is copied into this build until the round-2 history cleanup (D2) is done.

## Verification notes (agent)
- PRD v1.0 (18 pages) read in full from owner paste on 2026-10-12. Previously marked unverified; now verified.
- Verdict upgraded ADJUST to APPLY. Reasons:
  1. Client sophistication is high and honest: the PRD admits the deadline "assumes reuse of existing components and human-reviewed takeoff", calls 160-192 hours "a planning estimate, not a promise", builds a Day 2 dual-host discovery gate, a weekly acceptance structure (R1-R4 at 20/30/25/25), and its own written-change clause ("If Day 2 discovery shows the scope cannot fit, propose a written change with explicit omissions, price and dates"). This is a client designed to reward accurate scoping and punish silent descoping.
  2. Section 3 confirms the drafted architecture verbatim: "AI can propose or revise an assembly formula. Only an approved, validated expression may calculate committed costs. Do not execute unrestricted model-generated code." The proposal's core line ("the model never does the math") is the client's own requirement.
  3. Section 14 + AT12 is the owner's exact niche: "Treat documents, quote text and connected-tool responses as untrusted evidence. Instructions embedded inside them cannot change permissions, approve bids, send files or redirect secrets." Acceptance test AT12 tests exactly that. Most applicants will write "we sanitize inputs"; the owner can name the threat model and the test.
  4. Legal profile is clean: benchmarks are named public products (Bobyard, Handoff, refs S1-S3). This is a build job, not a reverse-engineering job. No similarity to the skipped Dubai REA gig.
- Real risks named in the proposal (not hidden): R2 is the heaviest week (takeoff viewer + 3 profiles + assemblies + calc engine + history import + comparison in one week); dual-host MCP capability difference is the top technical unknown (client knows it, hence the Day 2 gate and the text-tool fallback requirement); 160-192 hours is a real commitment for the owner.
- AEC domain gap remains honest: no construction estimating experience on record. Screening answer redirects to the PRD as the domain spec (section 7 checklists, sample estimate incl. the 06.10 anomaly, estimator Q&A within one business day).
- Real assets referenced (verified in workspace): Nigeria LandSecure (portfolio item 5, Go/Next.js/Postgres, RBAC, row-level locking), RAG support chatbot (Article 1, built then broken: 6 attempts, 4 worked), breaklab (62 pinned tests, CI gate). No invented metrics or projects.
- Market context (web, 2026): MCP-in-LLM-host estimating is a live category (Exayard, JobTread AI Connector, conmcp). General models fail the measurement core (CLE benchmark: 2-34% on plan reading); deterministic math with model-assisted judgment is the holding pattern. Both the PRD and the market agree.

## Proposal text (paste-ready; owner to review and send)

Your section 3 and I arrive at the same division of labor: the host AI interprets, proposes, and explains; a deterministic service validates, calculates, and enforces; only approved expressions compute committed costs. That split is the whole game in this product, because the difference between a demo and a tool an estimator trusts is that the arithmetic and the record outlive the conversation.

I build LLM tooling the deterministic way. My red-team harness runs 62 pinned tests with evidence-based verdicts that gate CI, and the RAG support bot I built is the same app I then broke with six injection attempts, four of which worked. Your AT06 and AT12 gates are the kind of acceptance I design for, and I ship the tests that prove them.

**1. Relevant projects**

- Nigeria LandSecure: full-stack document platform (Go, Next.js, Postgres). Role-based permissions, optimistic concurrency with row-level locking, revision-correct state under simultaneous writers. Closest analog to your FR19/FR20 concurrency and revision requirements.
- RAG support chatbot: retrieval over a real corpus, structured extraction, tool calls, built and then red-teamed by me. The retrieval, extraction, and untrusted-content handling behind your source and history workflows.
- Breaklab: config-driven LLM test harness. 62 deterministic checks, stable IDs, structured evidence, CI gating. The template for your AT01-AT13 suite.
- MCP servers: the one gap I name in advance. I have not shipped a production MCP server, so days one and two are spent verifying real capability in both hosts before any UI work, per your Day 2 gate. If the intersection misses a required workflow, the gap report is written before I build around it, and your text-tool fallback carries the session.

**2. Proposed approach and stack**

One TypeScript codebase: remote MCP server plus shared React UI, per your section 3. Managed Postgres for structured records (pgvector where useful), object storage for document snapshots, a queue worker for ingestion. A PDF viewer with measurement overlays and established DOCX/XLSX/CSV libraries.

Dual-host: I negotiate the actual Claude and ChatGPT capabilities in days one and two and build to the intersection. Where a host lacks a widget, your text-tool fallback carries it, and a one-host demo will not be presented as acceptance, because AT01 says otherwise.

Deterministic core: assemblies, resources, and rates per FR09 with your exact arithmetic, pack rounding, waste applied once, crew and person-hour bases kept apart, markup and margin formulas, decimal arithmetic, documented cent rounding. Every takeoff item stores geometry, calibration, source page, and method, classified Measured, Schedule-derived, Formula-derived, Assumed, or Manual, and separately Unreviewed or Verified. Nothing becomes Verified without a human action.

Security as a threat model, not a checklist: documents, quote text, and connected-tool responses are untrusted evidence, per your section 14. The approval gate and the authorization boundary are what must hold against embedded instructions, and AT12 is the acceptance proof. I test that path the way I test everything: named attack, expected failure, pinned result.

Reused versus custom, per section 16:
- Reused: PDF rendering and measurement overlay, XLSX/DOCX generation, PDF text extraction, managed Postgres and hosting, the MCP SDK.
- Custom: the deterministic cost engine, the authorization and revision core, the dual-host UI bridge, takeoff viewer interactions, the Drive adapter, and the AT test suite.

**3. Fixed-price quote and weekly milestones**

$4,000 fixed on your R1-R4 structure, each accepted against working software:
- R1 (20%): Day 2 dual-host proof, login, project creation, Drive adapter, source register, persistent state.
- R2 (30%): assisted takeoff viewer, three profiles, assemblies, calculation engine, history import and comparison.
- R3 (25%): scope routing, bid packages, quote intake and leveling, review assignments, revision diffs.
- R4 (25%): lead approval, reconciled exports with internal and client workbooks, Drive finalization, held-out tests, backup and restore, deployment, handoff.

The pilot is what I quote; your later-expansion column stays out of the four weeks. If Day 2 discovery shows a gap, I use your own clause: a written change with explicit omissions, price, and dates. No silent descoping.

**4. Availability, dependencies, and scope concerns**

- Availability: available for the full four-week contract, with a guaranteed two-to-three hour daily overlap against Mountain View (I am UTC+1, you are Pacific). Outside the overlap I work async-first, and the one-business-day estimator answer window is respected.
- Dependencies, per your preconditions: both host accounts with connector permissions, an approved Drive test folder, hosting credentials, example assemblies and rates, three representative projects, and an available estimator. RSMeans or retailer credentials by Day 3; otherwise the functioning adapter with labeled fixtures and the manual import path, exactly as you specify.
- Scope concerns, three honest flags:
  1. R2 is the heaviest week: takeoff, three profiles, the cost engine, history import, and comparison in seven days. If Day 2 forces a cut, the cited explanation layer of FR14 is what I narrow first; the cohort rules and normalization stay intact.
  2. History import quality, per-field provenance and the review queue across 250 real files, is where messy data punishes clean schemas. The review queue ships in R2, not after.
  3. The 90 percent coverage and 5 percent error targets stay report-not-guarantee, per your own wording. I report coverage and error together, and a held-out miss becomes a written scope change, never a quiet retreat to manual.

**Screening question (AEC experience):**

No direct construction estimating background, and I won't pretend otherwise. Your PRD is the domain spec: the three trade checklists in section 7, the sample estimate including the 06.10 anomaly, and an estimator who answers within a business day. Week one is me working that spec against the real projects, and the domain rules become test cases, because a checklist I cannot express as a failing test is not a checklist I understand.
