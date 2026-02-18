# PM Skills Arsenal

> **Knowledge weapons for product managers.** Not templates. Not checklists. Deep analytical frameworks encoded into AI skill files that produce outputs you can't get from raw prompting.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-1%20of%206-blue)
![Benchmark Tested](https://img.shields.io/badge/benchmark-tested%20across%203%20models-orange)

---

## Why This Exists

AI models are smart. But they don't naturally apply strategic frameworks, tier their evidence, or calibrate their confidence. They produce reasonable-sounding analysis that a senior PM could have written from memory.

**Skill files change that.** They encode domain-specific intellectual ammunition — 7 Powers scoring, disruption vector analysis, moat decomposition, evidence tiering — so that any AI agent produces output at the "$500K strategy engagement" quality tier.

The difference isn't marginal. It's measured.

---

## Benchmark: Proof, Not Claims

We tested our skill against raw prompting and an existing PM skill ([Dean Peters' company-research](https://github.com/deanpeters/Product-Manager-Skills)) across 3 models (Claude Sonnet 4, GPT-5.1, Claude Haiku 4.5) on a real competitive analysis problem.

### Results (Average Across 3 Models)

| Dimension | PM Skills Arsenal | Raw Prompting | Existing PM Skill | Ours vs. Raw |
|-----------|:-:|:-:|:-:|:-:|
| **Framework Depth** | **8.7** | 5.3 | 4.0 | +64% |
| **Artifact Quality** | **9.0** | 6.3 | 5.3 | +43% |
| **Actionability** | **8.0** | 6.3 | 4.7 | +27% |
| **Evidence Rigor** | **8.7** | 3.7 | 3.7 | **+135%** |
| **Novel Insight** | **8.0** | 4.7 | 3.3 | +70% |
| **TOTAL (/50)** | **42.3** | 26.3 | 21.0 | **+61%** |

```
                    PM Skills Arsenal    Raw Prompting    Existing PM Skill
                    ─────────────────    ─────────────    ─────────────────
Claude Sonnet 4          43/50              25/50              20/50
GPT-5.1                  46/50              28/50              25/50
Claude Haiku 4.5         38/50              26/50              18/50
                    ─────────────────    ─────────────    ─────────────────
Average                  42.3               26.3               21.0
```

**Key finding:** Evidence rigor is where skill files matter most (+135%). Models don't naturally tier their evidence or calibrate confidence. The skill forces this behavior — every claim gets an evidence tier tag, every recommendation gets a confidence percentage.

**Cross-model portability:** The cheapest model (Haiku 4.5) with our skill (38/50) outperformed the best model (GPT-5.1) raw (28/50) by 36%. Encoded frameworks raise the floor for all models.

> 📊 Full benchmark methodology, per-model breakdown, and dimension-by-dimension analysis: [`skills/competitive-market-analysis/benchmark/`](skills/competitive-market-analysis/benchmark/README.md)

---

## The Difference: Before and After

**Without skill (raw prompting):**
> "Figma has strong switching costs." *(No decomposition, no evidence tier, no confidence level.)*

**With PM Skills Arsenal:**
> **Switching Cost Decomposition — Figma:**
> | Cost Type | Strength | Evidence |
> |-----------|----------|----------|
> | Procedural | 🟢 High | 📊 [Tier 1] Teams have built muscle memory around Figma workflows |
> | Data | 🟢 High | 📊 [Tier 1] Design systems, component libraries are customer-created assets |
> | Relational | 🟡 Medium | [Tier 3] Stakeholder commenting creates organizational dependency |
> | Financial | 🔴 Low | [Tier 4] Per-seat pricing is competitive, no lock-in premium |
>
> *Moat classification: Customer-CREATED switching costs (data + procedural), not vendor-imposed. Durability: HIGH — these assets compound over time.* Confidence: 80%

The skill doesn't just produce more text. It produces **structured analytical artifacts** with evidence tiers, confidence calibration, and decomposed frameworks a PM can present to their VP without editing.

---

## Available Skills

| # | Skill | What It Does | Status |
|---|-------|-------------|--------|
| 1 | [**Competitive & Market Analysis**](skills/competitive-market-analysis/) | Score competitors against 7+ strategic frameworks. Produce a Competitive War Map with evidence-graded confidence. | ✅ Shipped |
| 2 | **Metrics & Experimentation** | Design metric hierarchies, run experiment design, detect Goodhart's Law, validate statistical significance. | 🔜 Next |
| 3 | **Problem Framing** | Decompose ambiguous problems into testable questions using first-principles reasoning. | 📋 Planned |
| 4 | **Discovery & Research** | Synthesize research evidence with quality tiers and confidence calibration. | 📋 Planned |
| 5 | **Narrative Building** | Build strategic narratives using Minto Pyramid, SCQ-A, and positioning frameworks. | 📋 Planned |
| 6 | **Specification Writing** | Write zero-question specs where no clarifying questions remain. | 📋 Planned |

Each skill is a **knowledge weapon** — it encodes domain frameworks with scoring rubrics and decision tables, not just references or checklists. The difference: knowledge weapons change the *ceiling* of what's possible. Process guides change the *floor*.

---

## Quick Start

### Option 1: Copy into context (works anywhere)

Copy the contents of [`skills/competitive-market-analysis/SKILL.md`](skills/competitive-market-analysis/SKILL.md) into any AI agent's context window. Works with Claude, ChatGPT, Gemini, Copilot, Cursor, Codex — any model, any platform.

### Option 2: Clone the repo

```bash
git clone https://github.com/avyayalaya/pm-skills-arsenal.git
```

Then load the skill file into your agent:
```
Load the file skills/competitive-market-analysis/SKILL.md and follow its methodology.
```

### Option 3: Claude Code / Copilot CLI

Place the skill in your project's `.github/skills/` directory or load directly:
```
@skill competitive-market-analysis
```

### Using the scripts (optional)

```bash
cd skills/competitive-market-analysis
pip install -r requirements.txt
python scripts/market_sizing.py --help
python scripts/competitive_scorer.py --help
```

Scripts provide deterministic calculations (market sizing arithmetic, 7 Powers scoring matrices). The skill works without them — they add precision for computation-heavy steps.

---

## How Skills Work

Each skill follows a consistent structure:

```
skills/
  competitive-market-analysis/
    SKILL.md              # The knowledge weapon — load this into your agent
    manifest.yaml         # Metadata for marketplace discovery
    README.md             # Quick reference
    requirements.txt      # Python dependencies (if scripts exist)
    examples/
      sample.md           # Full worked example
    scripts/
      market_sizing.py    # Deterministic computation helpers
      competitive_scorer.py
    benchmark/
      README.md           # Head-to-head benchmark results
```

**SKILL.md** contains:
- **Purpose** — when to use, when not to use
- **Input Contract** — what you need to provide
- **Domain Frameworks** — encoded with scoring rubrics, not just referenced
- **Quality Gradients** — intern → consultant → elite tiers
- **Failure Modes** — named patterns with detection and prevention
- **Worked Example** — realistic case at consultant tier
- **What's Next** — chain interface to other skills

---

## Quality Philosophy

**Knowledge weapons, not process guides.**

A process guide tells you the steps. A knowledge weapon encodes the domain frameworks you'd need hours to research — 7 Powers scoring, Aggregation Theory classification, switching cost decomposition by type, disruption vector analysis — and makes them available in every analysis.

The test: **can a PM produce this output without the skill file?** If yes, it's a template. If no, it's a knowledge weapon.

Every skill in this repo passes that test. The [benchmark data](skills/competitive-market-analysis/benchmark/README.md) proves it empirically.

---

## Roadmap

- [x] Competitive & Market Analysis (shipped, benchmarked)
- [ ] Metrics & Experimentation
- [ ] Problem Framing
- [ ] Discovery & Research
- [ ] Narrative Building
- [ ] Specification Writing
- [ ] Cross-skill benchmark (3 problems × 3 approaches × 3 models)
- [ ] MCP server for universal agent discovery

---

## Contributing

This repo is MIT licensed. Contributions welcome:

- **Use a skill and share results** — file an issue with what worked and what didn't
- **Report quality gaps** — if a framework is under-applied or a failure mode is missing
- **Suggest new skills** — file an issue with the PM task, why raw prompting isn't enough, and what frameworks should be encoded

---

## License

[MIT](LICENSE) — use commercially, modify, redistribute. No restrictions.

---

*Built by [Parth Sangani](https://www.linkedin.com/in/parthsangani/) — Principal PM at Microsoft, building AI systems that understand context at scale.*
