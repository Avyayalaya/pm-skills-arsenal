# Contributing

## New skills

Must score ≥90/105 on the [benchmark](benchmark/) before landing on `main`. Open an issue first describing the methodology, target audience, and example output. New skills must include `capability_summary`, `input_schema`, `output_schema`, and `example_invocation` in the YAML frontmatter — `validate_skills.py` will check.

## Improving existing skills

PRs welcome without the full benchmark. Re-benchmark before merge if the change affects framework application, evidence calibration, or output structure.

## Bug reports

Open a GitHub issue with: skill name, the input you ran, the actual output, and what you expected. For MCP server issues, include `python mcp/pm_skills_mcp_server.py --test` output.
