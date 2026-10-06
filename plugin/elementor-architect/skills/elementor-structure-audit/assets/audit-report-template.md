# Audit Report Template

> Copy into the deliverable. Delete guidance lines.

## Verdict (2–4 lines)

*Plain language: what this artifact is, what is sound, what is not, and the single most important thing to fix.*

## Evidence base

| Item | Value |
|---|---|
| Artifact type | page JSON / template JSON / kit listing / builder paste / HTML |
| Completeness | complete / partial (what is missing: …) |
| Size | elements: __ · deepest nesting: __ |
| Dialect | V3 / V4 / mixed / undetermined |
| Version context | Elementor ___ · Pro ___ *(or: unknown → version-sensitive findings labelled)* |
| Reference export supplied | yes / no *(changes confidence)* |
| Method | layers used (see structural-digest-protocol) |

## Findings register

| ID | Severity | Category | Finding | Evidence (element id/path) | Why it matters | Native alternative | Effort | Defect / Preference | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| F1 | Blocker | A1 page-sized HTML widget | 1 html widget holds 78% of the page | `#a1b2c3` | Client cannot change copy without code; no responsive control | Rebuild with containers + widgets; keep only the map embed scoped | L | Defect | CONFIRMED |

Severity: Blocker / Major / Minor / Note. Categories: structure · content & editability · styling · interaction · site/Theme Builder · responsive · dependencies · verification.

## Structural map

```
page
├─ container #6af611eb (hero)          12 elements, depth 4
│   └─ …
└─ html #a1b2c3 (page body)            1 element, settings 41 KB ⚠
```

## Inventory

| Metric | Value | Note |
|---|---|---|
| Total elements | | |
| Max nesting depth | | |
| `html` / `shortcode` widgets | | settings size |
| Custom CSS present | | |
| Dynamic bindings | | |
| Repeat settings keys (duplication) | | |

## Widget histogram

| `widgetType` | Count | Share | Core / Pro / add-on |
|---|---|---|---|

## Reference-export diff (if supplied)

| Claim | Seen in reference? | Status |
|---|---|---|
| `xxx` setting key | yes / no | CONFIRMED for this site / not seen in reference export |

## Top 5 fixes (ranked)

1. *(fix)* — why: *(client impact)* — effort: S/M/L
2. …

## Cannot be determined from this artifact

| Unknown | Cheapest test |
|---|---|
| Rendering at 390 px | Screenshot at 390 px |
| Whether the map iframe is third-party | Check the embed source |

## Confidence ledger

| Claim | Label |
|---|---|

## Recommended next step

*(one line: rebuild one section, import test on staging, hand off to QA, etc.)*
