# AI Red Teaming interview question bank (32 Q&A) — Oct 8, 2026
Use for: Terac 10-min AI interview, micro1 follow-ups (if human round), any AI-security role/client call.
Answer format always: Point -> Reason -> Your example -> Stop. 60-90 seconds.

## Definitions & positioning
1. AI red teaming in one sentence -> structured pessimism: attack your own AI like a hostile user, write down what breaks before a stranger does.
2. vs pentesting -> probabilistic behavior, attack-success RATES not pass/fail, surface includes English.
3. vs QA -> QA validates expected paths; red team adversarially validates unexpected. Builders can't self-test (confirmation trap; own proof 6/4).
4. vs bug bounty -> scoped+scheduled+design-targeted vs open-market. "Bounty finds holes. Red team says which rooms shouldn't exist."
5. why builder fails as only tester -> optimizes confirmation; helpful bot tested with helpful questions.

## Attack knowledge
6. injection vs jailbreak -> jailbreak = user attacks model policy; injection = third-party content attacks app instructions. Most products defend jailbreak, ignore injection.
7. direct vs indirect -> indirect scarier: hides in content system reads; attacker never touches product. RAG PDF-footer test as example.
8. system prompt leak -> looks prank, is info leak; can't fix in prompt ("telling the secret to the party you hide it from").
9. tool-call/agent attacks -> forgery, argument tampering, confirmation bypass, runaway loops. Fixes outside model: scoping, allowlists, idempotency, iteration budgets, human gate on irreversible.
10. RAG poisoning -> attacker text enters retrieval corpus; injection AND integrity failure; plan to demo on camera for series.
11. forgotten exfil -> markdown image URLs, tool params, errors, timing, anything agent can SEND. "What can it write, not say."
12. multimodal -> text in image via OCR = retrieval with extra steps; CV background = differentiator.
13. denial of wallet -> forced loops/huge context/agent retries = bill spike or outage; budgets & circuit breakers.
14. memory poisoning -> persists one injection into future users; TTL, review, separate user-words from system-facts.

## Defenses
15. works -> least-privilege tools, code-enforced confirmations, isolation (dual-LLM), budgets, regression in CI. All boring, all real.
16. fails alone -> prompt guardrails, "never do X", classifiers-as-only-line, "injection solved" vendors.
17. overkill -> read-only tool on public data with no PII path. Effort = blast radius.
18. can't fix -> known-limitation doc, reduce surface, log, tell owner. Hidden = incident with deadline.

## Process & reporting
19. 2-week engagement -> boundaries day1, layered tests to day8, convert findings->regression day9-10; report for founder, evidence for engineer.
20. finding format -> plain line, exact repro, business impact sentence, severity L x B, fix snippet + regression test.
21. auto vs manual -> ~60% scans (garak/promptfoo) for coverage, manual for weird; "tools find broken prompts, judgment finds broken design."
22. done? -> budget decision: all high-impact paths fixed or accepted in writing; suite runs in CI.

## Scenarios (structure beats speed)
23. support bot w/ refund+email -> trust map, 5 attack families, top finding = refund tool trusts any ID in context; fix = own-auth-ID only.
24. email-reading CRM agent -> lethal trifecta (untrusted input + private data + action channel); finding: model decides the write gate = design flaw not model flaw.
25. internal HR bot -> integrity over confidentiality; test corpus write access first.
26. "model 10x better wastes suite?" -> no: half findings are architecture; suite pins the floor.
27. found something embarrassing -> scope discipline, minimum evidence, private disclosure to owner, publish only with permission.
28. client won't fix -> written acceptance + date + name. Red teaming = risk made visible and owned.
29. found unbreakable? -> honestly yes when tools tightly scoped/no secrets/no writes: proof method works. Never promise all-breakable; promise all-testable.
30. injection solved? -> not at research layer (instruction/data mixing persists), containable at deploy layer. Practice lives in gap.
31. guardrail vendors -> test, don't trust; job = measure bypass cost, not marketing.
32. everything missing -> an OWNER for the failure: permission map held by someone with authority to stop it. "Half of findings = orphaned controls."

## STORY BANK (reuse these, they're current + verified)
- own chatbot 6 attempts / 4 breaks / pineapple refund / prompt leak (Oct 2 post, live)
- "doors look fine until someone tries the handle" (Oct 3 post)
- system prompt = production config nobody put in a diff (Oct 6 post)
- Tanya-thread: log the permission surface, not just the action (Oct 7)
- Tarique CHC thread: authority drift; audit trail = forensics not prevention (Oct 8)
- WM Media: free inside the building, gated outside it (Oct 7)
- BCG authorization gap: separation of duties collapses under one broad-credential agent (Oct 7)
