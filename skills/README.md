# Skills

Each skill gets its own folder:

```
skills/
  <skill-name>/
    SKILL.md
    (optional supporting files: scripts, references, examples)
```

`SKILL.md` uses minimal YAML frontmatter plus a markdown body:

```markdown
---
name: skill-name
description: When this skill should be used
---

Instructions for the skill go here.
```

Keep frontmatter to `name` and `description` only. Tool-specific fields don't belong in the canonical file — the goal is that this content is readable and reusable by any coding agent, not just Claude Code.
