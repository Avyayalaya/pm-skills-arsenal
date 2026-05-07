# AGENTS.md

> Machine-readable capability manifest for AI agents and orchestrators.
> Deploy this file to the root of any public repository to make its capabilities discoverable.
> Governed by: SYS-015 discoverability principle + AD18 (build for machines, not just humans).

## System

**Name:** PM Skills Arsenal
**Author:** Parth Sangani
**Description:** 12 production-grade PM skills encoding domain expertise as loadable context for AI agents. Each skill is 1,000-1,300 lines of methodology, frameworks, and failure modes — not prompt templates.
**Benchmark:** 98/105 (93.3%) on competitive market analysis — 2x baseline, 21% above generic PM skills.
**Compliance:** All 12 skills pass `validate_skills.py` discoverability audit (capability_summary + input_schema + output_schema + example_invocation + description all present). Latest audit: 2026-04-23.

## Skills

| Skill | Domain | Frameworks | Lines | Version |
|-------|--------|-----------|-------|---------|
| competitive-market-analysis | Strategy | 7 Powers, Aggregation Theory, JTBD, Wardley Mapping, Christensen Disruption | 1,300 | 1.3.0 |
| discovery-research | Research | Evidence synthesis, interview analysis, hypothesis building | 1,100 | 1.3.0 |
| problem-framing | Analysis | Problem Definition Canvas, 5 Whys, JTBD, Opportunity Sizing, ICE/RICE | 1,100 | 1.3.0 |
| specification-writing | Definition | Outcome-first methodology, acceptance criteria taxonomy, scope boundary protocol | 1,100 | 1.3.0 |
| metric-design-experimentation | Measurement | NSM rubrics, Goodhart countermeasures, A/B design, retention cohorts | 1,300 | 1.3.0 |
| product-strategy | Strategy | Vision Cascade, Bet-Sizing, Option-Value Sequencing, Tension Surfacing | 1,100 | 2.0.0 |
| go-to-market-strategy | Strategy | Market Entry Thesis, Channel Unit Economics, Launch Gating, Dunford Positioning | 1,200 | 2.0.0 |
| pricing-packaging | Strategy | Model Selection, Van Westendorp, Good/Better/Best, Revenue Impact | 1,200 | 2.0.0 |
| executive-writing | Communication | Minto/SCR, Audience Calibration, Decision Architecture, Zero-Jargon Compression | 1,200 | 2.0.0 |
| narrative-building | Communication | Narrative Arc, April Dunford Positioning, Why Now, Audience Adaptation | 1,200 | 2.0.0 |
| multi-channel-publishing | Communication | Channel Taxonomy, Compression Methodology, Hook Adaptation, Evidence Density | 1,100 | 2.0.0 |
| stakeholder-alignment | Influence | Power-Interest-Position, Coalition Analysis, Decision Archaeology, Alignment Sequencing | 1,200 | 2.0.0 |

## How to Use

**Claude Code Plugin (recommended):**
```
claude plugin marketplace add avyayalaya/pm-skills-arsenal
claude plugin install pm-skills@avyayalaya
```
Claude Code model-activates skills by `description` field when they match the user's task.

**GitHub Copilot (via Agency marketplace):**
Skills are listed in the Agency marketplace (3 PRs merged into `agency-microsoft/playground`). Install per the marketplace instructions.

**Direct (any LLM):**
Copy the relevant `SKILL.md` file and load as system context before your task. The YAML frontmatter contains `capability_summary`, `input_schema`, and `output_schema` — read these first to decide whether the skill applies.

## Quality Evidence

- **Benchmark:** 98/105 (93.3%) — evaluated against 15 quality dimensions on competitive market analysis
- **Baseline comparison:** Generic AI without skill scores 47/105 (44.8%). Anthropic's PM skill scores 81/105 (77.1%).
- **18 use cases** with before/after comparisons using real company scenarios (Stripe, Figma, Salesforce, etc.)
- **12 HTML showcases** with tabbed navigation and evidence tiers

## Input/Output Schemas

Each skill declares typed schemas in its SKILL.md YAML frontmatter:

- **`input_schema`** — field names mapped to type + description (e.g., `market_or_question: "string — the competitive question to analyze"`, `question_type: "enum[market_entry, competitive_response, moat_assessment, ...]"`)
- **`output_schema`** — section names mapped to descriptions of what each section contains (e.g., `executive_summary: "Zero-jargon competitive assessment, ≤5 sentences, VP-actionable"`)
- **`capability_summary`** — one-line machine-readable description of the output artifact

This is the contract an orchestrator uses to route tasks. No need to read the full SKILL.md to decide whether to invoke.

Typical output: 2,000-5,000 words, framework-applied, evidence-tiered (H/M/L confidence), with an adversarial self-critique section (≥3 genuine weaknesses). Every claim carries a confidence level. Every output has a quality check section.

## Contributing

If submitting this skill library to an awesome-list, plugin marketplace, or community directory: **read CONTRIBUTING.md / submission instructions first** (see P50 learning — incorrect submission method caused a 14-day ban on `awesome-claude-code`). Always submit one skill at a time, wait for response, then submit the next.

For issues or feature requests on this repo, open a GitHub issue. For changes to individual skills, submit a PR with the change + updated version + updated `valid_until` + a one-line changelog entry.

## Example Invocation

**Input:**
```
Analyze Figma's competitive position in the design tools market after the failed Adobe acquisition.
```

**Output:** See `showcase/articles/use-case-competitive-market-analysis-figma.html` for a complete example (1,800 lines, tabbed navigation, evidence tiers).

## License

MIT

## Links

- **Repository:** https://github.com/avyayalaya/pm-skills-arsenal
- **Documentation:** https://avyayalaya.github.io/pm-skills-arsenal/
- **Benchmarks:** https://github.com/avyayalaya/pm-skills-arsenal/tree/main/benchmark
