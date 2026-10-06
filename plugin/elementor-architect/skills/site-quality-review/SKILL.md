---
name: site-quality-review
description: >
  Version-aware, non-destructive review of performance and Core Web Vitals, SEO and
  accessibility for a page, site, or Elementor artifact. Produces one prioritised findings
  register where every item carries an explicit decision: flag only, recommend, prepare for
  approval, defer, or do not touch. Use for performance audits, Core Web Vitals questions,
  SEO structure reviews, accessibility checks, "why is this slow?", or "is this
  accessible/compliant?". Do NOT use for structural audits of Elementor JSON or templates
  (use elementor-structure-audit), for pre-delivery QA verdicts (use elementor-qa-gate), or
  for architecture planning (use elementor-native-architecture).
---

# Site Quality Review (Performance · SEO · Accessibility)

These are three professions. Your job is a competent, prioritised review — not blanket optimisation, and never a claim you cannot evidence.

## When to use

- Performance / Core Web Vitals review.
- SEO structure review (not plugin settings).
- Accessibility review, including compliance-bound clients.
- Pre-launch quality sweep.

## When NOT to use

Structural auditing of JSON/templates; QA verdicts; architecture planning.

## Inputs

- A URL, HTML, screenshots, a Lighthouse/PSI export, or artifacts to review. **Ask for one if you have nothing** and say what it would change.
- Hosting/caching/CDN stack, and which Elementor performance features are already active.
- Client context: industry, compliance obligations (public sector/education/health → accessibility escalation), traffic priorities.
- Stage: pre-launch or live, and what must not change right now.

## Workflow

1. **Scope and stage.** What is being reviewed, and what must remain untouched (cache config, SEO plugin, hosting)?
2. **Performance.** First establish what is *already* enabled (improved/conditional CSS loading, per-widget asset loading, Optimized Markup, CSS print method, caching/CDN, font strategy). Then review assets, DOM size, JS weight, third-party scripts, images, and font delivery. Separate **advice** from **measurement** — never invent field numbers.
3. **SEO.** Headings and semantics; slugs and URL architecture; indexability of archives, filters and pagination; redirect risk on redesigns; schema ownership; internal linking; duplicate-content risks from templates.
4. **Accessibility.** Keyboard path and focus visibility; contrast; heading order; landmarks; forms and labels; alt text policy; target sizes; motion; carousel/dialog behaviour; hidden-but-focusable traps. Escalate severity for compliance-bound clients.
5. **Apply the decision rules** (`references/playbook.md` §4) to every finding: flag only / recommend / prepare for approval / defer / do not touch.
6. **Prioritise** by impact × confidence ÷ risk of change. Cap the "do this now" list at ~5 items.
7. **Produce a measurement plan** for anything requiring real data (field CWV, screen-reader testing, lab runs).
8. **Output** using `assets/quality-report-template.md`.

## Output contract

1. Scope, evidence, and stage.
2. Findings register: severity, evidence, impact hypothesis, effort, risk, **decision**.
3. Top actions (max ~5) with reasons.
4. Deferral list with the trigger that should reopen each item.
5. **Do-not-touch list** (things that would fight the cache/SEO/security stack or destabilise a launch).
6. Measurement plan.
7. Confidence ledger.

## Hard rules

- **Never claim measured CWV or conformance.** No "Lighthouse is X", no "passes WCAG". State what structure implies, and what still needs testing.
- **Never recommend changing SEO or security plugin configuration** unilaterally; recommend and defer to the owner.
- **Do not repeat outdated Elementor performance myths** (e.g. "Elementor always loads a 500 KB stylesheet"). Check which optimisations are active in this version first.
- **A long unprioritised list is a failed review.**
- **Accessibility items for compliance-bound clients are blockers, not notes.**
- **Do not touch production** — this skill is read-only; changes are prepared elsewhere with approval.
- Give each finding a real reason it matters *to this client*, not a generic best-practice quote.

## References

- `references/playbook.md` — performance rules and thresholds, SEO checklist, accessibility checklist, flag/recommend/defer rules, measurement plan guidance.
- `references/verification-taxonomy.md`, `references/house-standard.md`.
- `assets/quality-report-template.md` — report format.

## Hand-offs

- Structural causes (DOM, nesting, widget bloat, hardcoded content) → `elementor-structure-audit` or `elementor-native-architecture`.
- Final handoff verdict → `elementor-qa-gate`.
- Content/editability causes → `acf-dynamic-content-plan`.

## Failure handling

- **No URL and no evidence** → ask for one artifact (URL, HTML, screenshots, PSI export); otherwise deliver a self-review guide, not a verdict.
- **"Make my site faster" with no boundary** → scope it: one page, one metric, one stage.
- **Live site mid-campaign** → defer anything with layout/URL risk; produce the deferral list as the main output.
- **Client demands a compliance statement** → explain what was and was not tested; recommend assistive-technology testing.
