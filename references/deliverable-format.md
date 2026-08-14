# Deliverable Format — File, Front Matter, and Summary Block

This file is the authoritative output contract for the AI Pulse. It replaces the external "global Markdown Deliverable Policy" that earlier versions of `SKILL.md` referenced; that policy lived outside this repo and is no longer available, so the contract is captured here instead. Nothing in the workflow should depend on a document outside this repository.

## Cadence and window

**Monthly, published in the first business days of the month, covering the prior full calendar month.** A briefing dated early September covers August 1–31. This keeps the window unambiguous for the reader: the title names a period, and the period is a whole month.

The `SKILL.md` fallback of "the prior 1–2 calendar months" still applies in two cases:

1. **A thin month.** If a single month genuinely lacks material, widen to two and say so in the issue rather than padding.
2. **A missed issue.** If a month slips, the next issue covers the gap. The June–August 2026 issue did exactly this after a three-month lapse.

Windows longer than three months are a signal the cadence has broken, not a format choice.

## Output location and filename

Save to `~/work-docs/ai/reports/`. Create the directory if it doesn't exist.

```
YYYY-MM-DD_HHMM_ai-pulse-<window-slug>.md
```

- `YYYY-MM-DD_HHMM` — the date and time of writing, not the coverage window
- `<window-slug>` — the coverage period, lowercased and hyphenated

Examples:

```
2026-08-14_1314_ai-pulse-june-august-2026.md
2026-09-03_0930_ai-pulse-august-2026.md
```

## Front matter

Required, at the very top of the file. These field values follow `exemplar-march-may-2026.md`, which is the approved issue and therefore governs when a prose template disagrees with it.

```yaml
---
title: AI Ecosystem & Market Update — [Window]
topics: [ai, briefing, tools, models]
date_created: YYYY-MM-DD
version: 1
purpose: AI tool and market update for consultants, [Window].
audience: Senior consultants, operators, PE teams, business leaders.
status: draft
---
```

Field notes:

- **`title`** — always the full deliverable name with the window appended. "Ecosystem" here is the proper name of the deliverable and is exempt from the banned-phrase list *(see `voice-and-banned-phrases.md`)*.
- **`topics`** — fixed list. Don't tune it per issue; stable tags are what make the archive searchable.
- **`date_created`** — the authoring date, matching the filename prefix.
- **`version`** — starts at `1` and increments on substantive revision of *that issue*, not per issue in the series. The March–May 2026 exemplar shipped at `version: 5` after five rounds of revision.
- **`purpose`** — window-specific, one line. A per-issue purpose is more useful in an archive than a boilerplate line repeated across every issue.
- **`status`** — `draft` until you've reviewed it. Both approved exemplars shipped as `draft`; if you want a distinct sent state, use `final` once the issue goes out.

## Summary block

Directly below the front matter, before the `------` rule and the document title. Neither exemplar carries one — the requirement came from the external policy — so the structure below is the standard as of the June–August 2026 issue, which is the first to implement it.

```markdown
## Summary

[One paragraph. What the window contained and what it means, written so someone
who reads only this paragraph gets the argument. Name the two or three most
consequential developments.]

**Key topics:** [Semicolon-separated list matching the entries, in section order.]

**In scope:** [What this issue covers.]

**Out of scope:** [What was deliberately excluded.]

**Assumptions:** [Where figures came from, as-of date, and any conflict between
sources that the reader should know about. This is where source caveats live —
divergence between vendor-reported and independent benchmarks, contradictory
reporting on availability, and anything stated to a common denominator because
sources disagreed.]
```

The **Assumptions** line is the load-bearing one. The briefing makes specific factual claims about pricing, benchmarks, and regulation; this is where you record what those claims rest on and where the evidence was thin. If verification surfaced a conflict that you resolved by writing to the safest common reading, say so here.

## Document body

Everything below the summary block follows `structure-template.md`: the `# AI Ecosystem & Market Update — [Window]` title, the `### **Meta Trend: …**` block with its sub-blocks, then `#### **Section**` headings with bold standalone development titles, inline `**Detail:**` and `**Why you care:**`, and `------` rules between entries.
