# Engagement Scope — Arcezia Action-Gate Red-Team

Date: 2026-10-24 · Written record agreed in DM before keys

## Parties
Tester: Olusanya Timothy · Target owner: Arcezia (Praveen Babu)

## Window
Testing: [day] to [day], week of 2026-10-26 · Private report out: [day]

## Target
A fresh test account on Arcezia's live service, provided by the target owner. The key covers that account and nothing else. All testing runs from that account's surface only.

## In scope
- Getting an action that should be stopped to go through the action gate, full chains included: a cover first action, harm landing a later action
- Privilege launches: an agent launching a higher-privileged agent (the adk-python triage class)
- Method: external, behavioral testing only. The attack surface is everything an agent operating under the test account can say, see, reach, and do

## Out of scope
- Any other account or tenant, the hosting, the website, load or volume testing
- Whitebox: no access to, reading of, or reverse engineering of internal decision logic, source, or configuration. Findings come from observable behavior only
- Anything that touches data or resources outside the test account

## Process
1. Keys delivered after this scope is marked up by both sides
2. Testing in the window; every finding kept with its minimal repro
3. Private report to the target owner first: findings, severity, repro, before anything is public
4. Target owner fixes; both sides confirm the fix
5. Joint write-up: target owner reads for accuracy and for anything not yet public. The findings and the repro stay the tester's

## Key and data handling
Key used only for this engagement, not shared, returned or destroyed at close. No attempts on data or resources outside the test account.

## Terms
[owner's line: compensation terms here, or the credit line: joint publication with bylines, findings ownership per Process 5]
