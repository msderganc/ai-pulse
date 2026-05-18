---
name: ai-pulse
description: Generate the "AI Pulse" executive briefing — a concise, opinionated monthly update on AI developments for senior consultants, operators, PE teams, and business leaders. Use this skill whenever the user asks for an AI Pulse, AI ecosystem update, AI market update, monthly AI briefing, AI exec summary, AI digest for leadership, "the AI update", or wants a forward-able internal briefing on recent AI developments aimed at non-technical executives. Trigger it even if the user describes the deliverable in their own words rather than naming it (e.g., "summarize the last six weeks of AI for our partners", "draft the monthly AI memo for clients", "what should the leadership team know about AI right now"). Owns voice, structure, content priorities, banned phrases, and a mandatory humanizer pass.
---

# AI Pulse — Executive Briefing Generator

This skill produces the "AI Pulse" — a recurring executive update on AI developments from roughly the past 1–2 months. The reader is a senior consultant, operator, PE investor, or business leader. They are intelligent but their technical depth varies. They want signal, not coverage.

## What this skill is *for*

**Primary purpose: catch senior consultants up on the AI tools and product surface they can actually use** — both on engagements and in their own daily work. The supporting purpose is business context: vendor moves, regulation, and economics that frame how clients buy.

A document a senior consultant would actually forward to a client or partner. Sharp operational observations. A clear throughline. No hedging for the sake of balance. No AI cliché vocabulary.

The standing thesis the meta-trend should sharpen: **the tool layer is where AI differentiation is moving — model capability is converging, while the product surface around the models is exploding.** Operating model and integration matters, but the tool releases are the lead story. Every issue's meta-trend should sharpen this thesis with the month's evidence.

**Length target: under 1000 total words.** Earlier versions of this skill targeted 1,500–2,500 words and ran long. The constraint matters — a forwardable executive briefing fits on a phone screen with minimal scrolling.

## What this skill is *not*

Not a news roundup. Not a benchmark recap. Not AGI speculation. **But it IS a tool catalog with judgment.** Include model releases (GPT-5.5, Gemini 3.1 family, Imagen 4, Veo 3, Opus 4.7), product launches (Claude Design, Cursor 3, Perplexity Comet/Deep Research, Images 2.0), and integration updates (Claude for Excel, MCP connectors, Gemini Workspace tie-ins) — these are exactly what consultants need to know about. Leave out pure benchmark movement without operational meaning, and leave out consumer-only features with no professional adjacent use.

## Workflow

Follow these steps in order. Don't skip the meta-trend or the humanizer pass — those are what separate this from a generic AI digest.

### 1. Establish the window and gather material

Today's date is fixed by the environment. Default window: the prior 1–2 calendar months ending the day before today. Confirm with the user if the framing is ambiguous.

Sources of material, in order of preference:
1. **User-provided input** — if the user dumped articles, links, or notes, treat that as the primary source.
2. **Web search** — if no input was provided, use WebSearch / WebFetch. Cast wide initially.

**Required coverage during search.** Before drafting, make sure you've searched for each of these in the window:
- Model releases from OpenAI, Anthropic, Google *(by name — e.g., "GPT-5.5 May 2026", "Claude Opus 4.7", "Gemini 3.1 release")*
- Product launches from each lab *(e.g., "Claude Design", "ChatGPT Images 2.0", "Veo 3 GA")*
- Office / productivity-tool integrations *(Excel, PowerPoint, Word, Notion, Linear, Workspace)*
- Major third-party AI tool updates *(Cursor, Perplexity, Notion AI, GitHub Copilot, NotebookLM, Granola)*
- Regulation and governance *(EU AI Act, MCP/Linux Foundation, sectoral rules)*
- Economics *(token pricing, multi-model routing, enterprise contracts)*

A common failure mode for this skill is to over-index on enterprise-strategy news and miss the actual product releases. The tool releases are not optional — they are the primary content for the consultant audience.

When weighting, **up-weight** anything a working consultant could pick up tomorrow: tools embedded in Office/Workspace, agentic interfaces, deliverable-generating research tools, financial-data integrations, parallel-agent coding tools, image/video/design generation, MCP connectors to professional data sources. **Down-weight** purely consumer features with no professional adjacent use, raw benchmark movement, and AGI commentary.

### 2. Identify the meta-trend (the hardest step — spend real time here)

Before drafting anything else, write the meta-trend. This is one sentence that frames the month's developments through the standing thesis (operational execution, workflow integration, governance, enterprise deployment).

A good meta-trend is:
- **Specific to this month's evidence** — not a generic restatement of the thesis
- **Opinionated** — it takes a position, not "things are changing across the AI landscape"
- **Operational** — it implies a "so what" for how enterprises should behave

If the developments don't obviously support a sharp thesis, that's a signal you need different developments, not a weaker thesis. Go back to step 1 and look for what's actually moving.

**Examples of meta-trend phrasing (illustrative only — do not copy):**
- "Vendor moats are migrating from training runs to enterprise workflow surface area."
- "Governance, not capability, is now the binding constraint on agent deployment."
- "The center of gravity for AI spend is moving from API calls to integration labor."

### 3a. Over-generate the topic menu and have the user select

**Do not draft until the user has selected from a topic menu.** This is a hard requirement, not optional. The skill has repeatedly chosen wrong content in past runs (missed major model releases, over-weighted business strategy, under-weighted tool releases). The selection step exists to catch this before the document is written.

**Over-generate, don't curate.** The goal here is breadth, not your best judgment. Present **at least 10 candidate items per section** wherever the window has them, including marginal calls and items you'd personally cut. The user picks the final set. Your job is to surface candidates, not pre-filter them. If a section genuinely has fewer than 10 candidates *(rare — there's almost always more news than you think)*, present what exists and say so.

**Format the menu so it's fast to mark up.** Use letter codes per section (A, B, C…) and numbered items underneath (A1, A2, A3…). One short descriptive line per item — enough for the user to decide without opening a browser. Group by the standard sections.

```
Proposed topic menu for [Month Year]
Reply with selections like: "A1, A3, A6, B2, B5, B7, C1, C4, D1, D3, D5, E2, E3"

Meta-trend proposal:
"[one-line thesis statement — flag if you want this tuned]"

A. OpenAI
A1. GPT-5.5 (April 23) — full retrained "Spud" model, multimodal, GDPval 84.9%
A2. GPT-5.5 Instant (May 5) — cheaper default in ChatGPT
A3. ChatGPT Images 2.0 (April 21) — image gen with reasoning, multilingual text
A4. Codex desktop app (May 15) — multi-agent coding workspace
A5. Codex + Managed Agents on AWS Bedrock (April 30)
A6. ChatGPT advertising trials announced — early monetization signal
A7. OpenAI Deployment Company JV (May 4) — 19 PE/consulting/SI partners
A8. Tomoro acquisition — 150 Forward Deployed Engineers
A9. [next candidate]
A10. [next candidate]
...

B. Anthropic
B1. Claude Mythos Preview (April 7) — frontier model under Project Glasswing
B2. Claude Opus 4.7 GA (May 4) — 1M context at standard pricing
B3. Claude Cowork GA — agentic local-file system with OpenTelemetry/RBAC
B4. Claude Security GA — data-flow tracing for codebases
B5. Claude Design (April 17) — Figma alternative
B6. Claude for Excel deepened — native ops + financial-data MCP connectors
B7. Claude for Small Business — QuickBooks/HubSpot/etc. integrations
B8. $1.5B JV with Blackstone, Goldman, H&F (May 4)
B9. Amazon 5GW compute agreement (April 21)
B10. Google Cloud $750M ecosystem commitment
...

C. Google
[10+ items]

D. Other Tools Worth Knowing
[10+ items — Cursor, Perplexity, xAI/Grok, Chinese open-weight labs (GLM, Qwen, Kimi, DeepSeek, MiniMax), Notion AI, GitHub Copilot, NotebookLM, etc.]

E. Business & Regulation
[10+ items — vendor deals, regulation, economics, infrastructure, governance moves]

Excluded outright (below the bar — let me know if any of these should be on the menu):
- [Topic] — [one-line reason]
- ...
```

Then wait for the user's selection. Parse it back as a confirmation:

```
Confirmed selections:
- A: A1, A3, A4 (3 entries)
- B: B1, B2, B5, B6 (4 entries)
- ...
Total: [N] entries.

Meta-trend: [confirmed/adjusted]

Drafting now.
```

Per-section length targets (matching the exemplar) for the draft phase: meta-trend block ~200–220 words; entries ~70–95 words each depending on weight; single-big-story entries ~50 words. The user's selection determines section count, but per-entry density should match the exemplar regardless of how many entries land in each section.

### 3b. Verify each confirmed item with a targeted web search

**Do not draft from initial-search summaries alone.** Initial broad searches surface that something happened; they routinely miss the specific numbers, partner lists, dates, pricing, and competitive context that make the Detail accurate. Before drafting, run a targeted search per confirmed item and capture:

- **Exact release/announcement date** (e.g., "May 14" not "May")
- **Real benchmark numbers, not impressions** ("SWE-bench Pro 53.4 → 64.3" not "10–15% lift")
- **Full partner / investor lists with names and dollar amounts**
- **Pricing details** (per token, per seat, per image, etc.)
- **Direct competitive positioning the vendor itself names** (e.g., "Codex catches up to Claude Code's February shipment of Remote Control")
- **Any feature that is genuinely new vs. incremental** (often missed in summaries that bundle "new product line" with "incremental capability lift")

A common failure mode for this skill is to draft from the first round of search results, which produces directionally-correct but factually-wrong content *(wrong partner counts, wrong benchmark numbers, wrong deal sizes, sometimes wrong regulatory framing)*. The targeted verification round is what catches this. If a search reveals the briefing's working frame is wrong *(e.g., a regulatory deadline you assumed was binding has actually been deferred)*, **stop and reframe before drafting** — don't write around the new information.

Verify in parallel batches where possible. If the user has confirmed 12–15 items, run them in 2–3 parallel batches of searches rather than serially.

### 3c. Run the pre-draft validation pass

**Do not draft until this validation pass has run.** This is a structured re-check of everything you've gathered in 3a (topic selection) and 3b (per-item verification). It exists because a series of correct-looking initial searches plus a directionally-confirmed verification round can still produce a briefing with the wrong framing, missing major related stories, or an unsupported throughline. The validation pass catches those before the document is written.

Run through this checklist for each confirmed item, and for the briefing as a whole. Produce a short validation report at the end. If anything is flagged, **fix it before drafting** — re-search where data is fuzzy, reframe where the premise has shifted, add or drop items where balance is off.

**Per-entry checks:**

1. **Source named.** Can you point to a primary or near-primary source *(vendor announcement, regulatory filing, named journalistic outlet)* for the central claim? If the strongest source you have is a third-party blog summarizing someone else's summary, search for the primary.
2. **Date precision.** Do you have the exact release/announcement date *(e.g., "May 14")*, not just a month? Inexact dates are a flag that the entry's substance hasn't been verified.
3. **Numbers grounded.** Every benchmark score, dollar amount, percentage, partner count, and capacity figure traces to a specific source with the same number. Round numbers that don't match the source *(e.g., saying "thousands of partners" when the source says "40+")* are a flag.
4. **Frame matches facts.** Does the framing you plan to use *(in the title and "Why you care")* match the verified facts, or does it carry over a premise from your initial impression that the verification round didn't update? **The EU-AI-Act failure mode lives here**: the initial premise was "August 2, 2026 is binding," verification revealed the deferral had been agreed, but a careless draft could still tell the reader to treat August 2 as binding. Reframe if the facts have moved.
5. **Competitive context surfaced.** If a release is a response to or catch-up against another vendor, is that context named? *(Codex mobile control was OpenAI catching up to Anthropic's February shipment of Claude Code Remote Control — without that frame, the entry undersells the news.)*

**Briefing-level checks:**

6. **Throughline.** Does each entry visibly reinforce or sharpen the meta-trend? If an entry sits there as standalone news with no connection to the throughline, either revise the entry's "Why you care" to draw the connection, drop the entry, or — if multiple entries don't fit — revise the meta-trend.
7. **Completeness within selected scope.** For each lab section the user picked, does the selection cover that lab's most operationally significant releases of the window? An obvious omission *(e.g., the section covers a vendor's model release but misses a same-window product launch from the same vendor)* gets surfaced for a quick re-decision before drafting.
8. **No double-counting.** Cross-references between entries are checked — if a story appears in two sections *(e.g., Anthropic's Google Cloud $750M commitment could land in either Google or Business)*, it's placed once and referenced once.
9. **Regulatory and economics framing checked twice.** Items where the operational implication depends on a current binding state *(deadlines, prices, deal terms)* get a second source. This is where the most damaging factual errors land if missed.

**Output format for the validation pass:**

```
Pre-draft validation pass
=========================

Per-entry status (✅ clean, ⚠️ flag, ❌ blocker):
- A1: ✅
- A3: ⚠️ Frame: I had "Bedrock is the lede" but verification surfaced computer-control as the bigger story — reframing
- B1: ✅
- B2: ⚠️ Numbers: working notes say "10–15% lift" but real benchmark is 53.4 → 64.3 (10.9-point bump on SWE-bench Pro) — updating
- ...

Briefing-level status:
- Throughline: ✅ every entry visibly reinforces the meta-trend
- Completeness: ⚠️ Anthropic section is missing the SpaceX/Colossus compute deal announced same week as Opus 4.7 — proposing to fold into B2

Blockers to fix before drafting: [list, or "none"]
Reframes applied: [list, or "none"]
Re-searches needed: [list, or "none"]
```

If the report contains **blockers** *(missing critical context, framing inversions, factual contradictions across sources)*, fix them — re-search, reframe, or surface to the user for a decision — before moving to drafting. If only **flags** *(minor wording adjustments, single-source claims worth a confirmation)*, address them inline and proceed.

### 3d. Bucket developments

Group selected items into sections. Standard sections (use only the ones with material this month — don't pad):
- **OpenAI** — model releases, ChatGPT product, Codex, API, business moves
- **Anthropic** — Claude releases, Cowork/Security, Office integrations, Anthropic Labs products (Design, etc.), Small Business
- **Google** — Gemini family, Veo, Imagen, Workspace/Gemini Enterprise integrations
- **Other Tools Worth Knowing** — Cursor, Perplexity, GitHub Copilot, NotebookLM, Granola, Notion AI, design/video/research tools consultants actually use
- **Business & Regulation** — material vendor moves, EU AI Act, governance shifts, token economics

Lead with the labs (OpenAI, Anthropic, Google) when their releases are the substantive content. "Other Tools Worth Knowing" is not optional padding — it is where Cursor 3, Perplexity Comet, and similar releases live, and these are often the most directly usable items for a working consultant.

Volume guidance for a <1000 word briefing:
- 12–15 development entries total is typical
- Each entry is short: 1–3 sentence Detail, 1–2 sentence Why you care
- Meta trend block ~150–180 words; longer than that and the briefing won't fit the length budget

### 4. Draft each section

**Before drafting, read `references/exemplar-issue.md`** — a real, user-approved issue. It is the ground truth for formatting. Then consult `references/structure-template.md` for the explicit hierarchy table and inline conventions.

Key formatting points the exemplar establishes (easy to get wrong if you rely on intuition):

- Heading hierarchy is shallow: `### **Meta Trend: …**`, `#### **What's changing**` (and other meta sub-blocks), `#### **OpenAI**` (and other section names).
- **Development titles are bold standalone lines, NOT `###` headings**: `**OpenAI GPT-5.2 released under competitive pressure**`.
- `**Detail:**` and `**Why you care:**` run **inline** with the content on the same paragraph, separated by a space — not on a separate line above the content.
- `------` horizontal rules separate development entries within a section.
- Accessibility clarifications use **italic parentheticals**: `*(short clarification)*`.
- **Bold inline emphasis** on load-bearing terms in the meta-trend and development bodies — one or two per paragraph, never decoration.

**Detail voice is narrative-descriptive, not telegraphic.** Each Detail reads like a briefing intro: "[Name] is [vendor]'s [latest/new] [category]…" followed by an "It excels at…" sentence listing strengths in parallel prose, then closing competitive or historical positioning. See `references/structure-template.md` for the canonical example and the full pattern. Avoid the spec-sheet/data-dump voice — that's a different document.

**Why-you-care voice stays sharp and operational.** Short sentences. Specific actors and decisions. State the implication directly. Don't bleed the narrative Detail voice into Why-you-care — the contrast between the two voices is what makes the briefing scannable. If you can't write a sharp Why-you-care, the development probably doesn't belong in the briefing.

### 5. Apply the voice rules while drafting

Read `references/voice-and-banned-phrases.md` for the full list. The big ones to keep front of mind:

- **Banned phrases:** "at a high level", "it's worth noting", "key consideration", "ultimately", "leverage", "drive value", "holistic", "journey", "foundation", "ecosystem" (except in the document title where it's the proper name of the deliverable), formulaic pros/cons, excessive hedging ("generally", "often", "typically"), overly symmetric formatting.
- **Tone:** Concise. Direct. Opinionated where appropriate. Not corporate. Not enthusiast.
- **Accessibility:** Keep technical terms only where useful. Add a short parenthetical only when a non-technical reader would otherwise stall. Explain in terms of business impact, risk, or execution implications. Do not explain how models work internally unless necessary.
- **No balanced-for-balance conclusions.** If the implication is clear, state it.

### 5.5. Post-draft writing review (mandatory)

Once a complete draft exists, run a structured writing review **before** the humanizer pass. The validation in step 3c catches whether the *facts* are right; this step catches whether the *writing* is doing its job. The two failures look different — factually-correct prose can still be unreadable, padded, or burying the point.

Read each entry as a senior consultant scanning the briefing on their phone, and ask the explicit communication-effectiveness questions: **are we getting the point across? is there too much detail? what do we really need in the text to get the point across?**

**Per-entry checks:**

1. **Lead sentence carries the news.** Can the reader stop after the first sentence of the Detail and still get the gist? If the first sentence is throat-clearing or product-naming without consequence, rewrite it.
2. **Every sentence earns its place.** Walk each sentence: does removing it hurt the point? If no, remove. This is where data-dumps die — benchmark numbers, partner lists, and pricing details belong only where they sharpen the point, not as proof you did your homework.
3. **Parentheticals pull weight.** Italic clarifications *(in this style)* exist to keep non-technical readers from stalling. Each one should answer a real question. If a parenthetical is just adjacent context, cut it.
4. **Why-you-care is operational, not a Detail rerun.** Names a specific actor or decision the reader makes differently because of this. Doesn't restate the Detail in different words. Two sentences, ideally one.
5. **Title still scans as a headline.** Sometimes titles drift toward product names during drafting — verify each title still carries the news, not just the name.

**Briefing-level checks:**

6. **Per-section density matches exemplar.** Each entry roughly 70–95 words across Detail + Why-you-care; single-big-story entries ~50; meta-trend block ~200–220 total. Entries running over 120 words are flagged for trimming.
7. **Voice tells caught.** Quick scan for banned phrases *(see voice-and-banned-phrases.md)*, AI vocabulary creep *("landscape", "additionally", "leverage", "ultimately")*, em-dash overuse, rule-of-three patterns where two would do, formulaic "X. Y. Z." rhythm.
8. **Meta-trend still tight.** The full block is 200–220 words. Each sub-block *("What's changing", "Where value now sits", "Why this matters", "2026 implication")* is short and earns its place. If the meta-trend has bloated, trim.
9. **Throughline reads top-to-bottom.** Scan section by section: does each section's selections reinforce the meta-trend? If a section reads like standalone news, either tighten the Why-you-cares to draw the connection or rethink the meta-trend.
10. **Titles-only scan test.** Read just the bolded titles top to bottom. Does a senior consultant get the issue's argument from titles alone? If titles read as a disconnected list, sharpen them.

**Output format:**

```
Post-draft writing review
=========================

Per-entry status (✅ clean, ⚠️ trim/sharpen, ❌ rewrite):
- A1: ✅
- A3: ⚠️ Detail runs 142 words and buries the news in sentence 3. Tightening.
- B1: ⚠️ Why-you-care restates the Detail. Rewriting for operational sharpness.
- B5: ✅
- ...

Briefing-level status:
- Per-section density: ✅
- Voice tells: ⚠️ Three em-dashes in one paragraph (B2). Replacing two with periods.
- Meta-trend tightness: ✅ (210 words across the block)
- Throughline: ✅
- Titles-only scan: ⚠️ C2 reads as product name. Rewriting.

Trimming applied: [list]
Rewrites applied: [list]
Blockers to fix before humanizer pass: [list, or "none"]
```

**Fix flagged issues before moving to the humanizer pass.** If significant rewrites are applied, the writing review should run again — entries that just got rewritten can introduce new tells.

### 6. Run the humanizer pass (mandatory)

Once a complete draft exists, invoke the humanizer skill via the Skill tool with the draft as the target. The humanizer is the authoritative style policy for the user's global setup — it catches AI-writing tells that surface even when you think you've been careful. Apply its suggestions, then re-read the result for any places where humanizer's edits flattened a deliberately sharp formulation; restore those.

Do not skip this step. The user has explicitly required it.

### 7. Write the file

Save the final briefing to `~/work-docs/ai/reports/` per the global Markdown Deliverable Policy. Filename pattern: `YYYY-MM-DD_HHMM_ai-pulse-<month-year>.md` (use today's date, with the briefing's coverage month in the topic slug, e.g., `2026-05-18_1430_ai-pulse-april-may-2026.md`).

Include the required YAML front matter from the global policy:

```yaml
---
title: AI Ecosystem & Market Update — [Month Year]
topics: [ai, executive-briefing, market-update]
date_created: YYYY-MM-DD
version: 1
purpose: Monthly AI Pulse briefing for senior consultants, operators, and business leaders
audience: Senior consultants, operators, PE teams, business leaders (mixed technical depth)
status: draft
---
```

Below the front matter, include the required human summary block (one-paragraph summary, key topics, scope in/out, assumptions) before the document body begins.

Create the `~/work-docs/ai/reports/` directory if it doesn't exist.

### 8. Report back

Tell the user the file path, the meta-trend you chose (one line), and the sections you included. Do not paste the full briefing into chat — the file is the deliverable. If you made non-obvious editorial cuts (a vendor section you dropped, a major story you excluded because it lacked operational implication), name them in 1–2 lines so the user can push back.

## Quality bar — self-check before reporting done

Read through the draft once more and ask:

1. **Throughline:** Does every section visibly reinforce the meta-trend, or do some items just sit there as news?
2. **Why-you-care specificity:** Can a senior consultant point at any "Why you care" and immediately use it in a client conversation? If you wrote "this matters for enterprise adoption" without saying *how*, rewrite it.
3. **Voice tells:** Did humanizer's pass actually run? Are any banned phrases still present? Are sentences overly symmetric in length and rhythm?
4. **Cuts:** Is there at least one development you considered and rejected? If you kept everything you found, the bar was too low.
5. **Forwardability:** Would a partner at a top consulting firm forward this to a CEO client without editing? If not, what would they cut or sharpen?

If any check fails, fix it before reporting done. The user values sharpness over volume.

## Inputs you can ask for (only if absent and unavoidable)

The user's CLAUDE.md tells you to default to action when intent is clear. So don't pepper them with questions. If genuinely blocked, ask for at most one of:

- The coverage window (only if "the latest" is ambiguous)
- A material dump (only if you cannot reach the web and have no input)

Otherwise, make the call and proceed.

## Reference files

- **`references/exemplar-issue.md`** — a real, user-approved AI Pulse. **Read this first** when drafting. When prose templates and the exemplar disagree on a formatting detail, the exemplar wins. The exemplar shows the canonical heading hierarchy (shallow — `###` for Meta Trend, `####` for sections, bold standalone lines for development titles), inline `**Detail:**` / `**Why you care:**` formatting, italic parenthetical clarifications, bold inline emphasis, and `------` horizontal rules between developments.
- `references/structure-template.md` — the exact document template with heading hierarchy table, inline formatting conventions, and section ordering rules.
- `references/voice-and-banned-phrases.md` — full voice rules, banned phrases, accessibility constraints, and the test for when hedging carries content vs. cushions a missing view.
- `references/content-priorities.md` — what to include vs. deprioritize, the selection test, and the hunting list of underreported categories.
