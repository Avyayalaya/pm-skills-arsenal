# PM Skills Arsenal

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Deep PM frameworks encoded for AI agents.** Load a skill file into any model. Get structured analysis with evidence tiers, scoring rubrics, and confidence calibration — output a PM cannot produce unaided.

Works with Claude, ChatGPT, Copilot, Cursor, Codex, and any agent that accepts custom context.

---

## Why This Exists

Most PM skill files are process guides: "Step 1: Define scope. Step 2: Identify competitors." A senior PM already knows these steps. The file saves time but doesn't change what's possible.

This repo takes a different approach. Each skill is a **knowledge weapon** — it encodes domain frameworks (7 Powers scoring, Aggregation Theory, Christensen's disruption vectors, switching cost taxonomies, evidence tiering systems) with scoring rubrics and decision tables. When loaded into an agent, the skill produces analysis the PM could not reconstruct from memory in a single session.

**The distinction:** process guides raise the floor. Knowledge weapons raise the ceiling.

### Design Principles

Every skill in this repo must satisfy:

1. **The unaided test** — Run the PM problem WITHOUT the skill, then WITH. If the skill-loaded output contains frameworks, taxonomies, or analytical structures the PM couldn't produce from memory, those are the right frameworks to encode.
2. **The practitioner test** — Would a $500/hr strategy consultant use this specific framework for this problem type? If yes, encode it. If it's academic or theoretical, skip it.
3. **Agent-native design** — Skills are written for the agent to reason within frameworks, not for the PM to follow steps with AI assistance. The agent applies 7 Powers scoring. The PM reviews the output.

---

## Benchmark

Tested against raw prompting (no skill file) and [Dean Peters' PM Skills](https://github.com/deanpeters/Product-Manager-Skills) (42 skills, CC BY-NC-SA) across three models using the competitive analysis skill on a Figma evaluation.

| Dimension | PM Skills Arsenal | Raw Prompting | Delta |
|-----------|:-:|:-:|:-:|
| Framework Depth | **8.7** | 5.3 | +64% |
| Artifact Quality | **9.0** | 6.3 | +43% |
| Actionability | **8.0** | 6.3 | +27% |
| Evidence Rigor | **8.7** | 3.7 | **+135%** |
| Novel Insight | **8.0** | 4.7 | +70% |
| **Average (/10)** | **8.5** | 5.3 | **+61%** |

Per-model breakdown:

| Model | With Skill | Raw Prompting |
|-------|:-:|:-:|
| Claude Sonnet 4 | 43/50 | 25/50 |
| GPT-5.1 | 46/50 | 28/50 |
| Claude Haiku 4.5 | 38/50 | 26/50 |

Key finding: the cheapest model with the skill (Haiku, 38/50) outperformed the best model without it (GPT-5.1, 28/50). Encoded frameworks raise the floor across all models. The widest gap is evidence rigor (+135%) — models don't naturally tier evidence or calibrate confidence unless the skill forces it.

Full methodology: [`skills/competitive-market-analysis/benchmark/`](skills/competitive-market-analysis/benchmark/README.md)

### Before / After

**Raw prompting:**
> "Figma has strong switching costs."

**With skill loaded:**
> | Cost Type | Strength | Evidence |
> |-----------|----------|----------|
> | Procedural | 🟢 High | 📊 [Tier 1] Teams have built muscle memory around Figma workflows |
> | Data | 🟢 High | 📊 [Tier 1] Design systems, component libraries are customer-created assets |
> | Relational | 🟡 Medium | [Tier 3] Stakeholder commenting creates organizational dependency |
> | Financial | 🔴 Low | [Tier 4] Per-seat pricing is competitive, no lock-in premium |
>
> *Customer-CREATED switching costs (data + procedural), not vendor-imposed. Durability: HIGH — compounds over time.* Confidence: 80%

---

## Skills

Six skills mapped to the PM operating cycle. Each addresses a cognitive bottleneck where domain expertise dramatically changes output quality.

| # | Skill | PM Cycle Stage | Core Question | Status |
|---|-------|---------------|---------------|--------|
| 1 | [**Competitive & Market Analysis**](skills/competitive-market-analysis/) | Analyze | Who are we fighting and where do we win? | ✅ Shipped |
| 2 | **Metrics & Experimentation** | Evaluate | How do we know this worked? | 🔜 Next |
| 3 | **Problem Framing** | Decompose | What exactly are we solving and for whom? | Planned |
| 4 | **Discovery & Research** | Research | What does the evidence actually say? | Planned |
| 5 | **Narrative Building** | Position | What's the story that makes this inevitable? | Planned |
| 6 | **Specification Writing** | Define | What must be true when this ships? | Planned |

### What's Inside Each Skill

- **5+ named domain frameworks** with scoring rubrics or decision tables
- **Quality gradients**: intern → consultant → elite tier output
- **Named failure modes** with detection patterns and corrections
- **Worked examples** at elite tier demonstrating the quality bar
- **Evidence tiers** or confidence calibration methodology
- **Optional Python scripts** for computation-heavy steps (market sizing, scoring matrices)

### What's NOT Here (and Why)

- No user stories (templates, not knowledge weapons — Dean Peters covers this well)
- No RICE/ICE prioritization (procedural scoring, doesn't benefit from 700 lines of frameworks)
- No workshop facilitation (our audience is agents, not facilitators)
- No TAM/SAM/SOM calculator (useful but deterministic math, not a moat)

### Skill Chaining

Skills are 99% standalone — each works from raw context (a brain dump, a Slack thread, meeting notes). But each skill's output is structured to feed the next. The chain creates **progressive rigor**: the competitive map informs the narrative, the narrative constrains the spec, the spec defines what you measure. Each artifact inherits the discipline of the one before it.

```
Problem Framing → Discovery → Competitive Analysis → Narrative → Spec → Measurement
```

Orchestration hints are embedded in each skill's "What's Next" section. Smart models figure out chaining on their own. Weaker models get explicit guidance.

---

## How to Use

**Quickstart:** Copy [`SKILL.md`](skills/competitive-market-analysis/SKILL.md) into your agent's context window. That's it.

```bash
git clone https://github.com/avyayalaya/pm-skills-arsenal.git
```

**Optional scripts** for computation-heavy steps:
```bash
cd skills/competitive-market-analysis
pip install -r requirements.txt
python scripts/competitive_scorer.py --help
```

Scripts are deterministic helpers (math, scoring, validation) — not core skill logic. The SKILL.md is the knowledge weapon; the script is a tool it can invoke.

---

## Repo Structure

```
skills/
  competitive-market-analysis/
    SKILL.md              # The skill — load this into your agent
    manifest.yaml         # Metadata (name, version, tags, compatibility)
    README.md             # Quick reference
    requirements.txt      # Python dependencies for scripts
    examples/
      sample.md           # Full worked example at elite tier
    scripts/              # Computation helpers (optional)
    benchmark/            # Head-to-head evaluation results
```

Each new skill follows this structure. `manifest.yaml` uses ecosystem-standard format (name ≤64 chars, description ≤200 chars) for marketplace compatibility.

---

## Roadmap

- [x] Competitive & Market Analysis — 7 Powers, Aggregation Theory, disruption vectors, evidence-tiered war maps
- [ ] Metrics & Experimentation — metric hierarchies, experiment design, Goodhart's Law detection, statistical validity
- [ ] Problem Framing — Ishikawa, 5 Whys taxonomy, assumption grading, opportunity mapping
- [ ] Discovery & Research — source quality taxonomy, confidence calibration, synthesis patterns, bias detection
- [ ] Narrative Building — Minto Pyramid, SCQ-A, positioning frameworks, stakeholder calibration
- [ ] Specification Writing — completeness taxonomy, ambiguity detection, zero-question standard

---

## Contributing

MIT licensed. Contributions welcome.

- **Bug:** A framework is under-applied or produces weak output → file an issue
- **Gap:** A failure mode is missing or a scoring rubric needs calibration → PR or issue
- **New skill idea:** A PM task where raw prompting falls short and encoded frameworks would help → open a discussion

---

## License

[MIT](LICENSE) — permissive for commercial and enterprise use.

---

Built by [Parth Sangani](https://www.linkedin.com/in/parthsangani/) · Principal PM, Microsoft M365 Copilot
