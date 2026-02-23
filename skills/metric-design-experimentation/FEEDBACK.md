# Feedback Log: metric-design-experimentation

> **Purpose:** Track real-world usage, capture what works and what doesn't, drive systematic skill improvement. Every use case should be logged here with rating and learnings.

---

## Use Case Log

### UC-001: [Brief Title] (YYYY-MM-DD)

**User:** [parth | team-member-name]
**Rating:** ?/10
**Scenario:** [1-2 sentences: what business problem, what prompt, what context]

**What Worked:**
- [Specific framework or output that delivered value]
- [Another thing that worked well]

**What Didn't:**
- [Gap, missing framework, wrong question addressed, etc.]
- [Another issue]

**Evidence Quality:**
- Input evidence: [T1/T2/T3/T4/T5/T6 breakdown of what was available]
- Output confidence: [H/M/L distribution in recommendations]
- [Did thin evidence produce thin output as expected, or did skill hallucinate?]

**Action Taken:**
- [What was changed in the skill file, if anything]
- [OR: Logged for pattern confirmation across more uses]

**Status:**
- [ ] Logged only
- [ ] Skill updated
- [ ] Waiting for pattern (needs 2+ similar cases)

---

### UC-002: [Next use case]

...

---

## Improvement Backlog

**Patterns requiring >=2 confirming cases before encoding:**

| Pattern | First Seen | Confirming Cases | Action When Validated |
|---|---|---|---|
| [e.g., "Too many frameworks for activation questions"] | UC-001 | 1/2 | Add routing logic to Context Fitness Check: activation questions → max 3 frameworks |
| [e.g., "Missing customer evidence tier"] | UC-003 | 1/2 | Add app store reviews/G2/forums as T2 evidence source in Evidence Standards section |

---

## Validated Improvements (Shipped)

| Improvement | Driven By | Version | Date |
|---|---|---|---|
| Context Gate added | UC from M365 Copilot Mobile analysis | v1.3.0 | 2026-02-19 |
| Reader Navigation + Notation Key | UC from M365 Copilot Mobile (7/10 rating: expert-only output) | v1.3.0 | 2026-02-19 |

---

## Usage Stats

| Month | Uses | Avg Rating | Top Issue |
|---|---|---|---|
| 2026-02 | 2 | 7.5/10 | Too many frameworks (2/2 cases) |
| 2026-03 | ? | ? | ? |

---

*Logging protocol: After every real-world use of this skill (by you or team), add a UC entry. Rate honestly. 7/10 with clear gaps is more useful than 9/10 with no learnings.*
