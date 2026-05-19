# Security

If you discover a security vulnerability in `pm-skills-arsenal`, please report it privately rather than through a public GitHub issue.

**How to report:**
- Open a [GitHub security advisory](https://github.com/Avyayalaya/pm-skills-arsenal/security/advisories/new) on this repo, or
- Email `parthsangani@gmail.com` with the details.

**What to include (best-effort, not all required):**
- A short description of the vulnerability
- Steps to reproduce, or a proof-of-concept
- Affected files / skills / installable surface (APM package, MCP server, hook scripts)
- Suggested fix, if you have one

**Response expectations.** This is a personal-time open-source project; response is best-effort and may take days. For urgent or sensitive disclosures, please indicate so in the subject.

**Scope.** Security-relevant areas include:
- The MCP server (`mcp/pm_skills_mcp_server.py`) — input handling, path resolution
- The telemetry hook scripts (`hooks/scripts/track-telemetry.{sh,ps1}`) — stdin parsing, log-file writes
- The APM manifest + plugin manifests — anything that could mislead a harness into loading unexpected content
- The published SKILL.md content — prompt-injection vectors, embedded data exfiltration patterns
