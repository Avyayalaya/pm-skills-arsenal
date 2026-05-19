# Changelog

## 2.1.0

Initial APM release. Multi-harness install (Copilot CLI, Claude Code, Cursor, OpenCode, Codex, Gemini) via the [APM Agent Package Manager](https://github.com/microsoft/apm) + telemetry hooks + composition wiring with [`microsoft/azure-skills`](https://github.com/microsoft/azure-skills) via `composes_with:` frontmatter on five highest-traffic skills + a [`docs/composition.md`](docs/composition.md) guide.

Pull `apm install Avyayalaya/pm-skills-arsenal#v2.1.0` for a pinned install across every compatible harness. See [README](README.md#install) for direct per-harness install paths.

### APM port + Microsoft-style plugin metadata

- `apm.yml` with marketplace authoring block
- Root `plugin.json` mirroring the `microsoft/azure-skills` shape
- `.mcp.json` wiring the existing `pm-skills` MCP server (5 tools: `list_skills`, `get_skill`, `list_agents`, `get_benchmark`, `run_skill`); server unchanged
- Multi-harness telemetry hooks + cross-platform `track-telemetry.{sh,ps1}` scripts — local-only JSONL append, no remote network calls, anonymized skill-invocation logging
- Per-harness plugin manifests: `.claude-plugin/`, `.cursor-plugin/`, `.plugin/` (OpenCode/Codex fallback), `gemini-extension.json`
- `SECURITY.md`, `.gitattributes`, `.github/CODEOWNERS`, README install section leads with APM (pinned `#v2.1.0` first; floating-main as fallback)

### Composition wiring

- `composes_with:` frontmatter on `specification-writing`, `problem-framing`, `metric-design-experimentation`, `product-strategy`, and `narrative-building` — declares cross-package routing relationships to `microsoft/azure-skills` siblings. Schema introduces 5 relations: `use_before`, `use_after`, `produces_input_for`, `requires_output_of`, `complements`
- [`docs/composition.md`](docs/composition.md) — companion guide with three reference workflows (greenfield plan-and-ship; diagnose-and-redesign from telemetry; strategy → launch), cross-reference index, relation vocabulary, and known artifact-format limitations

### Honesty fixes

- Every cite of the `98/105` benchmark across README / AGENTS / index / MCP server tool output now carries an explicit self-administered disclosure: the same author wrote the rubric AND scored every output. Raw outputs published at [`benchmark/`](benchmark/) for independent re-scoring.
- Stripped self-applied quality adjectives ("codex-grade") from README, manifests, and marketplace descriptions.

Full diff: see commit on `main` matching the v2.1.0 tag.
