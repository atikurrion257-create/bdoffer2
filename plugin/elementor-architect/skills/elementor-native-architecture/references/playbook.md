# Playbook — Native Architecture

## 1. The definition of "native Elementor" (normative)

> **Elementor-native architecture** is a document whose layout, content and styling are expressed exclusively through Elementor's own element types for the target dialect (`container`, legacy `section`/`column`, atomic `e-*` elements, and `widget` nodes), whose every element carries the required structural keys, whose settings keys are real control IDs of the **installed** Elementor (+Pro/add-on) version, whose responsive differences are expressed as Elementor responsive keys rather than as custom CSS, whose content that a non-developer must change is bound to Elementor/WordPress/ACF data sources rather than hardcoded, whose styling reuses the site's design system rather than duplicating values per element, and whose page-level behaviour is expressed through Theme Builder templates with explicit display conditions.

Four meanings people conflate, and which one we use:

| Meaning | Test | Our position |
|---|---|---|
| Rendered by Elementor at all | Does the page open in the editor? | Necessary, not sufficient |
| Built from Elementor primitives | Is any `html` widget carrying layout? | **Required** |
| Editable through controls | Can a non-dev change content without code? | **Required** for real client work |
| Wired into Elementor systems | Tokens, classes, dynamic tags, conditions, responsive keys? | **Required** |

## 2. The five architecture classes (use these words in reviews)

| Class | Definition | Verdict |
|---|---|---|
| **A. Looks like Elementor** | Rendered by Elementor but essentially an HTML widget page with custom CSS/JS | Not native — treated as "a screenshot you can edit" |
| **B. Native + a scoped HTML widget** | Native structure; the HTML widget owns an isolated fragment with a documented reason | Acceptable if scoped and recorded |
| **C. Built with native widgets (V3)** | Containers + widgets, controls for styling, responsive keys present | Native for V3-era sites |
| **D. Custom Elementor widget** | PHP widget via the Widgets API with its own controls | Native in form; justified only under §5 |
| **E. Hybrid** | Native + atomic + scoped exceptions, with a recorded boundary | The realistic answer for complex sites |

## 3. Escalation order (apply in this exact sequence)

1. **Atomic element** — target is V4 **and** the element exists in the target version.
2. **Core V3 widget** — a semantically correct widget exists (Heading, Image, Button, Icon Box, Tabs, Accordion, Form, …).
3. **Pro widget** — Pro is installed and the widget is genuinely right (Loop Grid, Nav Menu, Forms).
4. **Composed native** — build it from primitives + class/token. *This is the tier AI tools skip and where good architecture lives.*
5. **Loop / Component** — the pattern repeats: atomic Loop (4.2+) or Pro Loop for content; Component (V4) for layout reuse; global widget only for a single shared element on V3.
6. **Scoped custom CSS** — purely visual, consistent, named, documented.
7. **Custom widget** — only if §5 passes.
8. **Third-party widget** — only with a documented dependency and exit condition.
9. **Reject:** page-sized HTML widgets, iframe reproduction, image-based layouts, shortcode hacks wrapping content that should be a template.

## 4. Component boundaries

- A component is the smallest unit that should change as a whole (card, CTA block, header, list item).
- One component = one dialect. Never mix atomic and classic primitives inside a component.
- One component = one style source (classes/tokens), never per-instance overrides except documented one-offs.
- Repeated ≥2 places → reuse mechanism; repeated across pages → Component; repeated from content → Loop.
- Name components in the plan so they can become Components/Classes with the same names.

## 5. Custom-code justification rubric (score before approving)

| Test | Pass condition |
|---|---|
| Necessity | Cannot be done natively or by composition at reasonable cost |
| Reuse | Used in ≥2 places, or will be (else scoped one-off CSS at most) |
| Editability | Content stays in fields/controls after implementation |
| Scope | Isolated to a named class/component/template |
| Portability | Survives theme/plugin updates and a site migration |
| Performance | Within the house budgets (JS/CSS/image) |
| Accessibility | Keyboard, focus, contrast, reduced motion handled |
| Documentation | Recorded with an exit condition |

Any "no" → do not recommend it; return to step 4 of §3.

## 6. Layout discipline thresholds

| Rule | Threshold |
|---|---|
| Nesting depth | Flag > 4 for a simple section; require a reason beyond that |
| Wrapper-only containers | Never; remove or justify |
| Flex vs grid | Flex for 1-D rows/columns/stacks; grid for true 2-D (V4 atomic Grid, 4.2+) |
| Absolute positioning / fixed heights | Suspect by default; require justification and a responsive plan |
| Spacing | Container gap/padding + tokens; avoid per-widget margins for rhythm |
| Semantic tags | Correct heading order; `nav`/`main` where supported; sections for page bands |
| Repeats | Component/Loop, never copied trees |

## 7. Where native-first becomes counterproductive (say these out loud when relevant)

1. The atomic element does not exist yet (gallery, carousel, list in some versions).
2. The data shape does not fit (ACF Repeater/Flexible/Gallery/Clone have no native tag).
3. Fidelity requirements are contractual and absolute — negotiate, don't fight the builder.
4. The "fully native" version is dramatically heavier or harder to edit than a composed alternative.
5. The behaviour is genuinely bespoke (calculators, configurators, data visualisation).
6. A tiny scoped snippet is genuinely cheaper to maintain than 40 per-element overrides.

Every such case becomes an **exception record**: what / why / scope / exit condition.
