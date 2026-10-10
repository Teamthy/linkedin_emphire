# Comment draft — Tanya Janca, "is your agent a security boundary?" post
Date drafted: 2026-10-06, 10:19 PM WAT
Target: https://www.linkedin.com/in/tanya-janca/
Who: We Hack Purple founder, Head of Education/Community at Semgrep, best-selling author of "Alice and Bob Learn Application Security" and secure coding trainer. Tier C #35 on the master connect list.
Post (posted "now"): "If your AI agent did something it wasn't supposed to do tomorrow, would you even know? And if someone asked you to explain what happened three months later, could you?" What systems, what credentials, what data, what stopped it. "Telling your agent to behave itself is not a security boundary." Containment, least privilege, scoped credentials, meaningful logging, actual security requirements. Government investigation into OpenAI mentioned. "AI agents are software. We need to start treating them that way."
Post age when received: FRESH (minutes). Top-comment window open.

## COMMENT (paste this)
The three-months-later question is the one that exposes most teams. Everyone logs what the agent did. Almost nobody records what it was allowed to do at that moment.

Permissions drift. A tool gets added on a Tuesday. A service account gets widened for a debugging session and never narrowed back. So when you reconstruct the incident months later, you can see the action but not the boundary that should have stopped it.

The other thing my own testing keeps turning up: an agent does not get its own permissions, it inherits the service account's. If that credential can reach the table, the agent can act on it. That inheritance is almost never written down anywhere.

"Telling your agent to behave itself is not a security boundary" is the cleanest version of this I have read.

## WHY IT WORKS
1. She opens with a question and closes with a principle. This answers the question with what she did not say: log the permission surface, not just the actions.
2. "You can see the action but not the boundary that should have stopped it" is the quotable.
3. Permissions drift is concrete and universally true (the widened service account that never got narrowed back).
4. Closes on HER line, which is specific praise of the sentence, not the person.
5. Zero pitch, no link, no ask.

## CONNECTION STRATEGY
- **Hold the note.** She is very active and replies to substantive comments. A reply makes a BLANK request sufficient and saves October note quota (which is nearly spent).
- **If she replies: send the blank request immediately.**
- If no reply in 2 days, send the drafted note from the master list:
```
Tanya, Alice and Bob made AppSec click for me as a developer. I run AI red teaming from Lagos now, and your teaching style is the one I copy in my own writing. - T
```
- Long game: We Hack Purple community is full of developers learning security, exactly Timothy's audience. Comment on her posts monthly.

## PATTERN NOTE (third instance in one evening)
Tonight produced three comments on the SAME underlying argument:
1. Jesse Zhang PACT post — consent is not control; scope, revocation, audit
2. Adrian Sanchez draft — capture is visible, retention is not
3. Tanya Janca — the prompt is not a boundary; log the permission surface
Different people, different posts, one position: **the permission and audit layer is where the real risk lives, and it is the least tested part of any AI system.**
Action: name this as a frame in the Breaking AI series ("the invisible layer"). It is genuinely Timothy's own position, arrived at independently three times in one night.

## ASSET SPIN-OFFS
- Article candidate: "Log the boundary, not just the action" — permission-surface logging for agents.
- Card candidate: "Telling your agent to behave itself is not a security boundary." (quote, credited to Tanya)
- Micro post candidate: the three-months-later reconstruction problem.
- Zara interview evidence: agent permission inheritance is exactly the "LLM & AI Agent Engineering" focus area.

## STATUS
- Comment: drafted, pending paste (URGENT — fresh post)
- Note: HOLD, send only if she replies
- Reply handling: PENDING
