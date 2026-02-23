---
layout: default
title: Home
nav_order: 1
description: "Framework-driven PM skills that produce artifacts you cannot create unaided"
permalink: /
---

# PM Skills Arsenal

AI produces polished analysis that changes no decisions. These skills fix that.

> *Process guides raise the floor. Knowledge weapons raise the ceiling.*

---

## Why This Exists

When you load a skill, the cheapest model beats the best model without it.

| Condition | Score | vs. Baseline |
|---|---|---|
| Baseline (Claude, no skill) | 47 / 105 | — |
| Anthropic's PM Skill (methodology) | 81 / 105 | +72% |
| **PM Skills Arsenal (codex)** | **98 / 105** | **+109%** |

Benchmark: 5 prompts × 7 dimensions × 3 conditions. Full methodology and outputs in [`benchmark/`](https://github.com/Avyayalaya/pm-skills-arsenal/tree/main/benchmark).

The gap isn't model quality — it's encoded knowledge. Raw prompting produces generic analysis. Skill-loaded agents produce structured frameworks with evidence tiers, confidence calibration, and outputs that hold up to scrutiny.

---

## Install (Claude Code)

```bash
claude plugin marketplace add avyayalaya/pm-skills-arsenal
claude plugin install pm-skills@avyayalaya
```

Skills auto-activate when you ask Claude to do anything in their domain. No slash commands needed.

### GitHub Copilot

Reference skill files with `#` in Copilot Chat or Copilot CLI. Full setup guide: **[GitHub Copilot Installation](docs/github-copilot-install.html)**

**Other AI tools (ChatGPT, Cursor, Gemini):**
Copy the relevant `SKILL.md` directly into your context window.

---

## Skills

### [Competitive & Market Analysis](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/competitive-market-analysis/SKILL.md)

Structural assessment of who wins, why, and what to do about it. Scores competitive advantages by durability, decomposes switching costs by type, flags disruption vectors, and surfaces contradictions between frameworks instead of papering over them. Every recommendation carries an evidence tier and a confidence level.

Market entry · competitive response · moat assessment · build/buy/partner

### [Metric Design & Experimentation](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/metric-design-experimentation/SKILL.md)

Measurement systems that hold up under pressure. Builds metric hierarchies with leading/lagging pairs and counter-metrics, designs experiments with statistical rigor, and diagnoses the four ways metrics get gamed before it happens to yours.

North Star selection · experiment design · retention cohorts · metric gaming diagnosis

### [Specification Writing](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/specification-writing/SKILL.md)

Specs complete enough that the executor — engineer, AI agent, contractor — starts building without asking a single clarifying question. Outcome-anchored, with explicit scope boundaries, acceptance criteria by type, and failure conditions designed in from the start.

Feature specs · API contracts · agent task specs

### [Problem Framing](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/problem-framing/SKILL.md)

Decomposes vague problem areas into evidence-graded problem statements before anyone starts building. Root cause analysis, opportunity sizing, constraint mapping, and stakeholder impact — all with confidence levels so you know what's validated and what's still a guess.

Problem decomposition · opportunity sizing · stakeholder alignment · prioritization

### [Discovery & Research](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/discovery-research/SKILL.md)

Research synthesis that separates what users say from what they do. Grades every source by evidence quality, surfaces contradictions between data types, identifies where your evidence is dangerously thin, and maps the gaps that should drive your next research cycle.

Interview synthesis · evidence grading · stated vs. revealed · research gap analysis

### [Narrative Building](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/narrative-building/SKILL.md)

Strategic narratives that make a product feel inevitable — not by assertion but by structural argument. Positioning analysis, audience-adapted variants, evidence-integrated claims, pre-embedded objection responses, and a testing protocol that validates the story before it goes live.

Product positioning · launch narratives · internal alignment · stakeholder pitches

---

## See It In Action

- **[Figma vs Canva vs Adobe Express](docs/use-case-figma-canva-express.html)** — Who wins the design tools war and why Canva's enterprise play changes the answer
- **[M365 Copilot Adoption](docs/use-case-metric-design.html)** — How to measure whether a $30/user AI copilot is actually delivering value
- **[AI Chat Interface Spec](docs/use-case-specification.html)** — A spec for a ChatGPT-style interface complete enough that an engineer starts building without questions
- **[Notion's Growth Plateau](docs/use-case-problem-framing.html)** — Why Notion's growth stalled and which of 12 root causes actually matter
- **[Superhuman vs Gmail](docs/use-case-discovery-research.html)** — What users say they want from email vs what their behavior reveals
- **[Cursor's Positioning](docs/use-case-narrative-building.html)** — How Cursor positioned itself against GitHub Copilot and VS Code in a market Microsoft owns

**Multi-skill case studies:**
- **[Art Gallery Expansion](docs/case-study-art-gallery.html)** — A solopreneur decides whether to open a second location, from problem framing through final spec
- **[Meditation App Engagement](docs/case-study-meditation-app.html)** — A growth PM diagnoses why 30-day retention is falling, across 5 skills end-to-end

---

MIT · [Parth Sangani](https://github.com/avyayalaya)
