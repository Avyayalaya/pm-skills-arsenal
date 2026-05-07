# PM Skills Arsenal — MCP Server

An MCP server that exposes the 12 PM skills as tools for any MCP-compatible host (Claude Desktop, Cursor, Cline, custom agents).

## Tools

| Tool | Purpose |
|---|---|
| `list_skills` | Returns the catalog: name, description, tags, version, framework count, line count |
| `get_skill` | Returns the full SKILL.md content for a named skill |
| `list_agents` | Returns the 14 agent capabilities (orchestration, intelligence, thinking, etc.) |
| `get_benchmark` | Returns benchmark score and methodology for a named skill |
| `run_skill` | Returns skill content + caller's context, formatted for LLM execution |

## Install

```bash
pip install mcp
```

## Register in Claude Desktop / Claude Code

Add to `.claude.json` (or platform equivalent):

```json
{
  "mcpServers": {
    "pm-skills": {
      "command": "python",
      "args": ["<absolute-path-to>/pm-skills-arsenal/mcp/pm_skills_mcp_server.py"]
    }
  }
}
```

Restart the host. The five tools above appear under the `pm-skills` namespace.

## Register in Cursor

Cursor reads MCP servers from its settings JSON. Add the same `mcpServers` block as above to Cursor's MCP config file.

## Quick verification

```bash
python pm_skills_mcp_server.py --test
```

Expected: `All MCP server self-tests passed.`

## Private skills

The server enforces a `private` flag in the skill catalog. Private skills do not appear in `list_skills`, return an error from `get_skill`, and cannot be invoked via `run_skill`. Smoke test:

```bash
python test_private_flag.py
```

Expected: `All private-flag enforcement tests passed.`

---

Source: this server is maintained at `Agent_Prime/shared/toolkits/pm_skills_mcp_server.py` and copied to this repo. Bug fixes here should be ported back upstream.
