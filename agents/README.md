# Agents

Each agent gets its own folder:

```
agents/
  <agent-name>/
    agent.md
```

`agent.md` uses minimal YAML frontmatter plus a markdown body:

```markdown
---
name: agent-name
description: When this agent should be used
---

Instructions for the agent go here.
```

Keep frontmatter to `name` and `description` only. Tool-specific fields (e.g. Claude Code's `tools`, `model`) don't belong in the canonical file — the goal is that this content is readable and reusable by any coding agent, not just Claude Code.
