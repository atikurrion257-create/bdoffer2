# Widget Map — V4 (Atomic elements, Classes, Variables, Components)

**verified against:** Elementor 4.0–4.4 developer notes and release announcements, 2026-10-06. **Everything here is VERSION-DEPENDENT** — the atomic element set changed three times in six months. Verify against the target version before planning around any element.

## The model

| Concept | What it is | Why it matters |
|---|---|---|
| **Atomic elements** | The new building blocks (`e-div-block`, `e-flexbox`, `e-grid`, `e-heading`, `e-paragraph`, `e-button`, `e-image`, …) | Less markup than V3 widgets; styled through one unified Style tab |
| **Variables** | Design tokens: colours, spacing, font sizes, radii, shadows | Values redefined in one place |
| **Classes (global)** | Reusable style rules applied to elements; stored as `e_global_class` posts, ordered/labelled in the Kit; **hard cap 1000** | This is the V4 equivalent of "global styling" — the main anti-duplication mechanism |
| **Components** | Reusable **layout** structures with exposed properties | Reuse at layout level (not just widget level, like V3 global widgets) |
| **Interactions** | Trigger-based behaviour (scroll, hover, click) | Replaces many "add a custom JS library" cases |
| **Default Styles** | Per-HTML-tag baseline styling (h1–h6, p, div, button…) from the Design System panel | Site-wide typography/colour baseline; global classes sit above it |
| **Editor V4 / Atomic Editor** | The editing experience, enabled in Elementor → Editor → Settings | V3 and V4 coexist on the same page; existing sites are unaffected until enabled |

## Element availability matrix (VERIFY PER VERSION)

| Element | Introduced | Notes |
|---|---|---|
| Div Block, Flexbox, Heading, Paragraph, Button, Image | 4.0 (stable, March 2026) | The core set |
| Tabs, Form (Atomic Forms) | 4.0 | Forms are assembled from field elements inside a Form container, not one monolithic widget |
| Grid (`e-grid`) | 4.2 | True CSS Grid — use it for 2-D layouts instead of nested containers |
| Loop | 4.2 (Pro) | Query + layout + Loop Item template; dynamic fields inside |
| Accordion | 4.3 | Nested content per item, expansion modes, FAQ schema |
| Background Video | 4.3 | Container-level video background with play/pause |
| Default Styles | 4.3 | Per-tag styling baseline |
| Atomic List | 4.4 (ETA Oct 2026) | Verify before relying on it |
| Gallery / Carousel / Slider as atomic | **Not available as of 4.4** | Use the classic widget as a documented dialect exception |
| Custom CSS inside atomic | Limited | Prefer Classes/Variables; treat classic Custom CSS as an exception |
| Rich inline text formatting / lists in atomic text elements | Limited vs V3 | Long-form or list-heavy copy may need a V3 Text Editor inside a documented boundary |

## Choosing V4 vs the classic widget for one section

1. **Is the element available in this version?** If no → classic widget, recorded as an exception.
2. **Does the section need rich text structures** (nested lists, inline formatting, long copy)? If yes → consider a V3 Text Editor inside a documented boundary, or move the copy to dynamic post content.
3. **Is it a 2-D layout** (cards in rows *and* columns, dashboards)? → atomic Grid.
4. **Is the content repeatable?** → atomic Loop (Pro, 4.2+) with dynamic fields inside the Loop Item.
5. **Is it repeated across pages?** → Component with exposed properties (not a copied tree).
6. **Is styling shared?** → Global Class. Never re-style the same component per instance.
7. **Does it need motion?** → Interactions before custom JS.
8. **Anything else** → compose from atomic elements.

## Class and variable hygiene (the V4 equivalent of "no duplicate styles")

- **Naming:** one convention, applied consistently (`btn--primary`, `card`, `text--lead`, `space/md`, `color/primary`). Fill the specifics into `house-standard.md`.
- **Ownership:** Variables for values, Classes for rules. Do not hard-code a colour that a Variable already carries.
- **Cap awareness:** 1000 classes is a hard cap; class IDs are referenced by documents, so classes are **site-local** and do not travel cleanly between sites.
- **Hybrid caution:** if legacy Global Colours/Fonts are also in play, the two systems can be synced — decide which is the source of truth and say so in the plan.
- **Classes over local styles:** local styles on atomic elements have had template-rendering bugs; Classes are more predictable and reviewable.

## Data structure reminders (V4)

- Atomic elements add `version`, `editor_settings`, `interactions`, `styles` to the standard element object.
- In real exports, atomic content elements appear **widget-shaped** (`widgetType: "e-heading"`) with **typed settings wrappers** (`{"$$type": …, "value": …}`) — **LIKELY**, not a documented public contract.
- Global classes are stored as `e_global_class` posts (`_elementor_global_class_data`) with a REST surface at `/wp-json/elementor/v1/` (GET `frontend|preview`; PUT with `changes = {added, deleted, modified, order}`) — CONFIRMED for 4.x.

## Hard rule for this project

**No public API exists for creating atomic elements, and Elementor does not recommend outside integration.** Therefore: never present a hand-written atomic JSON as import-ready. Produce a blueprint, or route the work through Elementor's own MCP on a site (drafts only, human-approved).
