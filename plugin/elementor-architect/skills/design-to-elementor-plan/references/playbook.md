# Playbook — Design → Elementor Plan

## 1. Intake checklist

| Item | Why | If missing |
|---|---|---|
| Artifact type (image / Figma / URL / HTML) | Determines what is knowable | Ask |
| Fidelity intent (pixel-reference / system-first / refresh) | Sets expectations and cost | Assume **system-first** and say so |
| Target dialect & versions | Determines primitives | Ask once; else V3-safe + ASSUMED |
| Breakpoints / device priority | Responsive plan | Ask; else standard mobile/tablet/desktop with ASSUMED |
| Brand tokens (colours, type, spacing) | Avoids inventing a system | Derive a proposed scale, labelled |
| Content source (CMS vs static) | Determines fields vs literals | Assume CMS for anything listed >1× or likely to change |
| Pro / add-ons available | Determines widget options | Ask; else core-only with fallbacks stated |

## 2. What is knowable from a design artifact

**Reliably recoverable:** section boundaries; approximate grid/columns; hierarchy and reading order; text content (usually); component repetition; visible states; approximate colour families; image roles.

**Not recoverable:** exact spacing scale; type metrics (family/weight/line-height/letter-spacing); breakpoints; interaction and state designs (hover/focus/disabled/loading/error); assets and resolutions; anything hidden, clipped or behind a hover.

**Rule:** anything in the second list is an **unknown** (or an explicitly labelled proposal). Never let a plausible number become a fact in the plan.

## 3. Tokenisation rules

1. Anything used **≥2 times** becomes a token or class (colour, type style, spacing value, radius, shadow, button).
2. Name per `house-standard.md`; if the house standard is unfilled, propose names and say they are proposals.
3. Roles over values: `color/text-muted`, not `#8A8A8A` scattered through the plan.
4. Spacing uses a scale (e.g. 4/8/12/16/24/32/48/64/96) — flag any value off-scale as a question, not a decision.
5. Type: define display/heading/body/small roles with responsive steps or a fluid approach; never per-element font sizes.
6. States are part of the system: default, hover, focus-visible, active, disabled, loading, error, empty, selected.
7. On V4 target sites, prefer Variables (values) + Classes (rules). On V3, global colours/fonts + Theme Style. Never both as competing sources of truth.

## 4. Responsive intent patterns (use these, not "make it stack")

| Pattern | Desktop | Tablet | Mobile |
|---|---|---|---|
| Hero | row: copy + visual | row or stacked with reduced type | stacked, visual last, CTAs full width |
| Card grid | 3–4 up | 2 up | 1 up (or 2 up for small cards — decide, don't default) |
| Feature list | 2 columns | 2 columns | 1 column, icon+text tightened |
| Nav | full nav | condensed/drawer | drawer, 44px+ targets, focus-trapped |
| Tables | full table | horizontal scroll container | card conversion (state the a11y consequence) |
| Section rhythm | full spacing tokens | ~75% | ~60% |
| Type scale | display sizes | step down | step down; check wrapping, not just size |
| Media | wide ratio | crop-safe focal point | crop-safe; art direction only if it earns the weight |

Every structural change gets a reason. "It stacks" is not a reason.

## 5. HTML → native Elementor translation rules

| DOM pattern | Elementor target | Notes |
|---|---|---|
| Landmarks (`header/nav/main/section/footer`) | Container with the matching `html_tag` where supported | Semantic tags preserved |
| `h1`–`h6` | Heading with matching `header_size` | One `h1`; no skipped levels |
| `p` | Text Editor (V3) / Paragraph (V4) | Long-form body → dynamic post content, not widgets |
| `ul`/`ol` | Icon List, or Text Editor with a real list | Long lists → loop/dynamic |
| `a.cta` / button-looking link | Button widget/element | Real link semantics, real hover/focus states |
| `img` | Image | Explicit dimensions; alt policy applied; LCP image eager |
| `form` | Elementor Form (Pro) or a form plugin | Never hand-built HTML forms unless justified |
| Tabs/accordion/modal/carousel markup | Native widgets / Interactions | Never port the JS |
| `table` | Decide: Text Editor table / widget / third-party | Choose by editability and a11y needs |
| Repeated card markup | Component / Loop | Never copy the tree |
| Inline styles | Tokens/classes | Flag every raw value for explanation |
| Absolute-positioned layout | Flex/grid rebuild | Transliterate = future breakage |
| Decorative SVG/animation | Scoped HTML/SVG asset | Record as an exception |

**Always:** preserve semantics; convert layout CSS to flex/grid; tokenise spacing/type; keep interaction native; keep images as media-library assets.
**Never:** one giant HTML widget; inline styles; absolute-position layouts; fixed heights on content; CSS as the primary responsive mechanism; JS for native behaviour.
**Sometimes (justified):** SVG animation, third-party embeds, complex tables, long-form content (template frame instead).

## 6. Output density rule

A blueprint should be *skimmable and buildable*: one block per section, a table per mapping pass, and no more than a handful of settings per node — the ones that matter. If a section needs 40 lines, it usually needs splitting into components.

## 7. Failure modes to avoid

| Failure | Avoidance |
|---|---|
| Invented hex/pt values presented as facts | Observed/Inferred/Unknown markers |
| Single-section monolith (one giant container) | Section segmentation before tree building |
| Every text static | Content classification is mandatory |
| Duplicated styling | Tokenisation rule ≥2 |
| Silent add-on dependency | Dependency list with fallbacks |
| "Responsive" with no reasoning | Responsive intent table per breakpoint |
| Copying HTML div-soup into containers | Wrapper-only flags + nesting budget |
| Designing for one breakpoint | Breakpoint matrix in the blueprint |
| Missing interactive states | State checklist per interactive element |
| Losing accessibility semantics in translation | Semantic tag + heading order columns in the mapping table |
