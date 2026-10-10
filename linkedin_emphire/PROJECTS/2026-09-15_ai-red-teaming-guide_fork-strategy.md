# Fork Strategy: Teamthy/AI-Red-Teaming-Guide
Forked from: requie/AI-Red-Teaming-Guide (Tarique Smith, Cogensec)
Your fork: https://github.com/Teamthy/AI-Red-Teaming-Guide
Date: 2026-09-15
Status: Clean fork, 0 ahead, 0 behind (no commits yet)

## WHY THIS FORK CHANGES THE TARIQUE OUTREACH
A cold note says "I like your work." A fork with real, thoughtful commits says "I'm engaging with your work at the builder level — here are improvements I made that you might want."

Tarique is building Cogensec and maintaining this guide in public. Any serious, useful PR to the guide is worth 100 cold DMs. He will look at your GitHub if he accepts your connection note — and when he sees your fork has commits with real improvements (not typos), that's the moment he takes you seriously as a builder, not a fan.

The strategy:
1. Make your fork visible (star Tarique's repo, add your own notes/improvements in a branch)
2. Contribute small, legitimate improvements first (build trust)
3. Add one meaningful contribution that draws on your UNIQUE expertise (CV / African tech / multi-domain building)
4. Open a PR. Reference it in the DM AFTER he accepts your connection.
5. The PR becomes the natural conversation starter — not "be my mentor" but "I built X while studying your guide, thought it might be useful."

---

## PHASE 1 — THIS WEEK (before sending the connection note OR within 3 days of him accepting)

### 1.1 Clone the fork locally and READ IT end-to-end
You can't contribute what you haven't read. Go through:
- README.md (main guide)
- Attack Vectors & Techniques section
- templates/ directory (PR checklist, test-case library, vulnerability report, threat-modeling workshop templates)
- CHANGELOG

Pay special attention to the sections that touch your lane:
- **MCP pinning / agentic checks** (from the PR checklist template) — this is exactly where you've been commenting all day
- **Multimodal / CV attack surfaces** — look for gaps (see Phase 2)
- **OWASP LLM Top 10 (2025) references** — verify links, see if anything's outdated

### 1.2 Small, legitimate improvements you can PR in the next 3 days
These are LOW effort, HIGH signal. Tarique will notice because they show attention to detail, not grandstanding:

- **Link rot check.** He has a lychee link-check CI, but run it yourself and fix any broken references that have slipped through in the last few weeks. Open a PR: "Fix broken reference links found during lychee run."
- **Typo/grammar/clarity fixes in the README.** Read with fresh eyes and flag sentences that are confusing for someone new to red teaming. Open a PR: "Clarity pass on README sections X and Y for first-time readers."
- **Check the templates for completeness.** He added agentic checks (MCP pinning, agent registry, inter-agent auth) to the PR checklist in June. Are any other emerging attack surfaces missing? E.g., tool-call injection patterns that became known after June 2026? If you find a genuine miss, that's a real PR.

**Rule:** Start with at least one SMALL merged PR before proposing anything big. Small PRs prove you're serious and not drive-by.

### 1.3 Star Tarique's upstream repo (if you haven't) + follow him on GitHub
GitHub shows followers/stars. He'll see the notification.

---

## PHASE 2 — 1-3 WEEKS: YOUR UNIQUE CONTRIBUTION (the one that gets his attention)

This is where you bring something NO ONE ELSE can bring to his guide. Tarique is a NYC-based security product leader. His guide is excellent on general LLM/agent red teaming. But there are three big gaps that your specific background makes you the right person to fill:

### CANDIDATE A — Multimodal / Computer Vision Red Teaming appendix (HIGHEST IMPACT)
His guide is heavily text/LLM/agent focused. CV red teaming is a rapidly growing attack surface (deepfake evasion, adversarial patches on physical objects, perception attacks on autonomous systems, facial recognition bias exploitation, the AirPods-camera/POV perception attack surface Tom Emrich wrote about today).

You work in CV. Add an appendix: `appendices/multimodal-cv-red-teaming.md` covering:
- Adversarial patches in physical environments
- Deepfake detection evasion (especially relevant for African election-cycle concerns you talk about)
- Biometric system bypass / bias exploitation (ties to your non-Western-names hiring-bias point)
- Perception-layer attacks on embodied AI / robotics / vision-equipped agents (ties directly to the physical AI / Tom Emrich / Cogensec endogenous agent security angle)
- CV-specific tooling for red teaming (adversarial patch generators, facial-rec attack toolkits, etc.)
- Case studies of real CV failures in production

A non-trivial, useful section like this on a real gap in the guide will get his attention. It ties directly to Cogensec's thesis (endogenous agent security — agents with eyes need endogenous security too).

### CANDIDATE B — Global South / African AI Risk Case Studies addendum
He lists attack vectors and case studies, but they're mostly US/EU-centric (OpenClaw, promptfoo, Western data breaches). Add a section or case-study collection on:
- Deepfake-driven election interference in African markets (Kenya 2022 fake audio, Nigeria 2023 deepfake video incidents, etc.)
- AI-powered mobile-money/social-engineering attacks in markets with high mobile-money penetration (M-Pesa, Opay, etc.)
- Biometric identity system exploitation risks in markets rolling out digital ID (Nigeria's NIN, Kenya's Huduma Namba, etc.)
- Low-data-language attack surface (models trained primarily on English failing hilariously/dangerously on Yoruba, Igbo, Hausa, Swahili inputs)
- Regulatory gaps — African nations don't have the AI Act / EO style frameworks the US and EU are building; red teaming takes on different urgency.

This is a perspective literally no NYC security researcher can write authentically. It would make his guide genuinely global.

### CANDIDATE C — Practical hands-on red teaming lab for AI integrators (builders, not just security researchers)
His evaluation harness is marked "illustrative, non-production." You're a software engineer who BUILDS AI integrations, not a pure security researcher. Build out:
- A simple, runnable lab (with Docker or notebook) that walks an AI-INTEGRATION engineer through red-teaming their OWN RAG app / agent / tool-calling system
- Focus on the boring production failures you've been writing about (prompt injection leaking PII, tool-call injection in MCP servers, over-trust of AI outputs, data exfiltration through tool use)
- This targets a different audience than his existing guide (which skews security researcher / professional red team) — it targets the millions of app developers who are adding AI to products without knowing how to attack-test them

My pick: **A (CV appendix)** is highest impact because (1) it directly aligns with Cogensec's agent-security thesis as agents gain perception, (2) you genuinely have the CV expertise to write it, (3) multimodal red teaming is one of the fastest-growing gaps in the space right now, and (4) it ties all your public positioning this week into one coherent package.

B (Global South) is a strong runner-up and can be folded into A or done separately.

---

## PHASE 3 — THE PR + DM SEQUENCE (the natural mentor ask without asking)

Once you have at least one small merged PR AND the larger CV appendix (or a draft of it):

### 3.1 Open the PR
- Clear title: "Add appendix: Multimodal / Computer Vision red teaming considerations"
- PR description should be humble and clear:
  > Hey Tarique — been studying your guide while going through AI red teaming coursework (and building AI/CV integrations out of Lagos). I noticed multimodal / CV attacks weren't covered in depth, and as someone who ships CV systems I kept running into attack surfaces the current sections don't address (adversarial patches, perception attacks on agents with cameras, biometric bypass, deepfake evasion in production).
  >
  > Drafted an initial appendix covering CV-specific red teaming considerations. Happy to iterate, trim, add tooling refs, or break this up differently if you'd prefer. No pressure to merge if it doesn't fit the guide's direction — I'll keep maintaining it on my fork either way.

Notice the tone: humble, useful, no pressure, references Lagos/CV-building credentials naturally, offers to iterate.

### 3.2 If he merges, replies, or even just comments on the PR
THAT is your opening to message him. Not with "be my mentor" — with:
> Hey Tarique — really appreciate you taking the time to look at the PR. Working through your guide has been genuinely helpful as I've been going deeper on AI security from the builder side.
>
> One thing I've been wrestling with as a software engineer (not a pure security person) is [insert a genuine technical question you've hit while building — maybe about MCP server trust boundaries across agent fleets, or how to think about red-teaming systems where the CV model is supplied by a third party and you can't audit weights]. Would value your take whenever you have a minute — no rush.

If he answers thoughtfully, that's a real technical conversation. Then, 2-3 weeks later (after you've had a few exchanges AND he's seen you keep contributing):
> Hey Tarique — I've really appreciated the back-and-forth on this stuff. You've basically been mentoring me through your guide and PR feedback without the title. Would you be open to being an ongoing point of advice as I keep building in this space? Happy to be as low- or high-lift as works for you.

That's how you earn it.

---

## PHASE 4 — CONTENT ANGLES (all while building)

As you work through the guide and build additions, you get free LinkedIn content:
- "Here's what I learned going through Tarique Smith's AI Red Teaming Guide this week — three things that surprised me as an AI integration engineer"
- "I tried to red-team my own RAG app using the methodology in this guide. Here's what I broke."
- "Multimodal AI systems are coming (AirPods cameras, embodied agents) and almost no one is red-teaming the perception layer" — ties directly to Tom Emrich's post today
- "I contributed an appendix to an AI red teaming guide this week. Here's what open source taught me about security."

These posts work because they're about real work, not hot takes.

---

## DON'T
- Don't open a PR fixing typos on your first day and immediately ask for mentorship. Build trust first.
- Don't add 10 random tools to the tools list without testing them — Tarique already cares about correctness and removed unverified claims.
- Don't fork and never commit — an empty fork doesn't help you.
- Don't copy content from other sources without attribution — he runs a lychee/link checker, he'll notice.
- Don't add an "AI in Africa" section that's generic — make it specific, named, cited. Real incidents, real case studies, real tools.
- Don't treat this like a shortcut. The whole strategy works because you're GENUINELY learning and contributing — not gaming a relationship.
