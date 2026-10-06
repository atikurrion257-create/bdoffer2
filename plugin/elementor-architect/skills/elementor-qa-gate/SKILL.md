---
name: elementor-qa-gate
description: >
  The pre-delivery quality gate for an Elementor build. Verifies spec conformance,
  responsive behaviour across the site's actual breakpoints, editability, content stress
  cases (long, short, missing, empty, many), interaction states, dynamic-content behaviour,
  semantic structure and asset integrity, then returns a Ship / Ship-with-fixes / Not-ready
  verdict with blocking versus non-blocking findings and a sign-off checklist. Use when the
  user asks for QA, a final review, a responsive or desktop/tablet/mobile check, or whether
  a build is ready for production or client handoff. Do NOT use to discover architecture
  problems in a plan (use elementor-native-architecture), to analyse JSON structure
  (use elementor-structure-audit), or for performance/SEO/accessibility depth
  (use site-quality-review).
---

# Elementor QA Gate

Your job is to prevent an embarrassing handoff — not to admire the build. Every "pass" you issue must be something you actually verified.

## When to use

- "QA this", "final review", "ready to ship?", "check it before I hand it over".
- Responsive / breakpoint review.
- Editability verification ("can the client edit this safely?").
- Post-build regression check after changes.

## When NOT to use

Architecture planning; structural JSON analysis; deep performance/SEO/a11y (those findings can be folded in from `site-quality-review`, but the work happens there).

## Inputs

- Build artifacts and/or screenshots **per breakpoint** (state clearly when these are missing).
- The site's actual breakpoints (including custom ones) — ask if unknown.
- The blueprint/spec to check against, if one exists.
- Support matrix (browsers/devices) and content source.
- Who will edit this after launch, and what they are expected to change.

## Workflow

1. **Establish the baseline.** What is being checked against (blueprint, design, or the user's stated intent)? What evidence do you have? List the gaps before starting.
2. **Spec conformance.** Section by section: does the build match the agreed structure, and where it deviates, is the deviation recorded and justified?
3. **Responsive matrix.** Run `references/playbook.md` §2 dimensions × the site's breakpoints. Mark any row you cannot observe as *not observable from provided evidence* — never as a pass.
4. **Interaction states.** Hover, focus-visible, active, disabled, loading, error, empty, selected. Missing focus visibility is a Blocker for compliance-bound clients and a Major otherwise.
5. **Content stress tests.** Long title, short title, missing image, missing excerpt, no results, 100 results, special characters/RTL text, extreme image ratio, field with no value.
6. **Dynamic content behaviour.** Fallbacks, preview-context rendering, empty states, and the preview-post requirement for templates.
7. **Editability.** Can the role that will own the page make the changes they will actually need (text, images, links, prices, team members) without a developer?
8. **Semantics & accessibility spot checks.** Single `h1`, logical heading order, landmarks, focus path, alt text, contrast at a glance, tap targets, reduced-motion handling.
9. **Asset integrity.** Broken/missing images, oversized media, missing dimensions (CLS), format, LCP image handling.
10. **Regression risk.** What else could this change have affected — shared templates, global widgets/components, global styles, classes, conditions, loops?
11. **Post-change operational steps.** Regenerate CSS / clear caches / re-check dynamic previews — list the exact steps.
12. **Verdict.** Ship / Ship with fixes / Not ready. Blocking list, then non-blocking. Sign-off checklist. Use `assets/qa-report-template.md`.

## Output contract

1. Verdict + one-line reason.
2. Evidence base: what was reviewed vs what was not.
3. Findings by dimension and severity, each with evidence and fix.
4. Blocking list (must fix before handoff) and non-blocking list.
5. Responsive matrix with explicit not-observable rows.
6. Content-stress results.
7. Regression risk list.
8. Post-change operational steps.
9. Sign-off checklist.
10. Confidence ledger.

## Hard rules

- **Never issue a "pass" for anything you could not observe.** Mark it *not verified* with the cheapest test to verify it.
- **Blockers must be evidenced.** Aesthetics are Notes at most.
- **Blockers are reserved for** things that embarrass the agency or break the client's workflow: unusable on a common device, uneditable required content, broken/absent states, accessibility failures on interactive elements, missing or broken assets on a live surface.
- **Never claim WCAG conformance** or measured performance numbers. Say what the structure implies and what still needs testing.
- Always include the operational steps people forget (CSS regeneration, cache clearing, preview context).
- Do not fix things silently; report, then act only when asked.

## References

- `references/playbook.md` — QA matrix, content-stress catalogue, bug taxonomy, verdict rules.
- `references/verification-taxonomy.md` — confidence labels.
- `references/anti-pattern-catalogue.md` — to recognise structural causes behind QA failures.
- `assets/qa-report-template.md` — report format.
- `references/house-standard.md` — the agency's own breakpoints, budgets and escalation rules.

## Hand-offs

- Structural defect → `elementor-structure-audit`.
- Architecture flaw → `elementor-native-architecture`.
- Content/editability strategy → `acf-dynamic-content-plan`.
- Performance / SEO / accessibility depth → `site-quality-review`.

## Failure handling

- **No screenshots or URL** → produce an *evidence-limited QA*: a manual checklist, explicit unknowns, and **no** Ship verdict.
- **Only desktop evidence** → state that mobile/tablet behaviour is unverified; request the missing breakpoints.
- **User wants a verdict for a client** → never inflate; give the honest verdict with the blockers that exist.
- **Build is mid-flight** → QA the finished sections only and mark the rest out of scope.
