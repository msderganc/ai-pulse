# AI Pulse — Document Structure Template

Use this exact structure. The skeleton is not optional — readers expect this shape and scan for it. Always read both exemplars in this directory alongside this file: `exemplar-issue.md` *(original compact reference)* and `exemplar-march-may-2026.md` *(mature reference with headline titles, full descriptive voice, and per-section density at scale)*. The exemplars are ground truth for formatting choices that prose can't fully convey *(heading depth, inline emphasis, italic clarifications, horizontal rules, title style, entry density)*.

## Heading hierarchy (important — easy to get wrong)

The AI Pulse uses a deliberately shallow heading hierarchy. Most rendering surfaces (email clients, Notion, Confluence, Word) handle 3 levels gracefully; deeper nesting reads as bureaucratic.

| Element | Markdown |
| --- | --- |
| Document title (optional, often omitted when the briefing is pasted into an email or doc with its own title) | `# AI Ecosystem & Market Update — [Month Year]` |
| Meta Trend block | `### **Meta Trend: [thesis]**` |
| Meta Trend sub-blocks (What's changing, Why this matters, [Year] implication, plus optional extras like "Where value now sits") | `#### **What's changing**` |
| Section name (OpenAI, Google, Anthropic, Cross-Vendor, Regulation & Enterprise Risk, etc.) | `#### **OpenAI**` |
| Individual development title | `**OpenAI GPT-5.2 released under competitive pressure**` *(bold standalone line — NOT a heading)* |
| Separator between developments | `------` *(horizontal rule on its own line)* |

The development title being a bold standalone line, not a `###` heading, is one of the most counterintuitive aspects of the format. It matters because the visual rhythm of bold-title → Detail → Why-you-care → horizontal-rule is what makes the briefing scannable on phones and in pasted previews.

### Development titles are news headlines, not product names

A title must convey **what happened and why it matters** — not just name the product. The product name alone forces the reader to scan the Detail to understand whether the entry is worth their attention; a headline-style title lets them decide at a glance.

**Pattern:** `[Subject] [strong verb] [meaningful object/consequence]`

**Strip dates from titles** — dates belong in the Detail. Title space is too valuable to spend on calendar information.

**Examples (weak vs. strong):**

| Weak (product name only) | Strong (headline) |
| --- | --- |
| `GPT-5.5 (April 23)` | `GPT-5.5 released as OpenAI's first ground-up rebuild since GPT-4.5` |
| `Claude Design (April 17)` | `Anthropic Labs launches Claude Design as a Figma alternative powered by Opus 4.7` |
| `Gemini 3.1 family` | `Gemini 3.1 family lands across three price tiers, with Flash-Lite at one-eighth the price of Pro` |
| `Cursor 3` | `Cursor 3 rebuilds the IDE around parallel agents, taking the fight to Codex and Claude Code` |
| `EU AI Act deadlines deferred` | `EU AI Act high-risk deadlines pushed to 2027–2028, easing the August 2026 cliff` |

A senior consultant should be able to read the titles alone and know which entries matter to a current engagement. Treat the title like a Wall Street Journal headline, not a press-release dateline.

## Inline formatting conventions

These are what give the AI Pulse its distinct visual texture. Use them deliberately.

### `**Detail:**` and `**Why you care:**` run inline

The bolded label and its content sit on the same paragraph, separated by a space — not on separate lines, not on a line above content. Inline.

### Detail voice — descriptive, not telegraphic

The Detail section uses a narrative descriptive voice, not a data-dump. The pattern:

1. **Lead sentence identifies the thing fully** — "[Name] is [vendor]'s [latest/new] [product category], [where/how it fits]."
2. **A signature-feature clause** — often quoting the vendor's technical hook or the most distinctive characteristic.
3. **"It excels at..." sentence** — strengths listed as parallel prose (not bullets), 2–4 items.
4. **Closing competitive or historical positioning** — what it replaces, who it competes with, what it changes about the category.

Not every entry has all four components — multi-product composite entries and pricing/regulation entries adapt the voice rather than force the structure. But the voice itself (full sentences, narrative flow, deliberate placement of technical hooks and competitive context) is constant.

**Reference Detail (the canonical example):**

> ChatGPT Images 2.0 is OpenAI's latest image generation tool integrated into ChatGPT, featuring "thinking-enabled generation" that prioritizes interpretation and planning before pixel generation. It excels in rendering legible, multilingual text, maintaining stylistic realism, and handling complex instructions with precision, replacing DALL-E 3 with significant improvements in text accuracy and resolution.

**Notes:**

- Avoid the telegraphic spec-sheet voice *("Image gen with reasoning, 2K res, 8 images/prompt")* — that's a different document. The Detail reads like a clear briefing intro.
- Embed numbers and benchmark scores inline in sentences, not as standalone callouts.
- Italic parenthetical clarifications *(short, one-clause)* still apply for accessibility.
- Bold inline emphasis on load-bearing terms still applies — usually the product name and one or two distinctive features per Detail.

### Why-you-care voice — punchy, operational, opinionated

In contrast, Why-you-care stays sharp and direct. It is not a continuation of the Detail's descriptive voice. Short sentences. Names a specific actor or decision. States the implication directly. This is where the consulting judgment lives — and rewriting it into the descriptive Detail voice would dilute it.

### Italic parentheticals `*(...)*` for clarifications

Whenever a term might stall a non-technical reader, add a short italicized parenthetical. This is the canonical accessibility pattern for the AI Pulse:

- "*(the leading AI systems now deliver similar results for most business tasks)*"
- "*(a working memory roughly equivalent to hundreds of pages of text at once)*"
- "*(systems that write, review, and modify software)*"
- "*(those affecting safety, financial outcomes, or regulated decisions)*"

Keep them to one short clause. Italics signal "this is a clarification, you can skip it if you don't need it" — which is exactly how a senior technical reader scans the document.

### Bold inline emphasis on load-bearing terms

Bold key nouns and phrases that carry the operational signal, especially in the meta-trend block. Don't bold for decoration. Examples from the exemplar:

- "**workflows**", "**data readiness**", "**governance**"
- "**context window of up to 1 million tokens**"

One or two bolded phrases per paragraph is typical; more than three starts to feel like a marketing deck.

### Horizontal rules between developments

Place `------` on its own line between consecutive development entries inside a section. The rule is part of the rhythm — it gives the reader a visual breath between items and keeps bolded titles from running together.

## Full template

```markdown
# AI Ecosystem & Market Update — [Month Year]
*(top-level title optional; often omitted when pasted into a doc/email with its own title)*

### **Meta Trend: [Short thesis statement — one sentence, opinionated, operational]**

#### **What's changing**

[2–4 concise paragraphs. Describe the shift this month's evidence reveals. Use bold
inline emphasis on the load-bearing terms. Italic parentheticals for any term a
non-technical reader might stall on.]

#### **Where value now sits** *(optional — use when the throughline lends itself to a list)*

[Short framing sentence introducing the list, then:]

- How AI is embedded into **workflows** *(short clarification)*
- **Data readiness** and signal quality *(short clarification)*
- **Decision ownership**, thresholds, and escalation *(short clarification)*
- Adoption, **governance**, and cost control at scale *(short clarification)*

#### **Why this matters**

[One or two short paragraphs. Direct operational implication. Name the decision or
behavior that should change.]

#### **[Year] implication**

[One short paragraph. Forward-looking, take a position, no "time will tell".]

------

#### **[Section name — e.g., OpenAI]**

**[Development title — bold, standalone line, sentence case or title case but consistent across the issue]**

**Detail:** [Brief explanation of what changed and why it is materially different.
Usually 2–4 sentences. Lead with the change, not the vendor's framing of it.]

**Why you care:** [Specific implication for enterprise adoption, consulting work,
workflows, governance, economics, or operating models. One paragraph. Must be
actionable or decision-relevant.]

------

**[Next development title]**

**Detail:** ...

**Why you care:** ...

------

#### **[Next section — e.g., Google]**

**[Development title]**

**Detail:** ...

**Why you care:** ...

------
```

## Section ordering

Lead with whichever vendor or theme had the most operationally significant developments that month — not always OpenAI by default. The order signals what mattered. Typical ordering when developments are roughly equal:

1. The vendor with the biggest operational shift (often OpenAI or Anthropic)
2. Other major vendors with material moves
3. Cross-vendor / platform developments
4. Regulation & enterprise risk
5. Infrastructure / economics

If regulation drove the month, lead with regulation. The structure serves the throughline, not vendor diplomacy.

## Section minimums

- A section needs **at least one** development that materially affects enterprise adoption, operating models, workflows, governance, economics, regulation, or competitive dynamics.
- **Omit a section** rather than pad it. A blank OpenAI section is fine if OpenAI didn't do anything operationally meaningful that month.
- A section can hold a single development if that development carried the section by itself (see the Google entry in the exemplar — one Gemini Flash development).

## Length targets (guidance, not rules)

- Meta trend block: ~250–500 words total across the sub-blocks (more if you use the optional "Where value now sits" list)
- Each development entry: ~60–180 words total across Detail + Why you care (the exemplar's range)
- Total document: ~1,500–2,500 words is a comfortable range; longer if a major shift demands it

If the briefing trends toward 3,500+ words, you almost certainly kept items that don't earn their place. Cut.

## What the closing should *not* be

- Not a "key takeaways" bulleted recap (the reader just read it)
- Not "what to watch next month" unless you have a specific named thing to watch
- Not a generic exhortation to "stay agile" or "invest in AI literacy"
- If you don't have a sharp closing thought, the last development entry is the ending. That's fine — the exemplar ends on the EU AI Act entry with no wrap-up.

## When in doubt, look at the exemplars

Both `exemplar-issue.md` and `exemplar-march-may-2026.md` are real, approved AI Pulses. When this template and either exemplar disagree on a detail, the exemplar wins — update this template to match. When the two exemplars disagree *(e.g., entry density, title style, voice)*, treat `exemplar-march-may-2026.md` as the more recent canonical bar; it carries the mature voice and title conventions the briefings have evolved into.
