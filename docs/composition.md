# Composition — PM Skills Arsenal × Azure Skills

> How `pm-skills-arsenal` and `microsoft/azure-skills` compose under APM. Authored as part of BLD-006 Bet 7. Reference workflows drawn from worked examples that an agent can use as routing scaffolding.

---

## The reframe

Microsoft's `microsoft/azure-skills` established the pattern in 2026-05: **a domain capability layer = skills (the brain) + MCP server (the hands) + APM manifest (distribution) + telemetry hooks (adoption signal).** Azure was the first domain to ship the full stack.

`pm-skills-arsenal` is the second. PM Skills aren't a separate product for a separate audience — they are a **peer capability layer that composes with Azure Skills under APM**. When both are installed in the same harness, an agent doing plan-and-build work invokes both packages in the same routing context.

The composition isn't an emergent surprise. It's mechanically enabled by:

1. **Same install surface.** APM installs both packages into the same harness; same skill discovery; same hook lifecycle.
2. **Same SKILL.md format.** Each skill's `description` field encodes when-to-invoke triggers — `pm-skills` uses prose (`Use when…`), `azure-skills` uses an explicit `WHEN:` keyword; both serve the same router-matching purpose. `composes_with:` frontmatter (added by Bet 7) makes the cross-package relationships machine-readable.
3. **Same artifact medium.** Markdown. The output of one skill is consumable input to another, regardless of package origin.

---

## Three reference workflows

Drawn from worked examples in BLD-006 Bet 0 (the canonical proofs that this composition actually works on realistic developer tasks).

### Workflow A — Greenfield plan-and-ship

Trigger: "build me X on Azure" where X is a new product or service.

```
problem-framing                  (pm)  → frame what we're building, for whom
  └→ competitive-market-analysis (pm)  → confirm build vs. adopt
     └→ specification-writing    (pm)  → zero-question spec
        ├→ metric-design-experimentation (pm) → measurable outcomes
        └→ product-strategy      (pm)  → wedge + roadmap + NOT-doing
           ├→ azure-prepare      (azure) → infra plan from spec
           ├→ entra-agent-id     (azure) → identity for any agent components
           ├→ azure-validate     (azure) → pre-deploy checks
           ├→ azure-deploy       (azure) → ship
           └→ appinsights-instrumentation (azure) → live telemetry from metric plan
```

Key handoffs:
- Spec → `azure-prepare` Phase 1 brief (the spec's non-functional section drives Bicep choices)
- Spec ACs → `azure-validate` verification checks
- Metric design event schema → `appinsights-instrumentation` custom events
- Strategy NOT-doing list → constrains infra scope (e.g., "no Speech-to-Text" suppresses Speech infra)

### Workflow B — Diagnose-and-redesign from telemetry

Trigger: "metric X is declining; figure out why and fix it."

```
azure-diagnostics                (azure) → entry: scan health + recent changes
  └→ azure-kusto                 (azure) → drill into telemetry
     └→ problem-framing          (pm)    → pivot to PM thinking: structure root cause
        ├→ discovery-research    (pm)    → triangulate hypotheses with non-telemetry evidence
        └→ specification-writing (pm)    → spec for the fix
           ├→ azure-prepare      (azure) → incremental infra updates
           ├→ azure-validate     (azure) → guardrails for the redesign
           └→ azure-deploy       (azure) → ring-0 rollout
              └→ narrative-building (pm) → post-incident comms (audience-adapted)
```

Key handoffs:
- Azure Kusto query output (raw telemetry) → `problem-framing` evidence inventory
- Problem definition → `specification-writing` spec input
- Deploy receipt + diagnostics output → `narrative-building` runtime-evidence input

### Workflow C — Strategy → roadmap → launch

Trigger: "we're entering a new market / repositioning / shipping a major launch."

```
product-strategy                 (pm)    → bets + sequencing + NOT-doing
  ├→ pricing-packaging           (pm)    → tiers + price points
  ├→ go-to-market-strategy       (pm)    → segment + channel + launch
  └→ narrative-building          (pm)    → positioning + why-now + audience variants
     ├→ executive-writing        (pm)    → board memo
     ├→ multi-channel-publishing (pm)    → LinkedIn / blog / deck
     └→ azure-enterprise-infra-planner (azure) → platform-tier choices from strategic scope
        └→ azure-cost            (azure) → cost trajectory model per bet
```

Key handoffs:
- Strategy scope statement (internal-only? multi-region?) → `azure-enterprise-infra-planner` constraint input
- Strategy roadmap → `azure-cost` per-bet cost modeling
- Narrative → `executive-writing` source spine

---

## Cross-reference index

| pm-skills skill | Composes with (cross-package) | Composes with (within pm-skills) |
|---|---|---|
| `specification-writing` | `azure-prepare` (use_before), `azure-validate` (produces_input_for), `azure-deploy` (use_before) | `problem-framing` (use_after), `metric-design-experimentation` (complements) |
| `problem-framing` | `azure-diagnostics` (use_after), `azure-kusto` (use_after) | `specification-writing` (use_before), `competitive-market-analysis` (complements), `discovery-research` (use_after) |
| `metric-design-experimentation` | `appinsights-instrumentation` (produces_input_for), `azure-kusto` (complements) | `specification-writing` (use_after), `product-strategy` (complements), `discovery-research` (complements) |
| `product-strategy` | `azure-enterprise-infra-planner` (use_before), `azure-cost` (complements) | `specification-writing` (use_before), `go-to-market-strategy` (use_before), `metric-design-experimentation` (complements), `narrative-building` (use_before) |
| `narrative-building` | `azure-deploy` (use_after), `azure-diagnostics` (use_after) | `executive-writing` (use_before), `multi-channel-publishing` (use_before), `product-strategy` (use_after) |

Each row's machine-readable form lives in the corresponding SKILL.md's `composes_with:` frontmatter block.

---

## Relation vocabulary

The five relations used in `composes_with:` are:

**Reading convention:** every `composes_with:` entry describes the linked skill from *this skill's* point of view. `use_before` therefore means "this skill is invoked **before** the linked skill" — not "the linked skill is invoked before this skill."

| Relation | Meaning |
|---|---|
| `use_before` | This skill is invoked **before** the linked skill (the linked skill typically consumes this skill's output downstream). |
| `use_after` | This skill is invoked **after** the linked skill (this skill typically consumes the linked skill's output). |
| `produces_input_for` | Stronger than `use_before` — this skill's output is a structural input to the linked one. |
| `requires_output_of` | Stronger than `use_after` — this skill expects the linked skill's output to exist before it can run. |
| `complements` | The two skills can be invoked in parallel or interleaved; outputs combine. Order-agnostic. |

---

## Limitations (artifact-format gaps that still require manual hand-off)

These are findings from the Bet 0 worked examples (`EX-001`, `EX-002`) — places where the composition works *because the agent reads markdown in context*, not because there's a typed contract. Future work could formalize them.

1. **Spec → infra-plan handoff is prose.** `specification-writing` produces a markdown spec; `azure-prepare` reads it as text and translates manually. No structured "spec.json" schema.
2. **Telemetry → PM thinking handoff is prose.** `azure-kusto` query results are tables; `problem-framing` reads them in context. No "telemetry-evidence.json" contract.
3. **Strategy NOT-doing list doesn't propagate.** `product-strategy` produces a NOT-doing list; downstream Azure skills don't read it and may suggest excluded capabilities.
4. **Alert spec vocabulary mismatch.** `metric-design-experimentation` says "guardrail"; `azure-prepare` and Bicep alert rules say "threshold." Same intent, different vocab.
5. **Segmentation as a primitive.** Both packages reference user/tenant/cohort segmentation but neither owns a canonical segmentation artifact format.

These limitations don't break composition. They mean a human or the agent's reasoning bridges the format gap each time. A future bet could ship a `pm-skills/artifact-schemas/` primitive that both packages agree on.

---

## How an agent uses this

1. **At invocation time:** Agent reads the user's intent and matches against `WHEN:` triggers across all installed packages. SKILL.md's `composes_with:` field tells the agent which sibling skills are likely to be invoked next.
2. **At chain-of-thought time:** Agent uses the `composes_with:` graph to plan a multi-step workflow before executing each step.
3. **At handoff time:** Agent treats the previous skill's output as the next skill's input — no special marshaling needed because both packages speak markdown.

The composition is opportunistic, not declarative. The frontmatter doesn't *force* the agent to chain skills; it *recommends* the chain. The agent retains autonomy to pick a different sequence if the user's situation demands it.

---

## Pattern reference

- [microsoft/azure-skills](https://github.com/microsoft/azure-skills) — domain capability layer for Azure
- [microsoft/apm](https://github.com/microsoft/apm) — Agent Package Manager; common install surface
- BLD-006 worked examples — proof that composition holds on realistic developer tasks
