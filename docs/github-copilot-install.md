---
layout: "default"
title: "GitHub Copilot Installation"
nav_order: 3
---
# Install PM Skills Arsenal — GitHub Copilot

Load skill files into GitHub Copilot Chat or Copilot CLI to get elite-tier PM analysis. Same skills, same frameworks, same output quality as the Claude Code plugin.

---

## Quick Start

### Option A: Copilot Chat in VS Code / JetBrains

1. **Clone the repo** into your workspace (or a folder your editor can see):

   ```bash
   git clone https://github.com/Avyayalaya/pm-skills-arsenal.git
   ```

2. **Open the folder** in VS Code (or add it to your workspace).

3. **Reference a skill** in Copilot Chat using `#`:

   ```
   #skills/competitive-market-analysis/SKILL.md

   Our biggest competitor just made their core product free for teams
   under 50. We're a Series B with 800 paying customers. Build a
   competitive war map and recommend our response.
   ```

   Copilot loads the full skill file as context and produces framework-driven output.

> **Tip:** You can also drag and drop the `.md` file directly into the Copilot Chat window, or use the **Add Context** button.

### Option B: Copilot CLI

1. **Clone the repo** somewhere accessible:

   ```bash
   git clone https://github.com/Avyayalaya/pm-skills-arsenal.git
   ```

2. **Reference the skill file** in your prompt:

   ```
   #pm-skills-arsenal/skills/metric-design-experimentation/SKILL.md

   We're launching real-time co-editing in our analytics product. 22K DAU,
   W4 retention 52%. Build a measurement framework — NSM, experiment plan,
   and retention cohort design.
   ```

### Option C: No Clone (Copy-Paste)

1. Open the skill file on GitHub:
   - [Competitive & Market Analysis](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/competitive-market-analysis/SKILL.md)
   - [Metric Design & Experimentation](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/metric-design-experimentation/SKILL.md)
   - [Specification Writing](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/specification-writing/SKILL.md)

2. Click **Raw**, copy the full contents.

3. Paste into Copilot Chat at the start of your conversation, then ask your question.

---

## ⚠️ What NOT to Do

**Do NOT add skill files to `.github/copilot-instructions.md` or `.github/instructions/`.**

Why:
- Skill files are 1,000–1,100 lines each. GitHub recommends keeping instruction files under 1,000 lines — beyond that, Copilot processes instructions inconsistently.
- Instruction files load on **every** Copilot request. A 1,000-line skill file would consume most of your context budget even when you're doing unrelated work.
- Skills are meant to be loaded **on demand** — reference them with `#` when you need them.

---

## How It Works

When you reference a skill file with `#`, Copilot loads the full markdown content into its context window for that conversation. The skill contains:

- **Domain frameworks** with scoring rubrics and decision tables
- **Application method** — step-by-step with decision points
- **Quality gradients** — Intern / Consultant / Elite tier definitions
- **Failure modes** — what goes wrong and how to detect it
- **Mandatory output sections** — Assumption Registry, Adversarial Self-Critique, Revision Triggers

The model reads the skill and applies the encoded frameworks to your question. No special commands or syntax needed — just ask naturally.

---

## File Sizes & Context Budget

| Skill | Lines | Size | Fits in context? |
|---|---|---|---|
| Competitive & Market Analysis | 1,099 | 91 KB | ✅ Yes |
| Metric Design & Experimentation | 1,050 | 93 KB | ✅ Yes |
| Specification Writing | 1,109 | 114 KB | ✅ Yes |

All three files fit comfortably within Copilot's context window (200K+ tokens for current models). Loading one skill leaves ample room for your prompt, conversation history, and code context.

---

## Tips for Best Results

1. **Load one skill per conversation.** Each skill is self-contained. Loading multiple skills at once wastes context and can confuse framework application.

2. **Be specific in your prompt.** The skill handles the frameworks — you provide the domain context. Include: your product, your market, your constraints, your data.

3. **Use the Quick Version for follow-ups.** Each skill has a Quick Version (10–15 lines) inside the Full Version. After the initial analysis, you don't need to re-reference the full file — the model retains the framework context.

4. **Check the Quality Gradient.** Every skill output includes a self-assessment tier (Intern / Consultant / Elite). If output lands at Consultant tier, the skill's Failure Modes section tells you what to fix.

---

## Tested With

| Model | Status |
|---|---|
| Claude Sonnet 4.6 (via Copilot) | ✅ Tested — full framework application |
| GPT-5.1 (via Copilot) | ✅ Tested — strong output |
| GPT-5.2-Codex (via Copilot) | ✅ Tested — strong output |
| Claude Haiku 4.5 (via Copilot) | ✅ Tested — lower cost, good results |

---

## FAQ

**Q: Does Copilot truncate the file if it's too large?**
No. At 91–114 KB, skill files are well within Copilot's context window. You'll see the full framework applied in output.

**Q: Can I use this with GitHub Copilot in the browser (github.com)?**
Yes. Use the copy-paste method — paste the raw skill file contents into the Copilot Chat on github.com, then ask your question.

**Q: Can I reference multiple skill files at once?**
Technically yes, but not recommended. Each skill is 1,000+ lines. Loading two would consume significant context and dilute framework application.

**Q: How is this different from custom instructions?**
Custom instructions (`.github/copilot-instructions.md`) are short, persistent rules for every request. Skills are deep domain knowledge loaded on demand for specific tasks. They serve different purposes.

---

*[Back to Home](../index.html) · [GitHub Repo](https://github.com/Avyayalaya/pm-skills-arsenal) · MIT License*
