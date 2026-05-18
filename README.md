# ai-pulse

A Claude Code skill for generating the **AI Pulse** — a concise, opinionated executive briefing on AI developments for senior consultants, operators, PE teams, and business leaders.

## What it produces

A monthly markdown briefing covering the 1–2 month window with a sharp meta-trend, news-headline-style entry titles, descriptive Detail sections, and operational "Why you care" lines. Output lands in `~/work-docs/ai/reports/`.

## Install

Drag `ai-pulse.skill` into Claude Desktop, or symlink the skill into Claude Code:

```bash
ln -s /path/to/this/repo ~/.claude/skills/ai-pulse
```

## Usage

Invoke `/ai-pulse <window>` (e.g. `/ai-pulse March to May`). The skill runs:

1. **Search** for material across the window
2. **Topic menu** — present 10+ candidates per section for user selection
3. **Per-item verification** — targeted searches for exact dates, numbers, partners, pricing, competitive context
4. **Pre-draft validation** — facts, sources, framing, throughline
5. **Draft** in the established voice
6. **Post-draft writing review** — does it land? is there too much detail?
7. **Humanizer pass**
8. **Write file** to `~/work-docs/ai/reports/`

## Structure

```
SKILL.md                                    Workflow entry point
references/
  exemplar-issue.md                         Ground-truth approved example
  structure-template.md                     Format, headings, voice, title convention
  voice-and-banned-phrases.md               Voice rules, banned phrases, accessibility
  content-priorities.md                     Selection criteria, required coverage
ai-pulse.skill                              Packaged distribution for Claude Desktop
```

## Repackaging

After editing the skill, repackage with:

```bash
python3 -m scripts.package_skill /path/to/this/repo
```

from inside the skill-creator plugin directory.
