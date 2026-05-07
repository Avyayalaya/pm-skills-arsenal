"""Smoke test: verify patent-prosecution and any other private skill is blocked
on every public surface (list_skills, get_skill, run_skill).

Must pass before MCP server is published. The whole point of publishing the
server is to expose the 12 public skills; leaking a private skill here
defeats the gate.
"""
import json
import sys
from pathlib import Path

# Import the module under test
sys.path.insert(0, str(Path(__file__).parent))
from pm_skills_mcp_server import list_skills, get_skill, run_skill, SKILL_CATALOG


def test_list_skills_excludes_private():
    skills = json.loads(list_skills())
    names = [s["name"] for s in skills]
    private_slugs = [k for k, v in SKILL_CATALOG.items() if v.get("private")]
    assert private_slugs, "Expected at least one private skill in the catalog (sanity check)"
    for slug in private_slugs:
        assert slug not in names, f"Private skill '{slug}' leaked into list_skills"


def test_get_skill_blocks_private():
    private_slugs = [k for k, v in SKILL_CATALOG.items() if v.get("private")]
    for slug in private_slugs:
        result = get_skill(slug)
        assert result.startswith("Error:"), f"get_skill('{slug}') did not return Error"
        assert "private" in result.lower(), f"Error for '{slug}' should mention 'private'"


def test_run_skill_blocks_private():
    private_slugs = [k for k, v in SKILL_CATALOG.items() if v.get("private")]
    for slug in private_slugs:
        result = run_skill(slug, "any context")
        assert result.startswith("Error:"), f"run_skill('{slug}') did not return Error"


if __name__ == "__main__":
    test_list_skills_excludes_private()
    test_get_skill_blocks_private()
    test_run_skill_blocks_private()
    print("All private-flag enforcement tests passed.")
