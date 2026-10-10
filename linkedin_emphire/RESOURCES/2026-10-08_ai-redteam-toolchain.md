# AI Red Teaming Toolchain — reference (verified Oct 8, 2026)
## Open source core
- Garak (NVIDIA, Apache 2.0) — "nmap for LLMs," 100+ probes: injection, jailbreaks, encoding, extraction. v0.14.0 (Feb 2026). FIRST TOOL. Leon Derczynski = connect-list target.
- Promptfoo (MIT, now OpenAI, open-source commitment) — evals + redteam CLI, 50+ vuln classes, YAML, CI gating. Used internally at OpenAI/Anthropic. TOOL FOR TEAMS / CI.
- PyRIT (Microsoft, MIT) — attack orchestration: Crescendo multi-turn, TAP auto-jailbreak, multimodal. FRAMEWORK for custom adversaries.
- DeepTeam (Confident AI) — 40+ vulns mapped to OWASP LLM Top 10.
- Giskard — scan suite, bias/hallucination/agentic, ML-team friendly.
## Agent-specific (frontier layer)
- MCP Scan (Invariant Labs) — MCP server scanner: injection in tool descriptions, server impersonation, unsafe composition. -> feeds the planned MCP article (late Oct).
- Agentic Radar — static analysis of agent tool graph, excessive-agency flags pre-runtime.
## Defensive (test against)
LLM Guard (Protect AI), NeMo Guardrails (NVIDIA), Llama Guard (Meta), Rebuff, Lakera (Gandalf playground), Guardrails AI.
## Commercial names (market proof, not buys)
Lakera Red, Mindgard, HiddenLayer, CyberArk FuzzyAI, Promptfoo Enterprise. Existence proves demand: continuous scanning + auditor reports = what Timothy sells scoped, at consultant prices.
## Timothy's stack order
1. TODAY (1 hr): pip install garak -> test chatbot -> garak --target ... --probes prompt_injection -> screenshot for Article 3. (This closes the lab-setup task.)
2. This week: promptfoo redteam YAML on same bot -> checklist-follow-up content.
3. Before MCP article: MCP Scan on one public MCP server -> first-mover article.
4. Later: PyRIT Crescendo multi-turn demo.
## Positioning truth
Tools find broken prompts. Timothy's edge = judging whether the harness itself is honest (test adequacy, overfitting, gameable reward). "Evaluation of the evaluation." Use in Terac interview + Article 4+.
