#!/usr/bin/env python3
"""Add Just the Docs frontmatter to all documentation files."""

import os
from pathlib import Path

# Define frontmatter for each file
frontmatters = {
    "docs/use-case-metric-design.md": {
        "layout": "default",
        "title": "Metric Design: M365 Copilot Adoption",
        "parent": "Use Cases",
        "nav_order": 2
    },
    "docs/use-case-specification.md": {
        "layout": "default",
        "title": "Specification: AI Chat Interface",
        "parent": "Use Cases",
        "nav_order": 3
    },
    "docs/use-case-problem-framing.md": {
        "layout": "default",
        "title": "Problem Framing: Notion's Growth Plateau",
        "parent": "Use Cases",
        "nav_order": 4
    },
    "docs/use-case-discovery-research.md": {
        "layout": "default",
        "title": "Discovery Research: Superhuman Email",
        "parent": "Use Cases",
        "nav_order": 5
    },
    "docs/use-case-narrative-building.md": {
        "layout": "default",
        "title": "Narrative Building: Cursor Positioning",
        "parent": "Use Cases",
        "nav_order": 6
    },
    "docs/case-study-art-gallery.md": {
        "layout": "default",
        "title": "Case Study: Art Gallery Expansion",
        "parent": "Case Studies",
        "nav_order": 1
    },
    "docs/case-study-meditation-app.md": {
        "layout": "default",
        "title": "Case Study: Meditation App Engagement",
        "parent": "Case Studies",
        "nav_order": 2
    },
    "docs/github-copilot-install.md": {
        "layout": "default",
        "title": "GitHub Copilot Installation",
        "nav_order": 3
    }
}

def add_frontmatter_to_file(filepath, frontmatter):
    """Add YAML frontmatter to a file if it doesn't already have it."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if frontmatter already exists
    if content.startswith('---\n'):
        print(f"[OK] {filepath} already has frontmatter")
        return

    # Build frontmatter
    fm_lines = ['---']
    for key, value in frontmatter.items():
        if isinstance(value, str):
            fm_lines.append(f'{key}: "{value}"')
        else:
            fm_lines.append(f'{key}: {value}')
    fm_lines.append('---')
    fm_lines.append('')  # Blank line after frontmatter

    # Prepend frontmatter
    new_content = '\n'.join(fm_lines) + content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"[OK] Added frontmatter to {filepath}")

# Process all files
for filepath, frontmatter in frontmatters.items():
    if os.path.exists(filepath):
        add_frontmatter_to_file(filepath, frontmatter)
    else:
        print(f"[ERROR] File not found: {filepath}")

print("\nDone! All frontmatter added.")
