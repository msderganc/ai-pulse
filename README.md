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
  exemplar-issue.md                         Ground-truth approved example (compact)
  exemplar-march-may-2026.md                Ground-truth approved example (mature, canonical)
  structure-template.md                     Format, headings, voice, title convention
  voice-and-banned-phrases.md               Voice rules, banned phrases, accessibility
  content-priorities.md                     Selection criteria, required coverage
  deliverable-format.md                     Cadence, filename, front matter, summary block
ai-pulse.skill                              Packaged distribution for Claude Desktop
```

## Repackaging

A pre-commit hook auto-regenerates `ai-pulse.skill` whenever `SKILL.md` or any file in `references/` is staged for commit. The packaged `.skill` is added to the same commit so the distribution stays in sync with source.

**One-time setup after cloning:**

```bash
git config core.hooksPath .githooks
```

`core.hooksPath` is a local repo config and doesn't persist on clone, so this step is required once per checkout.

**Manual repackaging** (no source changes staged, or testing the script):

```bash
python3 scripts/repackage.py
```

The repackager is self-contained — it uses only Python's `zipfile` module, no dependency on the skill-creator plugin.
