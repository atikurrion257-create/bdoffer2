# QA Report Template

> Copy into the deliverable. Delete guidance lines. Never fill a cell you did not observe.

## Verdict

| | |
|---|---|
| **Verdict** | Ship / Ship with fixes / Not ready |
| **Reason (one line)** | |
| **Reviewer** | |
| **Build version / date** | |

## Evidence base

| Item | Provided? | Notes |
|---|---|---|
| Blueprint / spec | | |
| Desktop evidence | | |
| Tablet evidence | | |
| Mobile evidence | | |
| Custom breakpoint evidence | | |
| Site breakpoints (exact values) | | |
| Support matrix | | |
| Who edits after launch | | |

**Scope note:** *(what was reviewed; what was out of scope; what could not be observed)*

## Blocking findings (must fix before handoff)

| ID | Dimension | Finding | Evidence | Why it blocks | Fix | Effort |
|---|---|---|---|---|---|---|

## Non-blocking findings

| ID | Severity | Dimension | Finding | Evidence | Fix | Effort | Owner |
|---|---|---|---|---|---|---|---|

## Responsive matrix

| Dimension | Desktop | Tablet | Mobile | Custom BP |
|---|---|---|---|---|
| Layout primitive behaviour | | | | |
| Typography scale | | | | |
| Spacing rhythm | | | | |
| Navigation | | | | |
| Hero / media | | | | |
| Tables / data | | | | |
| Forms | | | | |
| Loops / grids | | | | |
| Visibility logic | | | | |
| Interaction states | | | | |
| Sticky / fixed | | | | |
| Overflow | | | | |

Values: **P** (pass, observed) · **F** (fail, evidenced) · **?** (not observable — list the test below).

## Content-stress results

| Test | Result | Evidence |
|---|---|---|
| Long title | | |
| Short title | | |
| Missing image | | |
| Missing optional field | | |
| Zero results | | |
| Many results | | |
| Special characters / RTL | | |
| Extreme image ratio | | |
| Empty value (`--`) | | |

## Interaction states

| Element | Default | Hover | Focus-visible | Active | Disabled | Loading | Error |
|---|---|---|---|---|---|---|---|

## Editability verification

| Content the client must change | Can they? | How | Risk |
|---|---|---|---|

## Accessibility spot checks

| Check | Result | Notes |
|---|---|---|
| Single `h1`, logical order | | |
| Landmarks | | |
| Focus visibility / order | | |
| Contrast (text, UI) | | |
| Alt text policy | | |
| Tap targets ≥ 44 px | | |
| Reduced motion | | |

## Regression risk

| Area | Risk | Why | Mitigation |
|---|---|---|---|

## Not observable — tests required

| Unknown | Cheapest test | Owner |
|---|---|---|

## Post-change operational steps

1. [ ] Regenerate Elementor CSS / clear Elementor cache
2. [ ] Clear page/object cache and CDN
3. [ ] Re-check dynamic template previews with a real post
4. [ ] Re-check affected breakpoints
5. [ ] Confirm nothing else uses the changed template/class/global element

## Sign-off checklist

- [ ] No Blockers outstanding
- [ ] Every Major has an owner and a deadline
- [ ] Every "?" row has a test assigned
- [ ] Content stress passed or exceptions accepted in writing
- [ ] Client's own editor has been tested against real content
- [ ] Rollback path known

## Confidence ledger

| Claim | Label |
|---|---|
