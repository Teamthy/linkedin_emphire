# Comment + note — Jesse Zhang, PACT (Personal Agent Consent & Trust Protocol)
Date drafted: 2026-10-06, 8:18 PM WAT
Target: https://www.linkedin.com/in/thejessezhang/ (CEO/Co-founder, Decagon, $4.5B)
Post: Open-sourcing PACT with Instinct. Personal agent contacts a business to cancel an order or change a booking; business must verify who it represents and what the customer approved. Customers sign in directly with the business and grant specific permissions. Agent never handles credentials. Business policies still determine what's allowed. Built on A2A and OAuth. Joining Meta's Muse Personal Agent Protocol working group.
Post age when received: 13 minutes, edited. FRESH — top comment window open.

## WHY THIS MATTERS
- Jesse is Tier A #6 on the master connect list. This post is the single best moment to engage him all month.
- PACT = consent + permissions + verification for agents. That is literally Timothy's red team lane applied to a protocol launch.
- Founder launching a standard publicly = he is watching the comments closely for the first hours.

## COMMENT (paste this)
The consent layer is the right place to fix this. The failures I find happen after the door opens though.

Three things PACT will get tested on: scope, revocation, and the audit trail. Does a customer's grant narrow to what they actually intended, or does it inherit whatever the business agent can reach? What happens when consent is revoked mid-action, after a tool call already fired? And when something goes wrong, can anyone prove what was approved, by whom, and when?

The interesting attack is not forged consent. It is real consent for a scope the customer misunderstood. The protocol works perfectly and the customer still loses.

Getting that right at the protocol layer is worth more than any guardrail prompt.

## UPDATED CONNECTION NOTE (send right after the comment)
```
Jesse, PACT is the right shape: consent at the protocol layer instead of prompt level. I red team agent permissions from Lagos, and this is where the real failures live. - T
```
(162 chars, under the 200 cap, ends with "- T", asks for nothing)
NOTE BUDGET: this would be note #2 of the month if Felix and Henry went out, or #3. Check the quota tracker before sending. If out of notes: send BLANK, the comment carries the context.

## WHY IT WORKS
1. Praises the architecture, then adds three failure modes he did not mention (scope, revocation, audit).
2. "Real consent for a scope the customer misunderstood" — A2A and OAuth solve identity, not intent scope. This is the insight.
3. "The protocol works perfectly and the customer still loses" is the quotable.
4. "Worth more than any guardrail prompt" aligns with his thesis, so the critique reads as support.

## ASSET SPIN-OFFS
- Article candidate: "Consent is not control: what PACT-style protocols still miss." Scope narrowing, mid-action revocation, approval audit trails. Pairs with the agent/MCP articles.
- Card candidate: "The protocol works perfectly and the customer still loses."
- Micro post candidate: real consent for a misunderstood scope, as a standalone observation.
- This thread is also evidence for the micro1 Zara interview: agent permission design is exactly what they score on "LLM & AI Agent Engineering."

## STATUS
- Comment: drafted, pending paste (URGENT — post is minutes old)
- Note: drafted, send immediately after comment
- Reply handling: PENDING
