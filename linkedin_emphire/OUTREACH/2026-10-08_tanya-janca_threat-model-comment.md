# Comment draft — Tanya Janca, Shostack 4-question threat modeling post
Date: Thu Oct 8, 7:47 PM WAT | Post 6 min old. 3rd substantive touch with Tanya (Oct 6 boundary reply pending note decision, Oct 7 logged-comment play, this).
Post: Don't predict every weird agent behavior; threat model the system. Adam Shostack's 4 questions. Egress example: restrict it, monitor it, know when crossed. Turns "AI unpredictable" into ordinary security engineering.

## COMMENT (paste — plain text, no markdown)
This is the demystification that gets teams moving. One addition from the field: egress restriction misses the quietest exfil because it rides the approved channels. If the agent can fetch URLs, the fetch is the egress pipe. If it can render a markdown image, post a comment, or open a ticket, data leaves through doors you opened on purpose. The model is not knocking on the denied port. It is using the allowed one.

And question four, did we do a good job, has a nasty property in AI systems: the answer decays. One new tool, one widened service account, one prompt change, and the threat model you approved in September is a history document by October. So the only durable answer is a logged escape attempt in a sandbox, rerun after every meaningful change. Findings become permanent tests, not closed tickets.

## WHY
1. Adds the exfil-through-sanctioned-channels insight — real field knowledge, extends her own example (she covered denied egress; nobody covers egress that IS the feature).
2. Second paragraph weaponizes her question 4: decay + sandbox-proven answer = his regression-test thesis, on her framework. "History document by October" is the quotable.
3. Ends on "permanent tests, not closed tickets" — a line AppSec people will quote back.
4. Still zero pitch; third quality comment in her thread = her reply or the blank request both become natural next.

## NEXT
- If she replies: answer once, then BLANK connection request (note quota stays for buyers).
- Content note: "egress via approved doors" is a card line + a beat for the agent-permissions article (Article 7-9 region).
