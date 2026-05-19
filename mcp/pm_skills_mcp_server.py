#!/usr/bin/env python3
"""
PM Skills MCP Server — exposes Agent Prime's PM skill library to other AI agents.

Tools:
  - list_skills: List all available PM skills with metadata
  - get_skill: Load a complete skill file by name
  - list_agents: List Agent Prime's agent capabilities
  - get_benchmark: Get benchmark results for a skill
  - run_skill: Prepare skill + context for LLM execution

Uses FastMCP from the `mcp` package (v1.26.0+).

Start: python mcp/pm_skills_mcp_server.py
Register in .claude.json:
  "mcpServers": {
    "pm-skills": {
      "command": "python",
      "args": ["<absolute-path>/pm-skills-arsenal/mcp/pm_skills_mcp_server.py"]
    }
  }
"""
import json
import sys
from pathlib import Path

# Resolve paths
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent  # pm-skills-arsenal/mcp/ -> pm-skills-arsenal/
SKILLS_DIR = SCRIPT_DIR.parent / "skills"
AGENTS_DIR = ROOT / "agents"

# Skill catalog — maps slug to directory name
SKILL_CATALOG = {
    "competitive-market-analysis": {
        "dir": "competitive-market-analysis",
        "description": "9 frameworks for structural competitive analysis — moats, disruption risk, market mapping",
        "tags": ["analyze", "strategy", "market-intelligence"],
        "version": "1.3.0",
        "frameworks": 9,
        "lines": 1300,
    },
    "discovery-research": {
        "dir": "discovery-research",
        "description": "8 frameworks for user discovery — problem space mapping, insight synthesis, opportunity sizing",
        "tags": ["analyze", "research", "user-insight"],
        "version": "1.3.0",
        "frameworks": 8,
        "lines": 1100,
    },
    "problem-framing": {
        "dir": "problem-framing",
        "description": "8 frameworks for problem definition — root cause, constraint mapping, solution space",
        "tags": ["define", "problem-shaping"],
        "version": "1.3.0",
        "frameworks": 8,
        "lines": 1100,
    },
    "specification-writing": {
        "dir": "specification-writing",
        "description": "6 frameworks for product specs — PRDs, user stories, acceptance criteria, edge cases",
        "tags": ["define", "execution"],
        "version": "1.3.0",
        "frameworks": 6,
        "lines": 1100,
    },
    "metric-design-experimentation": {
        "dir": "metric-design-experimentation",
        "description": "9 frameworks for metrics and experiments — North Star, Goodhart countermeasures, A/B design",
        "tags": ["evaluate", "metrics", "experimentation"],
        "version": "1.3.0",
        "frameworks": 9,
        "lines": 1300,
    },
    "narrative-building": {
        "dir": "narrative-building",
        "description": "8 frameworks for strategic narratives — story arcs, audience mapping, evidence layering",
        "tags": ["communicate", "narrative", "influence"],
        "version": "2.0.0",
        "frameworks": 8,
        "lines": 1200,
    },
    "product-strategy": {
        "dir": "product-strategy",
        "description": "7 frameworks for product strategy — vision cascade, bet-sizing, option-value sequencing, strategic tension surfacing, deprioritization, resource allocation, roadmap communication",
        "tags": ["strategy", "planning", "roadmap", "leadership"],
        "version": "1.0.0",
        "frameworks": 7,
        "lines": 1100,
    },
    "go-to-market-strategy": {
        "dir": "go-to-market-strategy",
        "description": "7 frameworks for GTM strategy — market entry thesis, segment selection, channel unit economics, launch gating, positioning, success/failure metrics, growth mechanics",
        "tags": ["strategy", "launch", "growth", "market-entry"],
        "version": "1.0.0",
        "frameworks": 7,
        "lines": 1200,
    },
    "pricing-packaging": {
        "dir": "pricing-packaging",
        "description": "7 frameworks for pricing strategy — model selection, willingness-to-pay analysis, competitive pricing map, Good/Better/Best packaging, sensitivity analysis, revenue impact, AI/SaaS patterns",
        "tags": ["monetization", "strategy", "growth", "business-model"],
        "version": "1.0.0",
        "frameworks": 7,
        "lines": 1200,
    },
    "executive-writing": {
        "dir": "executive-writing",
        "description": "8 frameworks for executive documents — Minto Pyramid, audience calibration, decision architecture, zero-jargon compression, ask framing, evidence cascade",
        "tags": ["communication", "strategy", "leadership", "executive"],
        "version": "1.0.0",
        "frameworks": 8,
        "lines": 1200,
    },
    "multi-channel-publishing": {
        "dir": "multi-channel-publishing",
        "description": "7 frameworks for content derivatives — channel taxonomy, compression methodology, hook adaptation, evidence density calibration, audience matching, fidelity verification, spoken script derivation",
        "tags": ["content", "publishing", "distribution", "strategy"],
        "version": "1.0.0",
        "frameworks": 7,
        "lines": 1100,
    },
    "stakeholder-alignment": {
        "dir": "stakeholder-alignment",
        "description": "7 frameworks for organizational alignment — power-interest-position mapping, coalition analysis, decision archaeology, alignment sequencing, objection pre-emption, communication strategy, monitoring",
        "tags": ["leadership", "communication", "influence", "organizational"],
        "version": "1.0.0",
        "frameworks": 7,
        "lines": 1200,
    },
    "patent-prosecution": {
        "dir": "patent-prosecution",
        "description": "Indian patent law — claim architecture, prior art search, filing strategy (private)",
        "tags": ["legal", "IP", "patents"],
        "version": "1.0.0",
        "frameworks": 6,
        "lines": 1000,
        "private": True,
    },
}

# Agent catalog
AGENT_CATALOG = [
    {"name": "Prime", "capability": "orchestration", "description": "Routes work, reviews quality, kills noise"},
    {"name": "Scout", "capability": "intelligence", "description": "Finds market signals for theses"},
    {"name": "Synthesizer", "capability": "thinking", "description": "Builds strategic theses from evidence"},
    {"name": "Writer", "capability": "production", "description": "Converts theses to publishable artifacts"},
    {"name": "Connector", "capability": "distribution", "description": "Builds strategic relationships"},
    {"name": "Experimenter", "capability": "validation", "description": "Runs rapid experiments"},
    {"name": "Clerk", "capability": "tracking", "description": "Tracks commitments and staleness"},
    {"name": "Planner", "capability": "planning", "description": "Turns ideas into 4-stage plans"},
    {"name": "Builder", "capability": "execution", "description": "Executes Build Handoff Specs"},
    {"name": "Industry Analyst", "capability": "analysis", "description": "Maps industry structure"},
    {"name": "Investment Analyst", "capability": "analysis", "description": "Investment-grade analysis"},
    {"name": "Judge", "capability": "decision", "description": "Autonomous decision proxy"},
    {"name": "Patent Analyst", "capability": "IP_prosecution", "description": "Patent mining and filing"},
    {"name": "Emissary", "capability": "external_action", "description": "Autonomous external actions across platforms"},
]


def list_skills() -> str:
    """List all available PM skills with metadata.

    Returns JSON array of skill objects with name, description, tags, version.
    """
    skills = []
    for slug, info in SKILL_CATALOG.items():
        if info.get("private"):
            continue  # Don't expose private skills
        skills.append({
            "name": slug,
            "description": info["description"],
            "tags": info["tags"],
            "version": info["version"],
            "frameworks": info["frameworks"],
            "lines": info["lines"],
        })
    return json.dumps(skills, indent=2)


def get_skill(skill_name: str) -> str:
    """Load a complete skill file by name.

    Returns the full SKILL.md content as a string.
    If the skill is not found, returns an error message.
    """
    info = SKILL_CATALOG.get(skill_name)
    if not info:
        available = ", ".join(k for k, v in SKILL_CATALOG.items() if not v.get("private"))
        return f"Error: Skill '{skill_name}' not found. Available: {available}"

    if info.get("private"):
        return f"Error: Skill '{skill_name}' is private and cannot be accessed via MCP."

    skill_path = SKILLS_DIR / info["dir"] / "SKILL.md"
    if not skill_path.exists():
        return f"Error: Skill file not found at {skill_path}"

    return skill_path.read_text(encoding="utf-8")


def list_agents() -> str:
    """List Agent Prime's agent capabilities.

    Returns JSON array of agent objects with name, capability, description.
    """
    return json.dumps(AGENT_CATALOG, indent=2)


def get_benchmark(skill_name: str) -> str:
    """Get benchmark results for a skill.

    Returns benchmark score and details if available.
    """
    if skill_name == "competitive-market-analysis":
        return json.dumps({
            "skill": skill_name,
            "score": "98/105",
            "percentage": "93.3%",
            "methodology": "15-criterion evaluation, 7-point scale per criterion",
            "evaluator": "self-administered (rubric authored by the skill author; scored via LLM-as-judge with Claude Opus 4 by the same author)",
            "independence": "this is an author-administered assessment, not an independent evaluation; raw outputs published at benchmark/ for re-scoring",
            "date": "2026-02-19",
            "threshold": "90/105 (publication quality, author-administered)",
            "details": "Missing 7 points: D2 (per-cell tier annotation) and D7 (H/M/L inline throughout)",
        }, indent=2)
    return json.dumps({
        "skill": skill_name,
        "score": "not yet benchmarked",
        "note": "Formal benchmark available for competitive-market-analysis only. Other skills follow the same structural standards. All benchmark assessments are author-administered.",
    }, indent=2)


def run_skill(skill_name: str, context: str) -> str:
    """Prepare a skill + context for LLM execution.

    Returns the skill content followed by the context, formatted for
    an LLM to process according to the skill's methodology.
    """
    skill_content = get_skill(skill_name)
    if skill_content.startswith("Error:"):
        return skill_content

    return f"""# Skill: {skill_name}

{skill_content}

---

# Context for Analysis

{context}

---

# Instructions

Follow the Method section of the skill above. Apply all frameworks to the context provided. Produce output matching the Format Rules section. Run the Evaluation Criteria as a self-check before finalizing.
"""


def start_server():
    """Start the MCP server using FastMCP."""
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError:
        print("Error: mcp package not installed. Run: pip install mcp", file=sys.stderr)
        sys.exit(1)

    mcp = FastMCP("PM Skills Arsenal")

    @mcp.tool()
    def tool_list_skills() -> str:
        """List all available PM skills with metadata (name, description, tags, version, framework count)."""
        return list_skills()

    @mcp.tool()
    def tool_get_skill(skill_name: str) -> str:
        """Load a complete PM skill file by name. Returns the full SKILL.md content."""
        return get_skill(skill_name)

    @mcp.tool()
    def tool_list_agents() -> str:
        """List Agent Prime's 14 agent capabilities (name, role, description)."""
        return list_agents()

    @mcp.tool()
    def tool_get_benchmark(skill_name: str) -> str:
        """Get benchmark score and evaluation details for a PM skill."""
        return get_benchmark(skill_name)

    @mcp.tool()
    def tool_run_skill(skill_name: str, context: str) -> str:
        """Prepare a PM skill + context for LLM execution. Returns skill content + context + instructions."""
        return run_skill(skill_name, context)

    @mcp.resource("skills://health", name="health", description="Health check for PM Skills MCP server")
    def health_check() -> str:
        """Health check — returns server status, skill count, and agent count."""
        public_skills = [k for k, v in SKILL_CATALOG.items() if not v.get("private")]
        skill_files_found = 0
        for slug in public_skills:
            info = SKILL_CATALOG[slug]
            skill_path = SKILLS_DIR / info["dir"] / "SKILL.md"
            if skill_path.exists():
                skill_files_found += 1

        return json.dumps({
            "status": "ok",
            "server": "PM Skills Arsenal",
            "skills_registered": len(public_skills),
            "skills_on_disk": skill_files_found,
            "agents_registered": len(AGENT_CATALOG),
            "skills_dir": str(SKILLS_DIR),
        }, indent=2)

    mcp.run()


if __name__ == "__main__":
    if "--test" in sys.argv:
        # Quick self-test without starting the server
        print("Testing MCP server functions...")
        skills = json.loads(list_skills())
        print(f"  list_skills: {len(skills)} skills")
        assert len(skills) >= 12  # At least 12 public skills

        skill_content = get_skill("competitive-market-analysis")
        assert not skill_content.startswith("Error"), f"Unexpected error: {skill_content[:100]}"
        print(f"  get_skill: {len(skill_content)} chars")

        agents = json.loads(list_agents())
        print(f"  list_agents: {len(agents)} agents")
        assert len(agents) >= 14

        benchmark = json.loads(get_benchmark("competitive-market-analysis"))
        print(f"  get_benchmark: {benchmark['score']}")
        assert benchmark["score"] == "98/105"

        private_skill = get_skill("patent-prosecution")
        assert private_skill.startswith("Error"), "Private skill should not be accessible"
        print("  private skill correctly blocked")

        print("\nAll MCP server self-tests passed.")
    else:
        start_server()
