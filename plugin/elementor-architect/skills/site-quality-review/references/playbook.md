# Playbook — Site Quality Review

## 1. Performance: check before you advise

| Already-shipped Elementor capabilities (verify per version) | Implication |
|---|---|
| Improved / conditional CSS loading (per-widget) | Do not claim "Elementor loads all CSS everywhere" |
| Per-widget asset loading / conditional scripts | Widget choice still matters, but bloat is reduced |
| Optimized Markup (one wrapper instead of two) | Wrapper count advice must account for it |
| global.css elimination (3.25) and conditional library loading (3.26) | Old optimisation advice is stale |
| Optimized DOM output merged into defaults | Verify before recommending experiments |

Then review: assets (images, fonts), DOM size and nesting, JS weight and third parties, LCP element handling, CSS print method, caching/CDN ownership.

**Targets (use as guidance, not law):** LCP ≤ 2.0 s (Google "good" ≤ 2.5 s), INP ≤ 150 ms (≤ 200 ms), CLS ≤ 0.05 (≤ 0.1), measured at p75 of field data. Practical budgets: JS < ~300 KB compressed, CSS < ~80 KB compressed, hero image < ~200 KB, page weight < ~1.5 MB. Present these as targets with the buffer rationale.

**Never** state measured values you did not measure. Frame as "hypothesis" + "how to measure".

## 2. SEO checklist (structure, not plugin settings)

- One `h1`; logical heading order; headings describe content rather than styling.
- Landmarks present (`header`, `nav`, `main`, `footer`), one `main`.
- Meaningful link text; no "click here"; internal linking to relevant pages/archives.
- Slug/URL architecture decided pre-build; redirect map for every changed URL on a redesign.
- Indexability decisions made deliberately: archives, taxonomy pages, filtered/paginated URLs, search results, thin template pages.
- Schema ownership stated (theme, SEO plugin, or builder feature) — never two systems emitting the same type.
- Template-driven duplicate content identified (e.g. near-identical archive pages).
- Image alt policy: decorative vs informative; no keyword stuffing.
- Canonical and pagination behaviour verified, not assumed.

## 3. Accessibility checklist (WCAG 2.1/2.2 AA behaviours as the review standard)

Keyboard: full path reachable; logical focus order; **visible focus**; escape closes dialogs/drawers; focus trapped where needed; no hidden-but-focusable elements.
Structure: correct heading order; landmarks; lists/tables semantically built; forms labelled with errors associated.
Visual: text contrast; UI component contrast; states distinguishable without colour alone; target sizes (44 px guidance); motion respects `prefers-reduced-motion`; carousels pause/advance controls.
Content: alt text; captions/transcripts for media; link purpose clear from context.
Testing limits: state clearly that automated review cannot verify screen-reader experience, and recommend assistive-technology testing for compliance-bound work.
Escalation: public sector, education, health, enterprise, or any client with a dated compliance obligation → accessibility findings are **Blockers**.

## 4. Decision rules (apply to every finding)

| Decision | When | Example |
|---|---|---|
| **Flag only** | Impact uncertain or out of scope | Unidentifiable third-party script |
| **Recommend** | Clear improvement, moderate risk, needs a decision | Self-hosting fonts; enabling an asset-loading optimisation; adding dimensions |
| **Prepare for approval** | Clear win, low risk, reversible, staging-verifiable | Fixing heading order; replacing a hardcoded value with a dynamic tag; removing a redundant wrapper layer |
| **Defer** | Change would fight the current stack or the site is mid-launch | Cache/minify/CDN settings; URL restructuring; schema ownership; global font swaps |
| **Do not touch** | Outside the mandate without explicit instruction | SEO plugin configuration; security configuration; hosting |

Prioritisation formula: **impact × confidence ÷ risk of change**, with a hard cap of ~5 items in "do this now".

## 5. Measurement plan template

| Question | Method | Where | Owner |
|---|---|---|---|
| Field LCP/INP/CLS | Field data (CrUX/PSI) at p75, mobile | Live URL | — |
| Lab performance | Lighthouse/PSI run on a cold cache | Staging/live | — |
| Real breakpoints | Device/screenshot check at 390/768/1025/1440 | Preview URL | — |
| Accessibility | Keyboard-only pass + one screen reader (NVDA/VoiceOver) | Preview URL | — |
| SEO | Crawl + Search Console after launch | Live | — |

## 6. Reporting anti-patterns to avoid

- The 40-finding dump with no priorities.
- Recommending changes that fight the host's cache layer.
- Copying generic Core Web Vitals advice without connecting it to this page's actual LCP element.
- Duplicating a structural audit's findings (hand off instead).
- Claiming compliance.
- Forgetting the "do not touch" list — it is often the most valuable section of the report.
