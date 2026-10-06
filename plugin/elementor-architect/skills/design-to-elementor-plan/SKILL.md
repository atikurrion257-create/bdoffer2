---
name: design-to-elementor-plan
description: >
  Convert a screenshot, Figma design or export, live URL, or HTML/CSS implementation into
  a decision-complete Elementor implementation blueprint: section segmentation, component
  reuse, design-token mapping, per-node widget/element selection, content and dynamic-data
  classification, responsive intent per breakpoint, an unknowns register, and verification
  steps. Use when the user says rebuild this screenshot, convert this design or HTML to
  Elementor, map this Figma to WordPress, or asks for a build/implementation plan from a
  visual or markup source. Do NOT use to audit existing Elementor JSON, templates or
  exports (use elementor-structure-audit), to plan a whole site's content model and
  templates (use wordpress-site-architecture), or to verify a finished build
  (use elementor-qa-gate).
---

# Design → Elementor Plan

Turn a visual or markup source into something a competent developer can execute without asking you design questions.

## When to use

- Screenshot(s) / Figma frames / Figma export → Elementor plan.
- Live URL → plan to reproduce or rebuild its structure.
- HTML/CSS → native Elementor architecture (with a node-by-node mapping table).
- "Blueprint", "build spec", "mapping", "implementation plan" requests from a visual.

## When NOT to use

Auditing Elementor artifacts; site-level content modelling and Theme Builder planning; final QA.

## Inputs

Required: the artifact (image(s), HTML/CSS, URL, Figma export/description).
Helpful: fidelity intent (pixel-reference vs **system-first** — default system-first); brand tokens; content source (CMS-driven or static); device priority; support matrix.
Probe if unknown (one question): dialect/version context. Default to V3-safe with ASSUMED labels.

## Workflow

1. **Classify the artifact and intent.** Screenshot / Figma / URL / HTML. Pixel-reference vs system-first vs refresh. Say which you assumed.
2. **Segment into named sections** with a stable convention (`hero`, `value-props`, `social-proof`, `pricing`, `cta`, `footer`). List assumptions about anything ambiguous.
3. **Component identification and reuse plan.** Find repeats (cards, list rows, logos, testimonials, CTAs, buttons) and choose the reuse mechanism per repeat: Component / Loop / template part / copy (last resort).
4. **Design-system pass.** Derive tokens (colour roles, type scale, spacing scale, radii, shadows, button styles, interactive states) or ingest the client's system. Map to the site's system — global colours/fonts + Theme Style on V3, Classes/Variables on V4. Say explicitly that measurements read from a picture are proposals, not facts.
5. **Structure mapping.** Per node: primitive (container/flex/grid), element/widget, semantic tag, and only the settings that matter. Apply the escalation order from `elementor-native-architecture`.
6. **Content classification.** Per node: static-by-exception / post field / ACF field / option / menu / media. Propose field names for anything dynamic. Anything a client will change weekly must not be static.
7. **Responsive intent.** Per breakpoint: *what changes and why* — column counts, stacking order, type steps, spacing rhythm, nav collapse, image ratios, tap targets, hover-vs-touch. Never "make it stack".
8. **Dependency check.** Widgets/plugins/add-ons required (Pro? third-party?), with a fallback for each.
9. **Risks and unknowns.** Measurements not observable in the artifact; illegible copy; missing states; asset ambiguity; fidelity risk; accessibility risk; LCP/CLS risk.
10. **Verification plan.** What to check after build (single H1, contrast, dimensions, tap targets, empty states, LCP image, responsive breakpoints).
11. **Output** using `assets/blueprint-template.md`.

## Output contract

Per-section blueprint (tree + per-node mapping + token plan + content sources + responsive intent), plus: assumptions/unknowns register, dependency list, risk list, verification plan, confidence ledger. Mark every measurement that matters as **Observed**, **Inferred** or **Unknown**.

## Hard rules

- Never present a hex value, font size, spacing value or breakpoint read from an image as fact. Propose from a scale and label it.
- Never invent measurements the artifact cannot contain (states, breakpoints, hidden elements, hover behaviour).
- Preserve semantics: one `h1`, logical heading order, real landmark tags, meaningful link text.
- Prefer content in fields over hardcoded text; say so whenever a text block is likely to change.
- State fidelity honestly: native + responsive + token-based builds are fluid, not pixel-locked. Negotiate the requirement rather than fighting the builder.
- If a required widget is not installed/available, say so and give the fallback (composition, alternative widget, or documented exception).
- Long-form article or documentation bodies do **not** get converted into dozens of widgets — recommend a template frame plus dynamic post content.

## References

- `references/playbook.md` — intake checklist, tokenisation rules, responsive intent patterns, HTML→native translation rules, failure modes.
- `references/blueprint-template.md` (in `assets/`) — the output format.
- Shared: `dialect-policy.md`, `widget-map-v3.md`, `widget-map-v4.md`, `verification-taxonomy.md`, `house-standard.md`.

## Hand-offs

Say the hand-off out loud.
- Anything dynamic or editable → `acf-dynamic-content-plan`.
- Site-level templates, conditions, content model → `wordpress-site-architecture`.
- Pre-delivery verification → `elementor-qa-gate`.
- Native-ness disputes or exceptions → `elementor-native-architecture`.

## Failure handling

- **Low-resolution or single-breakpoint input** → ask for more evidence, or deliver with an explicit fidelity-risk section.
- **Illegible copy** → labelled placeholder, and ask for the text.
- **No design at all, only a goal** → do not invent a layout; ask for a reference or produce a standard/structure proposal clearly marked as a proposal.
- **Too many screens at once** → ask for one page or flow at a time.
- **HTML with no CSS** → ask for the CSS or infer structure only, and label all styling as unknown.
