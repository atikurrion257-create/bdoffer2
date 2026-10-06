# Structural Digest Protocol (large artifacts)

**verified against:** this project's own design, 2026-10-06. Use whenever a JSON/HTML/export is too large to reason about in one pass — a 4,000-element page, a full kit, a long HTML document.

Analysing everything at once burns context, produces shallow findings, and invites invented detail. Work in layers, and say which layer you are in.

## Layer 0 — Inventory (cheap, highest signal)

Report, before judging anything:

- Artifact type (page JSON / template JSON / kit listing / HTML / CSS) and whether it is complete.
- Dialect: `container`/`section`/atomic `elType`s / `widgetType` patterns.
- Element counts: total, per `elType`, per `widgetType` (histogram, top 15).
- Nesting depth: max, distribution, and where the deep chains are.
- `isInner` distribution (sanity).
- Settings footprint: which elements carry large `settings` objects; size of the biggest few.
- Custom-code footprint: `html`/`shortcode` widgets and their settings size; custom CSS presence; inline `<style>`/`<script>`.
- Dynamic footprint: `__dynamic__` presence/count.
- Repeater usage: which settings are arrays of objects (and whether items have `_id`).
- Media references: count and obvious breakage (external URLs vs IDs).

If Layer 0 alone answers the question, stop there.

## Layer 1 — Skeleton

Output the element tree with **types and IDs only** (no settings), truncated to a stated depth, plus counts per branch. This is what makes structure visible: nesting archaeology, flattened layouts, wrapper-only containers, dialect mixing.

Ask the user to confirm the skeleton matches what they expect before deep analysis — this catches "wrong file / partial paste" errors early.

## Layer 2 — Targeted dives

Fetch full settings only for the elements Layer 0/1 flagged:

- every `html`/`shortcode` widget (the biggest risk),
- elements whose settings exceed a size threshold,
- the deepest chains,
- repeaters with suspicious or missing `_id`s,
- every element with dynamic bindings,
- the section the user actually asked about.

Quote the relevant fragment when reporting, so the user can verify.

## Layer 3 — Spot checks

Sample a handful of unflagged elements to test your conclusions (are the "clean" sections really clean?). State the sample size. If a pattern found in Layer 2 appears in the sample, the problem is systemic — say so.

## Rules

1. **State the layer** you are in and what you are deliberately not looking at yet.
2. **Never summarise settings you have not seen.** "Not analysed" is a valid answer.
3. **Ask for chunks rather than guessing.** If the paste is truncated, say which part is missing and what to send.
4. **Carry counts, not impressions.** "37 of 210 elements are wrapper-only" beats "there is a lot of nesting".
5. **End with what remains unexamined** and whether it could change the verdict.

## Triggers

Use this protocol automatically when: the artifact exceeds roughly a few hundred elements; the paste looks truncated; the user says "big file"; an export contains multiple templates; or a kit/export listing is involved.
