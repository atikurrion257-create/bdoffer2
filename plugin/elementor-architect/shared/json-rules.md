# JSON Rules (structure, typing, tiers, validation)

**verified against:** Elementor developer data-structure docs + observed 4.x exports, 2026-10-06. Control IDs are **VERSION-DEPENDENT**.

## 1. Structure

**Document (template export, kit template, page content file):**
```json
{ "title": "…", "type": "page", "version": "0.4", "page_settings": {}, "content": [] }
```
**Element (inside `content` or inside a stored `_elementor_data`):**
```json
{ "id": "6af611eb", "elType": "container", "isInner": false, "settings": {}, "elements": [] }
```
**Widget element:** same, plus `"widgetType": "heading"`.
**Atomic element:** same as element, plus `"version"`, `"editor_settings"`, `"interactions"`, `"styles"`; content elements appear widget-shaped (`widgetType: "e-heading"`) with typed settings wrappers (`{"$$type": …, "value": …}`) — LIKELY, not a documented contract.

Rules: `id` unique per document (7-char hex is the convention, LIKELY); `isInner` true for nested layout elements; `settings` is `{}` (or `[]`) when empty; `elements` is always an array; widgets are leaves.

## 2. Typing conventions

| Value kind | Shape | Example |
|---|---|---|
| Dimension (single) | `{unit, size, sizes}` | `{"unit":"px","size":20,"sizes":[]}` |
| Dimensions (per-side) | `{unit, top, right, bottom, left, isLinked}` | padding, margin, border-radius |
| Responsive value | base key + `_tablet` / `_mobile` suffixes | `align`, `align_tablet`, `align_mobile` |
| Link | `{url, is_external, nofollow}` | `{"url":"/contact","is_external":"","nofollow":""}` |
| Repeater | array of objects, each with `_id` | tabs, accordion items, icon lists, form fields |
| Dynamic binding | `__dynamic__` map of `[elementor-tag …]` strings | LIKELY — confirm from a real export |
| Switcher/boolean | often `"yes"` / `""` | verify per control |

Never invent nested responsive objects (`{"desktop": …, "tablet": …}`) — that is invalid.

## 3. The three output tiers

| Tier | Name | What may be emitted | Mandatory warnings |
|---|---|---|---|
| **T1** | Analysis artifact | Observations about existing JSON (findings, metrics, trees) | Confidence labels per finding |
| **T2** | Classic scaffold (V3) | Containers + core widgets + **whitelisted** structural settings only | "Validate on a staging site first"; "control IDs must match your Elementor/Pro version"; per-claim confidence |
| **T3** | Atomic fragment (V4) | Illustrative atomic structures for documentation/spec **only** | "REFERENCE ONLY — not import-ready. Use Elementor MCP to create atomic structures on the site." |

**Hard rules:** never present T3 as importable; never emit T2 without the whitelist + warning; never emit settings keys that were not seen in a real export or official docs.

## 4. The whitelist principle (T2)

Allowed without asking (structural, stable, documented):
`flex_direction`, `flex_wrap`, `justify_content`, `align_items`, `gap`, `padding`, `margin`, `min_height`, `custom_height`, `height`, `content_position`, `html_tag`, `width`, `background_color`, `border_radius`, `title`, `header_size`, `text`, `editor`, `link`, `align`, `align_tablet`, `align_mobile`, `image` (`{url,id}`), `image_size`, `text_color`, `typography_*` (only if confirmed).

Everything else: ask for a reference export, or leave it to the human in the editor. A scaffold that omits a styling key is useful; a scaffold that invents one is a trap.

## 5. Things that cannot be generated site-independently

- Media attachment IDs (images must resolve in the target library).
- Global class / variable IDs and names (site-local; classes are referenced by ID).
- Dynamic-tag IDs and their settings.
- Template, loop, popup and form IDs.
- Any setting whose key or enum changed between versions.

Say so, rather than producing something that half-works.

## 6. Import surfaces (there is no public import REST endpoint)

| Artifact | Surface | Post-import step |
|---|---|---|
| Template JSON/ZIP | Templates → Saved Templates → Import Templates, or the editor library | Regenerate CSS |
| Kit ZIP | Elementor → Tools → Import/Export Kit, or `wp elementor kit import` | Regenerate CSS; reconcile globals |
| Library file/dir | `wp elementor library import` / `import-dir` | Regenerate CSS |
| Design system ZIP | Design System panel → Import | Regenerate; resolve conflicts (override vs keep) |
| Page structure | Elementor editor (paste scaffold), or Elementor MCP (V4, drafts) | Verify in editor |

Always include the "regenerate CSS / flush cache" step in any import instruction.

## 7. Validation checklist (manual, and the spec for the v1.1 script)

**Structural:** dialect detected; correct wrapper vs bare array; `id` present/unique/format; `elType` legal; `widgetType` present iff widget; `elements` arrays present; `isInner` sane; no sections inside containers in an atomic target.
**Typing:** dimensions in the right shape; links well-formed; repeaters arrays with `_id`; responsive values as suffixes; no invented nesting.
**References:** `__dynamic__` format; class/variable IDs exist in the target kit; media resolves; loop/template references valid.
**Hygiene:** nesting depth; wrapper-only containers; absolute positioning/fixed heights; HTML widget size; custom CSS footprint; missing responsive overrides; duplicate styling; unused anchors.
**Grounding:** diff against a real export from the same site and version; anything absent from the reference is reported as **not seen in reference export**, never as "wrong".

## 8. Reporting format for JSON work

Structural map (tree + counts) → widget histogram → findings (severity, evidence path, why, fix, confidence) → tier declaration → validation notes → what could not be determined + cheapest test.
