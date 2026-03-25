# AGENTS.md

> Machine-readable capability manifest for AI agents and orchestrators.
> Deploy this file to the root of any public repository to make its capabilities discoverable.

## System

**Name:** PM Skills Arsenal
**Author:** Parth Sangani
**Description:** 12 production-grade PM skills encoding domain expertise as loadable context for AI agents. Each skill is 1,000-1,300 lines of methodology, frameworks, and failure modes — not prompt templates.
**Benchmark:** 98/105 (93.3%) on competitive market analysis — 2x baseline, 21% above generic PM skills.

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

**MCP Server (recommended for Claude Code):**
```
claude mcp add avyayalaya/pm-skills-arsenal
```

**GitHub Copilot Plugin:**
```
# In VS Code Copilot Chat, load skills as context:
@workspace /skills competitive-market-analysis
```

**Claude Code Plugin:**
```
claude plugin marketplace add avyayalaya/pm-skills-arsenal
claude plugin install pm-skills@avyayalaya
```

**Direct (any LLM):**
Copy the relevant `SKILL.md` file and load as system context before your task.

## Quality Evidence

- **Benchmark:** 98/105 (93.3%) — evaluated against 15 quality dimensions on competitive market analysis
- **Baseline comparison:** Generic AI without skill scores 47/105 (44.8%). Anthropic's PM skill scores 81/105 (77.1%).
- **18 use cases** with before/after comparisons using real company scenarios (Stripe, Figma, Salesforce, etc.)
- **12 HTML showcases** with tabbed navigation and evidence tiers

## Input/Output Schemas

**Input:** Business context as natural language. Each skill's Context Gate specifies required vs. optional inputs.

**Output:** Structured analysis document with sections defined by the skill. Typical output: 2,000-5,000 words with frameworks applied, evidence cited, confidence levels stated (H/M/L), and adversarial self-critique included.

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
