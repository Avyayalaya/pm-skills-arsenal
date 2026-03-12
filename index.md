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

12 codex skills covering the full PM lifecycle — from analysis through strategy, communication, and influence.

### Analysis & Research

**[Competitive & Market Analysis](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/competitive-market-analysis/SKILL.md)** — Structural assessment of who wins, why, and what to do about it. 7 Powers, Aggregation Theory, Christensen Disruption, JTBD, Wardley Mapping, Blue Ocean, Crossing the Chasm, Win/Loss.

**[Discovery & Research](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/discovery-research/SKILL.md)** — Research synthesis that separates what users say from what they do. Evidence Triangulation, Interview Analysis, Signal vs Noise, Demand-Side Analysis, Research Gap Mapping.

**[Problem Framing](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/problem-framing/SKILL.md)** — Decomposes vague problem areas into evidence-graded problem statements. Problem Definition Canvas, 5 Whys, JTBD Problem Framing, Opportunity Sizing, Constraint Mapping, ICE/RICE.

### Definition & Measurement

**[Specification Writing](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/specification-writing/SKILL.md)** — Specs so complete the executor starts building without asking a single clarifying question. Outcome-First Methodology, Acceptance Criteria Taxonomy, Scope Boundary Protocol, Failure Condition Design.

**[Metric Design & Experimentation](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/metric-design-experimentation/SKILL.md)** — Measurement systems that hold up under pressure. NSM + Decomposition Tree, Leading/Lagging Indicators, Goodhart's Law, Experiment Design, Retention Cohort Methodology, HEART.

### Strategy & Planning

**[Product Strategy](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/product-strategy/SKILL.md)** — Strategic product roadmaps with confidence-rated bets, option-value sequencing, and explicit deprioritization. Vision-to-Roadmap Cascade, Strategic Bet-Sizing, NOT-Doing Section, Resource Allocation.

**[Go-to-Market Strategy](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/go-to-market-strategy/SKILL.md)** — GTM strategy with wedge identification, channel unit economics, and launch gating. Market Entry Thesis, ICP Scoring, Channel Strategy, Competitive Positioning (Dunford), Distribution Mechanics.

**[Pricing & Packaging](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/pricing-packaging/SKILL.md)** — Pricing recommendations with model selection, WTP assessment, and sensitivity analysis. Van Westendorp, Gabor-Granger, Good/Better/Best Architecture, Revenue Impact Modeling, AI/SaaS Patterns.

### Communication & Influence

**[Executive Writing](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/executive-writing/SKILL.md)** — Executive-ready documents — strategy one-pagers, board memos, decision briefs — with role-calibrated framing. Minto Pyramid / SCR, Format Routing, Audience Calibration, Decision Architecture, Zero-Jargon Compression.

**[Narrative Building](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/narrative-building/SKILL.md)** — Strategic narratives that make a product feel inevitable. Positioning (Dunford), Why Now, Audience Adaptation, Evidence-Narrative Integration, Objection Anticipation, Competitive Narrative Analysis.

**[Multi-Channel Publishing](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/multi-channel-publishing/SKILL.md)** — Channel-specific content derivatives from a source document. 7-Step Compression Protocol, Hook Adaptation, Evidence Density Calibration, Source Fidelity Verification, Spoken Script Derivation.

**[Stakeholder Alignment](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/stakeholder-alignment/SKILL.md)** — Stakeholder alignment strategy with influence mapping, coalition analysis, and sequenced alignment plan. Power-Interest-Position Matrix, Decision Archaeology, Objection Pre-emption, Alignment Monitoring & Recovery.

---

## See It In Action

Interactive showcases — full skill outputs with tabbed navigation, evidence tiers, and framework analysis.

### Analysis & Research
- **[Figma vs Canva vs Adobe Express](showcase/articles/use-case-figma-canva-express.html)** — Who wins the design tools war and why Canva's enterprise play changes the answer
- **[Superhuman vs Gmail](showcase/articles/use-case-discovery-research.html)** — What users say they want from email vs what their behavior reveals
- **[Notion's Growth Plateau](showcase/articles/use-case-problem-framing.html)** — Why Notion's growth stalled and which of 12 root causes actually matter

### Definition & Measurement
- **[AI Chat Interface Spec](showcase/articles/use-case-specification.html)** — A spec for a ChatGPT-style interface complete enough that an engineer starts building without questions
- **[M365 Copilot Adoption](showcase/articles/use-case-metric-design.html)** — How to measure whether a $30/user AI copilot is actually delivering value

### Strategy & Planning
- **[Async Video Platform AI Pivot](showcase/articles/use-case-product-strategy.html)** — 6-month roadmap for a Loom-like platform with AI bet-sizing and option-value sequencing
- **[PriceScope AI GTM](showcase/articles/use-case-go-to-market-strategy.html)** — Go-to-market for an AI pricing tool: ICP scoring, channel unit economics, launch gating
- **[CodeLens AI Pricing Redesign](showcase/articles/use-case-pricing-packaging.html)** — Flat-rate to usage-based: WTP analysis, Good/Better/Best tiers, migration strategy

### Communication & Influence
- **[DataVault Investment Brief](showcase/articles/use-case-executive-writing.html)** — Strategy one-pager for a $2M AI platform investment, role-calibrated for VP audience
- **[Cursor's Positioning](showcase/articles/use-case-narrative-building.html)** — How Cursor positioned itself against GitHub Copilot and VS Code in a market Microsoft owns
- **[AI Personalization Paradox](showcase/articles/use-case-multi-channel-publishing.html)** — Compressing a 3,200-word Substack into LinkedIn, conference abstract, and spoken script
- **[Data Platform Migration](showcase/articles/use-case-stakeholder-alignment.html)** — Aligning 4 VPs on a $3M Redshift-to-Databricks migration

---

MIT · [Parth Sangani](https://github.com/avyayalaya)
