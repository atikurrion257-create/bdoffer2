# Playbook — QA Gate

## 1. Verdict rules

| Verdict | Conditions |
|---|---|
| **Ship** | No Blockers; Majors documented with owners; every not-verified row has a test assigned; content stress passed or has known, accepted exceptions |
| **Ship with fixes** | No Blockers, but Majors that must be done within the handoff window; every one has an owner and a due point |
| **Not ready** | Any Blocker: unusable on a common device, required content uneditable, broken/missing state, inaccessible interactive element, broken assets on a live surface, or an unverified claim that the client will rely on |

A verdict without an evidence base is not a verdict.

## 2. Responsive matrix (fill per build)

| Dimension | Desktop | Tablet | Mobile | Custom BP |
|---|---|---|---|---|
| Layout primitive behaviour | | | | |
| Typography scale | | | | |
| Spacing rhythm | | | | |
| Navigation | | | | |
| Hero / media (ratio, focal point, weight) | | | | |
| Tables / data | | | | |
| Forms (stacking, input types, tap targets) | | | | |
| Loops / grids (column counts) | | | | |
| Visibility logic (hidden and why) | | | | |
| Interaction states (hover vs touch vs focus) | | | | |
| Sticky / fixed elements | | | | |
| Overflow (horizontal scroll, long words/URLs) | | | | |

Cells accept: pass / fail (with evidence) / **not observable** (with the test). No blank cells.

## 3. Content-stress catalogue (run all that apply)

| Test | What it catches |
|---|---|
| Very long title / heading | Wrapping, overlap, truncation, layout shift |
| Very short title | Awkward spacing, decorative rules that assume length |
| Missing featured image | Broken layout, placeholder gaps |
| Missing excerpt / optional field | Empty regions, orphaned dividers |
| Zero results | Empty state absent or ugly |
| Many results (50–100) | Pagination, performance, layout drift |
| Special characters / RTL text | Font, alignment, truncation |
| Extreme image ratio (portrait in landscape slot) | Cropping, distortion, focal point loss |
| Field with no value (`--`) | Fallback behaviour |
| Long unbroken string (URL, email) | Overflow / horizontal scroll |
| Repeated edits (the client editing twice) | Design collapse, duplicated content |

## 4. Interaction states checklist

Per interactive element: default, hover (where applicable), **focus-visible**, active/pressed, disabled, loading, error, empty/selected. Also: keyboard reachability, logical focus order, focus trap for drawers/dialogs, escape to close, and reduced-motion respect.

## 5. Bug taxonomy (use for categorising findings)

1. Structural · 2. Responsive · 3. Content · 4. Interaction · 5. Accessibility · 6. Performance (spot level) · 7. Consistency (tokens/naming) · 8. Editor experience · 9. Dependency/version fragility · 10. Verification gaps.

## 6. Editability verification questions

- Who is editing after launch, and what exactly will they change?
- Can they do it without a developer — text, images, links, prices, team members, FAQs?
- Can they break the design doing it (style controls exposed as content, free HTML fields)?
- Are field labels and instructions in the client's words?
- Are there places where an editor will predictably want something they cannot reach?

## 7. Reporting format

For each finding: ID · dimension · severity · evidence · why it matters (client terms) · fix · effort (S/M/L) · owner · confidence.
Then: blocking list, non-blocking list, not-verified list with tests, operational steps, sign-off checklist.

## 8. Post-change operational steps (always state these)

1. Regenerate Elementor CSS / clear Elementor cache (`Elementor → Tools → Regenerate Files & Data`, or the CLI equivalent).
2. Clear page/object caches and any CDN.
3. Re-check dynamic template previews with a real post selected.
4. Re-check the affected breakpoints, not just desktop.
5. Confirm nothing else uses the changed template/class/global element.

## 9. Common QA misses (check deliberately)

- Only desktop was reviewed.
- States (hover/focus) were never designed, only the default.
- The client's *actual* content differs from the demo content.
- A shared template was edited and other pages changed silently.
- A global class/variable change rippled across the site.
- Cache/CSS was regenerated but the CDN was not.
- Keyboard-only navigation was never tried.
- The build was verified as "looks right" rather than against the spec.
