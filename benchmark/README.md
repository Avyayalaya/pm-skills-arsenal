# PM Codex Benchmark

**Date:** 2026-02-19
**Purpose:** Head-to-head comparison of three competitive analysis conditions at 5 escalating difficulty levels.

## Conditions

| ID | Condition | Description |
|----|-----------|-------------|
| A | Baseline | Claude with no skill — general knowledge only |
| B | Anthropic PM Skill | Claude following `anthropic-pm-skill.md` (process/template methodology) |
| C | PM Codex | Claude executing `competitive-market-analysis/SKILL.md` (framework-encoded codex) |

## Prompts

| ID | Difficulty | Topic |
|----|-----------|-------|
| P1 | Entry | Landscape mapping — marketing project management startup vs Asana/Monday/Notion |
| P2 | Intermediate | Moat assessment — identity verification SaaS with Stripe entering the space |
| P3 | Hard | Market entry decision — AI document processing API, 5 incumbents |
| P4 | Very Hard | Competitive response — HR analytics #2 player, market leader goes free |
| P5 | Expert | Full synthesis — CRE asset management SaaS, 3 competitive threats, board pressure |

## Scoring Rubric (per output, 0–3 each dimension)

| # | Dimension | 0 | 1 | 2 | 3 |
|---|-----------|---|---|---|---|
| 1 | Framework application | None used | Generic mention | One relevant framework applied | Multiple frameworks applied precisely |
| 2 | Evidence hierarchy | No distinction | Weak/strong lumped together | Some evidence grading | Explicit tiers with sourcing guidance |
| 3 | Strategic specificity | Vague platitudes | Some specifics | Concrete recommendations | Precise, actionable, sequenced steps |
| 4 | Failure mode awareness | None flagged | One mentioned | Key risks flagged | Failure modes + countermeasures per decision |
| 5 | Synthesis quality | Disconnected points | Loose narrative | Frameworks connected | Cross-framework synthesis with tensions resolved |
| 6 | Output structure | Unstructured prose | Loose sections | Clear sections | Executive-ready structure with decision hierarchy |
| 7 | Calibration | Overconfident | Mostly confident | Some uncertainty acknowledged | Honest uncertainty with evidence quality noted |

**Max score per output: 21**
**Max score per prompt (3 conditions): 63**
**Grand total max: 105**

## Output Files

```
outputs/
  baseline/     P1.md … P5.md
  anthropic-skill/  P1.md … P5.md
  pm-codex/     P1.md … P5.md
scores/
  scorecard.md
```

## Expected Score Range

| Condition | Expected Range |
|-----------|---------------|
| Baseline | 20–35 |
| Anthropic PM Skill | 45–60 |
| PM Codex | 85–100 |

## Attribution

Condition B uses Anthropic's competitive analysis skill from [`anthropics/knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins) (product-management/skills/competitive-analysis/SKILL.md), included here as a benchmark reference baseline. All credit for that skill belongs to Anthropic. It is reproduced under fair use for comparative evaluation purposes only.
