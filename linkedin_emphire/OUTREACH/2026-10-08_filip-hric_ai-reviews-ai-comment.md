# Comment — Filip Hric, live "AI reviewing AI" session just ended (JUG Oberpfalz w/ Johannes Rabauer)
Date: Thu Oct 8, ~8:58 PM WAT | Filip posted thanks-clip 1 min ago → he's in reply-mode NOW, best window.
Session: Claude Code built Java feature live; Qodo Agentic Toolbox reviewed with team rules + codebase context; findings = real bug / fair point / false alarm, kept score. Qodo = AI code review company (Filip: QA/AI reliability, author). Audience: QA + eng leaders on AI reliability.
Context stat from thread: METR — open-source maintainers reviewed AI PRs that PASSED tests; ~half wouldn't merge.

## COMMENT (paste)
The number I'd watch from a night like this is not the real bugs. It is the false alarms. A reviewer that cries wolf gets ignored within two sprints, and then the one real catch drowns with everything else. The bar for an AI reviewer is not outsmarting the coder. It is being trusted enough that humans still read it.

Context injection is what moves that number. Team rules, architecture, what this repo has decided. That is the only thing separating a reviewer from an echo, the reviewer knows something the writer did not have.

My failure list from production AI has the same shape as your test failures. Reviewers audit against rules someone wrote. What breaks is usually what nobody wrote. Which tools it may call, which data it may touch, which commitments it may make. No rules file catches those, and tests pass around them like water.

## WHY
1. Right after the event, founders/reviewers answer every early comment — Filip just posted, in flow.
2. Re-frames the metric (false alarms, not catches) = the take Qodo's own engineers should care about; product-relevant, not fan noise.
3. "Reviewer vs echo = information asymmetry" is the quotable; lands the post's own premise sharper than the premise.
4. Last paragraph smuggles the red-team thesis (unwritten constraints) into the code-review debate — his whole brand in one paragraph, zero pitch.
5. Echoes his Gergely comment (review as style-check) — cross-thread consistency = becoming a named voice on AI reliability, not a random commenter.

## FOLLOW-UPS
- If session recording is public (JUG Oberpfalz on YouTube), watch 20 min before Article 2; "I watched two AI review each other live, here is the score nobody shows" = ready-made micro.
- Filip: peer/amplifier tier. No connection note left after Quivly's; if he replies, blank request Saturday.
- Johannes Rabauer (host, 2nd-degree): if his thread shows this comment, one like/comment back cheaply; JUG community = eng-leader reach.
