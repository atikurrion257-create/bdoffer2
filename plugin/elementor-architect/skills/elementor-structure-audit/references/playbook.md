# Playbook — Structure Audit

## 1. Audit method

Work outside-in, evidence-first:

1. Completeness and scope (what is present, what is not).
2. Structural validity (keys, types, ids, dialect).
3. Quantitative inventory (counts, histograms, depth, sizes).
4. Behavioural questions in order of client impact: **can they edit it → does it hold on real content → does it survive on mobile → will it still work in a year**.
5. Findings distilled and ranked; then the not-determinable list.

Never lead with aesthetics. Lead with what will hurt the client.

## 2. Severity definitions

| Severity | Test | Examples |
|---|---|---|
| **Blocker** | The client cannot use or maintain the site as intended, or it breaks on realistic content | Page-sized HTML widget; hardcoded content that must be edited; image-only layout; iframe reproduction; no Theme Builder architecture on a content site |
| **Major** | Significant maintenance/performance/consistency cost; certain future rework | Fake nesting; flattened layouts; duplicated styling; no responsive overrides; missing empty states; undocumented dependencies; conditions applied site-wide |
| **Minor** | Quality/consistency; cheap to fix | Deprecated sections in a new document; unused anchors; minor off-scale values |
| **Note** | Preference or future consideration | Alternative widget choice; naming style |

## 3. Editability analysis (the question clients actually care about)

For each content-bearing element ask: *who changes this, how often, and can they?* Then classify:

| Class | Definition | Fix |
|---|---|---|
| Editable in the editor | Has a control the role can use | — |
| Editable but unsafe | Control exists but breaks layout/design if misused (e.g. style fields exposed as content) | Move to tokens/fields; constrain |
| Trapped in code | Lives inside an HTML widget, custom CSS, or a page-level snippet | Rebuild natively |
| Hardcoded where dynamic is required | Should come from a field/option but is a literal | Field + dynamic tag |
| Duplicated literal | Same value in several places | Single source (option/field) |

## 4. Dynamic-content analysis

- Identify `__dynamic__` usage (LIKELY format; confirm from a real export).
- Flag content that *looks* dynamic-ready but is static: repeated CTAs, contact details, prices, testimonial content, feature lists.
- Flag dynamic fields with no fallback (missing image, empty excerpt, absent meta).
- Note the preview-context trap: templates without a preview post render empty/dash — that is a workflow issue, not a structural defect; say so.

## 5. Reference-export diffing (how confidence actually rises)

If the user supplies an export from the same site/version:

1. Build the set of `elType`s, `widgetType`s and settings keys actually present.
2. Compare anything the other skill intends to recommend or emit against that set.
3. Report: *seen in your export* (CONFIRMED for this site) vs **not seen in reference export** (do not claim it is valid or invalid — ask).
4. Never upgrade a LIKELY control-ID claim to CONFIRMED without this diff.

## 6. Reporting language

- Use "defect" / "preference" explicitly.
- Quantify: "37 of 210 elements are wrapper-only" beats "lots of nesting".
- Give the *why it matters* in client terms ("every price change needs a developer").
- Give the fix as the native alternative, with effort band (S/M/L).
- For each Blocker, state the handoff consequence.
- Never use "invalid" for something merely unusual.
- Close with the cheapest tests for what could not be determined.

## 7. Common audit questions and where to look

| Question | Look at |
|---|---|
| "Is it native?" | `html`/`shortcode` footprint, widget histogram, custom CSS, sections vs containers |
| "Can the client edit it?" | Hardcoded literals, HTML widget ownership, duplicated values |
| "Will it hold up?" | Empty states, long-content risk, fixed heights, absolute positioning |
| "Will it work on mobile?" | `_tablet`/`_mobile` keys, custom-CSS responsive rules, tap targets |
| "Can I import this?" | Tier rules, dependency list, media/class/dynamic references, version compatibility |
| "Why is it slow?" | Hand off to `site-quality-review`; note DOM/nesting/asset signals in the structure section |

## 8. Audit anti-patterns to avoid committing yourself

| Anti-pattern | Fix |
|---|---|
| Finding manufacturing (padding the report) | Only evidential findings; cap at ~10 ranked findings plus notes |
| Style opinions dressed as defects | Label them preferences or drop them |
| Ignoring the business context | Ask what the page is for; severity depends on it |
| Claiming to have validated what you only saw in part | Use the digest layers and state them |
| Rewriting the artifact instead of reporting | Report per finding; rewrite only on request |
