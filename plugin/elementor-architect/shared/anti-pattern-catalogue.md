# Anti-Pattern Catalogue

**verified against:** Elementor 3.24–4.3 docs, ACF/Elementor integration guidance, practitioner evidence, 2026-10-06.

The failure signatures below are what AI-generated — and rushed human — Elementor work looks like. Each entry: what it looks like in an artifact, why it hurts, severity, and the native alternative. Use this as the primary lens for audits of AI-built pages.

## Severity scale

| Level | Meaning | Handoff impact |
|---|---|---|
| **Blocker** | The client cannot use or maintain the site as intended; or the page will break on realistic content | Must fix before handoff |
| **Major** | Significant maintenance, performance or consistency cost; will cause future rework | Fix before or immediately after handoff |
| **Minor** | Quality/consistency issue; cheap to fix | Fix when convenient |
| **Note** | Preference or future consideration | No action required |

---

## A. Structure

**A1 — Page-sized HTML widget** *(Blocker)*
Signature: one `html` widget containing most of the page; settings blob is enormous; almost no other widget types on the page.
Why: no editor control; every copy change is a code edit; global styling cannot reach it; responsive behaviour is whatever the CSS says; accessibility and SEO are unmanaged.
Native alternative: the §9 decision tree — containers + core widgets; loops for repeated content; scoped custom code only for isolated fragments.

**A2 — Fake nesting / wrapper-only containers** *(Major)*
Signature: chains of containers with a single child; the "structure" is decoration, not layout.
Why: DOM bloat, editor friction, harder to debug.
Fix: remove the wrapper; use container gap/padding for rhythm.

**A3 — Flattened layout** *(Major)*
Signature: what the design shows as a grid is built as one long column, or as absolutely positioned elements; two-column layouts that only line up by coincidence.
Why: breaks on real content, fights responsiveness.
Fix: flex row/column or grid, with explicit alignment.

**A4 — Sections/columns in a new build** *(Minor/Major)*
Signature: `elType: section` + `column` in a document created after containers were default (3.16+).
Why: deprecated path, more wrappers, no future.
Fix: containers (`container` on V3, atomic Flexbox/Div on V4).

**A5 — Absolute positioning and fixed heights for content** *(Major)*
Signature: `position: absolute`, negative margins, `height` in px on text-bearing blocks.
Why: content growth and viewport changes break the layout.
Fix: flex/grid alignment; `min-height` where a height is genuinely needed.

**A6 — Nesting archaeology** *(Minor/Major)*
Signature: 8+ container levels for a simple section.
Why: editing is slow; DOM cost; fragile.
Fix: flatten to the primitives actually needed.

## B. Content and editability

**B1 — Hardcoded content that should be dynamic** *(Blocker for client work)*
Signature: repeated literal text/prices/contact details inside settings; the same value typed on several pages.
Why: the client cannot change it; values drift out of sync.
Fix: ACF/post fields, theme options, dynamic tags, or a structured type + loop. Decide with `acf-dynamic-content-plan`.

**B2 — Design decisions stored as content** *(Major)*
Signature: ACF fields for "headline colour", "background style", "font size".
Why: lets non-designers break the design system; duplicates tokens.
Fix: tokens/classes for design; fields for content.

**B3 — Missing empty states** *(Major)*
Signature: dynamic blocks with no fallback; missing image renders a broken box; empty excerpt leaves a layout gap.
Why: real sites have missing data.
Fix: explicit fallback per field (hide / default / placeholder-in-preview-only).

**B4 — Repeated trees instead of reuse** *(Major)*
Signature: the same card markup duplicated 12 times; identical styling re-applied per instance.
Why: every change must be made N times.
Fix: V4 Component (with properties) / Loop / global widget / template part.

## C. Styling

**C1 — Duplicate styles / no design system** *(Major)*
Signature: the same hex/rgb or size repeated per element; no global colours/fonts, no Classes/Variables, or two competing token systems.
Why: visual drift; multi-hour edits.
Fix: tokens + classes; one source of truth.

**C2 — Custom CSS replacing controls** *(Major)*
Signature: large page-level Custom CSS doing what native controls do; `!important` chains; selectors targeting Elementor's internal classes.
Why: breaks on updates and with markup experiments; invisible to editors.
Fix: native controls + tokens; keep a scoped, named snippet only for genuinely visual exceptions.

**C3 — Excessive inline CSS/JS in widgets** *(Minor/Major)*
Signature: `<style>`/`<script>` inside text/HTML widgets or settings.
Why: unmanaged, unminified, duplicated, cache-hostile.
Fix: enqueue properly (small plugin/child theme) or use native controls.

## D. Interactions and behaviour

**D1 — JS for behaviour Elementor provides natively** *(Major)*
Signature: custom accordion/tabs/modal/carousel written in JS inside an HTML widget.
Why: duplicates a maintained implementation; keyboard/a11y usually broken; performance cost.
Fix: native Tabs/Accordion/Popup/Interactions.

**D2 — Iframe site reproduction / embed-as-layout** *(Blocker)*
Signature: an `<iframe>` rendering another page or the "approved design" as the page body.
Why: not editable, not indexable, not responsive, not accessible; it is a screenshot with extra steps.
Fix: build it natively; use an iframe only for genuinely third-party content, sandboxed and lazy-loaded.

**D3 — Image-only layouts** *(Blocker)*
Signature: a designed section delivered as one flattened image; text baked into a PNG.
Why: unreadable to assistive tech, unindexable, unlocalisable, uneditable, blurry at scale.
Fix: rebuild with native structure; images carry decorative roles only.

**D4 — Missing interactive states** *(Major)*
Signature: no hover/focus/active/disabled designs; hover-only affordances; invisible focus.
Why: accessibility failures and dead-feeling UI.
Fix: define states per interactive element; ensure focus visibility.

## E. Structure of the site (Theme Builder and content model)

**E1 — No Theme Builder architecture** *(Major)*
Signature: every page hand-built including header/footer; no single/archive templates; no display conditions.
Why: N× the work; inconsistency; rebuilds for every content change.
Fix: header/footer/single/archive templates + a conditions matrix (see `wordpress-site-architecture`).

**E2 — Conditions applied site-wide because specificity was hard** *(Major)*
Signature: one "single" template with no conditions or blanket `include/general`; exclusions absent.
Why: templates fight each other; unpredictable output.
Fix: explicit include + exclude + priority per template.

**E3 — Content model avoidance** *(Major)*
Signature: 200 pages instead of a CPT; everything a Page; no taxonomy.
Why: unmaintainable, no dynamic content, no archives.
Fix: content model decisions first (`wordpress-site-architecture`), then templates.

**E4 — Long-form content built as widgets** *(Major)*
Signature: article bodies as dozens of Heading/Text widgets.
Why: writers cannot work; search/pagination break; structure is rigid.
Fix: template frames the page; dynamic post content owns the body.

**E5 — Undocumented dependencies** *(Major)*
Signature: third-party widgetTypes/add-ons required with no note; a plugin the client will not maintain.
Why: silent breakage later.
Fix: dependency register with purpose + exit condition + fallback.

## F. Responsive and quality

**F1 — Responsive by accident** *(Major)*
Signature: no `_tablet`/`_mobile` overrides; layout works at one width; fixed desktop widths; horizontal scroll at ~1025px.
Why: most traffic is not desktop.
Fix: responsive intent per breakpoint; container stacking, token steps, image ratios.

**F2 — Blanket stacking** *(Minor)*
Signature: everything stacks on mobile with no typographic or spacial adjustment; tap targets < 44px.
Why: usable but poor; low conversion.
Fix: step the type scale, adjust spacing and order deliberately.

**F3 — Oversized/unoptimised media** *(Minor/Major)*
Signature: multi-MB hero images; no dimensions (CLS); wrong formats; missing responsive sizes.
Why: LCP and CLS failures.
Fix: dimensions, formats, sizes, and an explicit LCP policy.

## G. Verification and process

**G1 — Never verified on real content** *(Major)*
Signature: built with placeholder-length copy; no empty-state testing; no long-title testing.
Why: breaks on launch day.
Fix: content-stress tests (`elementor-qa-gate`).

**G2 — Never verified at other breakpoints** *(Major)*
Signature: only desktop was checked.
Fix: breakpoint matrix with explicit "not observed" rows.

**G3 — Unverifiable claims** *(Note→Blocker if it reaches a client)*
Signature: "this passes WCAG", "Lighthouse is 100", "this JSON will import cleanly".
Fix: verification taxonomy; state what was tested and how.

---

## How to use this catalogue

1. Inventory the artifact, then scan categories A–G in order; record hits with evidence (element path/ID) and severity.
2. Rank by severity × impact × effort.
3. For each hit, give the native alternative — never just "this is wrong".
4. Distinguish **defect** from **preference** explicitly.
5. Close with what could not be determined from the artifact and the cheapest test for each.
