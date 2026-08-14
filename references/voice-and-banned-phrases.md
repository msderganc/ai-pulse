# Voice, Tone, and Banned Phrases

The AI Pulse has a specific voice. Most "AI writing" tells leak in unconsciously — this file exists to make them conscious.

## Voice in one paragraph

Concise, direct, opinionated where warranted. The writer is a senior person who has seen many cycles, has views, and respects the reader's time. Professional but not corporate. Operationally fluent — they talk about enterprise deployment, governance, and economics the way an experienced consultant does, not the way an AI enthusiast does. They will say "this is the wrong way to think about it" when it is.

## Audience accessibility

- The reader is intelligent but technical depth varies. Some are deeply technical; some are CFOs.
- Keep technical terminology only where it's load-bearing.
- The canonical accessibility pattern is the **italic parenthetical**: `*(short clarification)*`. Use it whenever a term might stall a non-technical reader. Examples from the exemplar: "*(a working memory roughly equivalent to hundreds of pages of text at once)*", "*(systems that write, review, and modify software)*", "*(those affecting safety, financial outcomes, or regulated decisions)*". One short clause, italicized, in parentheses, inline.
- Italics signal "this is a clarification, skip if you don't need it" — exactly how senior technical readers scan the document.
- Explain in terms of business impact, workflow change, risk, or execution implications. Never in terms of how models work internally — unless that mechanism is itself the story.
- Avoid multi-sentence asides explaining model architecture.

## Banned phrases (hard list — do not use)

These phrases are AI-writing tells. They appear in the user's original prompt as explicitly disallowed.

- "At a high level"
- "It's worth noting"
- "Key consideration"
- "Ultimately"
- "Leverage" (as a verb meaning "use")
- "Drive value"
- "Holistic"
- "Journey"
- "Foundation" (as in "lay the foundation for…")
- "Ecosystem" — exceptions: (1) the deliverable's own title "AI Ecosystem & Market Update" is the proper name and stays; (2) section names that describe cross-vendor developments (e.g., "Cross-Vendor / Ecosystem Developments") are fine when "ecosystem" genuinely refers to the multi-vendor system of interdependent actors. Don't use it in body prose as a vague stand-in for "industry" or "space".

## Banned moves (patterns, not phrases)

- **Formulaic pros/cons.** No "Benefits / Drawbacks" lists. If there's a tradeoff, write a sentence.
- **Excessive hedging.** Strike "generally", "often", "typically", "in many cases" unless precision genuinely depends on them. If you find yourself hedging three times in a paragraph, you don't have a view yet — go form one. Note: controlled, content-carrying softeners are fine — the exemplar uses "Many organizations believe the hard part of AI adoption is behind them" because the *content* of the claim depends on it being many-not-all. The test: does the hedge carry information, or is it cushioning a confident assertion the writer is afraid to make? Cushioning gets cut; informational hedging stays.
- **Overly symmetric formatting.** Don't make every section the same length. Don't open every paragraph with the same sentence shape. Vary rhythm.
- **Repetitive sentence structures.** Watch for the "X. Y. Z." rule-of-three pattern, parallel "-ing" constructions ("driving X, enabling Y, transforming Z"), and the AI habit of pairing every claim with its mirror ("not just X, but Y").
- **Balanced-for-balance conclusions.** No "time will tell", "on the other hand", or "both sides have merit" when one side is clearly stronger. Take the position.
- **Generic consulting narration.** "Organizations should consider…" is filler. Say *which* organizations, *which* consideration, and *why now*.
- **AI cliché vocabulary.** "Unlock", "transform", "empower", "harness", "navigate", "paradigm shift", "game-changer", "next-generation" — kill on sight.

## Words and phrases to be suspicious of (not banned, but flag for review)

These often signal AI writing but occasionally earn their place. Use deliberately, not by default:

- "Robust", "seamless", "comprehensive", "scalable", "innovative"
- "Cutting-edge", "state-of-the-art"
- "It is important to…", "It should be noted…"
- "In today's…", "In the current landscape…"
- "Going forward", "moving forward"
- "Significant" used to mean "big" (it has a statistical meaning that gets diluted)

## Punctuation, rhythm, and inline emphasis

- **Em dashes are fine but not as a tic.** AI writing tends to use them every other sentence as a connector. Reserve them for genuine parenthetical asides or sharp interruptions. If a draft has em dashes in three consecutive paragraphs, replace at least two with periods, commas, or restructured sentences.
- **Sentence length variation.** A briefing where every sentence is 18–24 words reads like AI. Mix short declaratives with longer analytical sentences.
- **No oxford-comma-rule-of-three lists where two examples would do.** "Workflows, governance, and economics" is fine when you mean all three; not when you mean "workflows and governance".
- **Bold inline emphasis on load-bearing terms.** Bold the nouns and phrases that carry the operational signal — "**workflows**", "**governance**", "**context window of up to 1 million tokens**". One or two bolded phrases per paragraph is typical. More than three per paragraph reads like a marketing deck. Don't bold for decoration.

## Opinion calibration

The briefing is opinionated, not contrarian for its own sake. Calibration:

- **State implications directly.** "This means PE-owned services firms will see margin pressure within 12 months" — not "this could potentially impact services margins over time".
- **Don't editorialize the vendors.** No "OpenAI continues to dominate" or "Google is finally catching up" framing. Describe what they did and what it changes.
- **Distinguish "we think" from "everyone agrees".** If you're taking a position that's not the consensus, you can say so without breaking voice — "the conventional read is X; we'd argue Y because Z" is fine when warranted.

## The humanizer relationship

After the draft is complete, the humanizer skill runs a pass that catches AI tells from a broader policy (the user's authoritative style policy). Treat humanizer as a backstop, not a substitute for following these rules during drafting. If humanizer flattens a deliberately sharp formulation during cleanup, restore the original — its job is to remove tells, not to neutralize voice.

Three of humanizer's rules are exempted here because they collide with the AI Pulse format rather than with AI tells: §16 (inline-header lists) would strip the `**Detail:**` / `**Why you care:**` labels, §15 (boldface) would strip the load-bearing emphasis described above, and §14's dash ban would strip en dashes from date ranges, numeric ranges, and prices. Em dashes in prose stay subject to §14. See SKILL.md step 6 for how to invoke it. Everything else in humanizer applies in full — and several of its patterns *(rule-of-three, negative parallelisms, AI vocabulary, hedging)* overlap with this file, so a hit there is a hit here.
