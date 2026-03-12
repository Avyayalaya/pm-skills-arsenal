# PM Skills Arsenal

**Knowledge weapons for product managers.** Deep analytical frameworks encoded into AI skill files that produce outputs a PM cannot create unaided.

> *Process guides raise the floor. Knowledge weapons raise the ceiling.*

---

## Why This Exists

When you load a skill, the cheapest model beats the best model without it.

| Condition | Score | vs. Baseline |
|---|---|---|
| Baseline (Claude, no skill) | 47 / 105 | — |
| Anthropic's PM Skill (methodology) | 81 / 105 | +72% |
| **PM Skills Arsenal (codex)** | **98 / 105** | **+109%** |

Benchmark: 5 prompts × 7 dimensions × 3 conditions. Full methodology and outputs in [`benchmark/`](benchmark/).

The gap isn't model quality — it's encoded knowledge. Raw prompting produces generic analysis. Skill-loaded agents produce structured frameworks with evidence tiers, confidence calibration, and outputs that hold up to scrutiny.

---

## Install (Claude Code)

```bash
claude plugin marketplace add avyayalaya/pm-skills-arsenal
claude plugin install pm-skills@avyayalaya
```

Skills auto-activate when you ask Claude to do anything in their domain. No slash commands needed.

**Manual load (any AI — Claude, ChatGPT, Cursor, Copilot):**
Copy the relevant `SKILL.md` directly into your context window.

---

## Skills

12 codex skills covering the full PM lifecycle — from analysis through strategy, communication, and influence.

### Analysis & Research

| Skill | What it produces | Frameworks encoded |
|---|---|---|
| [**Competitive & Market Analysis**](skills/competitive-market-analysis/SKILL.md) | Competitive War Map — moat scoring, positioning, competitive response strategy | 7 Powers, Aggregation Theory, Christensen Disruption/COAP, Roger Martin, Wardley Mapping, JTBD, Data Content Loops, Blue Ocean, Crossing the Chasm, Win/Loss |
| [**Discovery & Research**](skills/discovery-research/SKILL.md) | Evidence-graded research synthesis with signal classification | Evidence Triangulation, Interview Analysis, Research Quality Assessment, Signal vs Noise, Insight Classification, Demand-Side Analysis, Research Gap Mapping, Competitive Discovery |
| [**Problem Framing**](skills/problem-framing/SKILL.md) | Structured problem definition with opportunity sizing | Problem Definition Canvas, 5 Whys, JTBD Problem Framing, Opportunity Sizing, Problem-Solution Fit, Constraint Map, Stakeholder Impact Matrix, ICE/RICE |

### Definition & Measurement

| Skill | What it produces | Frameworks encoded |
|---|---|---|
| [**Specification Writing**](skills/specification-writing/SKILL.md) | Zero-Question Specification — a spec so complete any executor starts without asking a single clarifying question | Outcome-First Methodology, Acceptance Criteria Taxonomy, Scope Boundary Protocol, Executor Context Model, Failure Condition Design, Ambiguity Resolution Framework |
| [**Metric Design & Experimentation**](skills/metric-design-experimentation/SKILL.md) | Measurement Framework — metric hierarchy, leading/lagging pairs, counter-metrics, experiment plans, retention cohorts | NSM + Decomposition Tree, Leading/Lagging Indicators, Goodhart's Law (4 variants), Experiment Design, Statistical Validity, Retention Cohort Methodology, Multi-Armed Bandit, HEART, PMF Measurement |

### Strategy & Planning

| Skill | What it produces | Frameworks encoded |
|---|---|---|
| [**Product Strategy**](skills/product-strategy/SKILL.md) | Strategic product roadmap with confidence-rated bets, option-value sequencing, and explicit deprioritization | Vision-to-Roadmap Cascade, Strategic Bet-Sizing, Option-Value Sequencing, Strategic Tension Surfacing, NOT-Doing Section, Resource Allocation, Roadmap Communication |
| [**Go-to-Market Strategy**](skills/go-to-market-strategy/SKILL.md) | GTM strategy document with wedge identification, channel unit economics, and launch gating | Market Entry Thesis, Segment Selection & ICP Scoring, Channel Strategy with Unit Economics, Launch Sequencing & Gating, Competitive Positioning (Dunford), Success Metrics & Failure Criteria, Distribution & Growth Mechanics |
| [**Pricing & Packaging**](skills/pricing-packaging/SKILL.md) | Pricing recommendation with model selection, WTP assessment, competitive pricing map, and sensitivity analysis | Pricing Model Selection, WTP Assessment (Van Westendorp, Gabor-Granger, Conjoint), Competitive Pricing Map, Good/Better/Best Package Architecture, Sensitivity Analysis, Revenue Impact Modeling, AI/SaaS-Specific Patterns |

### Communication & Influence

| Skill | What it produces | Frameworks encoded |
|---|---|---|
| [**Executive Writing**](skills/executive-writing/SKILL.md) | Executive-ready documents — strategy one-pagers, board memos, decision briefs — with role-calibrated framing | Minto Pyramid / SCR, Format Routing (3 document types), Audience Calibration by Role, Decision Architecture, Zero-Jargon Compression, Ask Framing, Evidence Cascade, Document Quality Gate |
| [**Narrative Building**](skills/narrative-building/SKILL.md) | Positioning narrative with audience adaptation and competitive narrative analysis | Narrative Arc, Positioning (Dunford), Why Now, Audience Adaptation, Evidence-Narrative Integration, Objection Anticipation, Competitive Narrative Analysis, Narrative Testing |
| [**Multi-Channel Publishing**](skills/multi-channel-publishing/SKILL.md) | Channel-specific content derivatives — LinkedIn posts, conference abstracts, spoken scripts, podcast briefs | Channel Format Taxonomy, 7-Step Compression Protocol, Hook Adaptation by Channel, Evidence Density Calibration, Audience Context Matching, Source Fidelity Verification, Spoken Script Derivation |
| [**Stakeholder Alignment**](skills/stakeholder-alignment/SKILL.md) | Stakeholder alignment strategy with influence mapping, coalition analysis, and sequenced alignment plan | Power-Interest-Position Matrix, Coalition Analysis, Decision Archaeology, Alignment Sequencing, Objection Pre-emption, Communication Strategy by Stakeholder, Alignment Monitoring & Recovery |

---

## What Makes These Different

Most PM skill libraries are process guides: templates, checklists, step-by-step procedures. They help you follow a process you already know.

These are codices: domain knowledge encoded as scoring rubrics, decision tables, and output templates. They give the AI the expert frameworks it needs to reason at a higher level — frameworks a strong PM has internalized over years of practice.

| | Process guide | Codex (this repo) |
|---|---|---|
| What it encodes | How to follow a process | What an expert knows |
| Output when loaded | Structured template | Frameworks applied with expert judgment |
| Value when you already know the process | Low | High — deeper frameworks than most practitioners hold |
| Model dependency | Higher | Lower — cheap models produce strong output |

**Every skill in this repo:**
- Is 1,000–1,300 lines of encoded domain knowledge, not a template
- Includes scoring rubrics with explicit 0–3 criteria (not "good / bad" — observable signals at each level)
- Includes decision tables mapping conditions to actions
- Includes Quality Gradients (Intern / Consultant / Elite tier) so you can self-evaluate output
- Includes ≥5 Failure Modes with detection signals and corrections
- Includes Mandatory Output Sections — Assumption Registry, Adversarial Self-Critique, Revision Triggers — that make elite-tier output the default

---

## Design Principles

**Take positions, use confidence levels.** No weasel words. Every conclusion carries H / M / L confidence (>70% / 40–70% / <40%). Calibrated uncertainty is more useful than false confidence.

**Evidence-tiered claims.** Every substantive claim carries an inline evidence tier. T2 (validated in your own data) carries different weight than T4 (industry benchmark) or T6 (inferred from first principles).

**Adversarial self-critique is mandatory.** Every output includes ≥3 genuine weaknesses argued against the analysis as forcefully as possible. Outputs that haven't been stress-tested fail at the worst moment.

**Framework selection before application.** Every skill has a Step 0 routing table that maps question type to the 3–5 load-bearing frameworks to apply. Applying all frameworks to every question inflates output without improving decisions.

**MIT license.** Commercial use permitted. Fork, adapt, integrate.

---

## Usage Examples

**Competitive analysis:**
> "We're evaluating whether to enter the SMB HR analytics market. Our current ICP is mid-market. Use the competitive market analysis skill to assess the strategic landscape."

**Product strategy:**
> "Build a 6-month product roadmap for our AI writing assistant. We have 3 engineers and need to decide between improving the editor, adding collaboration, or building an API."

**Executive writing:**
> "I need a strategy one-pager for our VP of Product recommending we invest in a developer platform. Here's the data: [paste]."

**Go-to-market:**
> "We're launching a pricing analytics tool for e-commerce. Help me build the GTM strategy — who to target first, which channels, and what the launch sequence looks like."

**Stakeholder alignment:**
> "I need to get 4 VPs aligned on migrating to a new data platform. Engineering VP is supportive, Finance VP is skeptical, Product VP is neutral, Design VP hasn't engaged."

**Pricing:**
> "We're redesigning our pricing from flat-rate to usage-based for our AI API product. Current price is $99/mo. Help me think through the model, packaging, and migration."

---

## Benchmark Methodology

Head-to-head: 5 prompts at escalating difficulty × 7 scoring dimensions × 3 conditions (baseline, Anthropic PM Skill, PM Skills Arsenal).

**Scoring dimensions (0–3 each, 105 max):**
D1 Framework application · D2 Evidence hierarchy · D3 Strategic specificity · D4 Failure mode awareness · D5 Synthesis quality · D6 Output structure · D7 Calibration

**Publication threshold:** ≥90/105 (85.7%) required. Current score: **98/105 (93.3%)**.

Full outputs and scorecard: [`benchmark/`](benchmark/)

---

## Repo Structure

```
pm-skills-arsenal/
  .claude-plugin/
    plugin.json           ← plugin identity
    marketplace.json      ← enables claude plugin install
  skills/
    competitive-market-analysis/   ← Analysis & Research
    discovery-research/
    problem-framing/
    specification-writing/         ← Definition & Measurement
    metric-design-experimentation/
    product-strategy/              ← Strategy & Planning
    go-to-market-strategy/
    pricing-packaging/
    executive-writing/             ← Communication & Influence
    narrative-building/
    multi-channel-publishing/
    stakeholder-alignment/
  benchmark/              ← head-to-head benchmark (all 3 conditions + scorecard)
  README.md
  LICENSE                 ← MIT
```

---

## Contributing

High quality bar. Before contributing a new skill:

1. Read the skill building standards (encoding patterns, format rules, benchmarking methodology) — link in Wiki
2. Run a head-to-head benchmark: baseline vs. your skill, 5 prompts, 7 dimensions
3. Score ≥90/105 before submitting a PR

PRs that add frameworks to existing skills, fix factual errors, or improve worked examples are welcome without the full benchmark requirement.

---

## License

MIT — use commercially, fork freely, attribution appreciated but not required.

---

*Built by [Parth Sangani](https://github.com/avyayalaya)*
