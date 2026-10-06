# Playbook — ACF + Dynamic Content

## 1. Supported dynamic field types (LIKELY — verify per site/version)

| ACF type | Native Elementor dynamic tag | Strategy | Fallback |
|---|---|---|---|
| Text, Textarea, Number, Email, URL | Yes | ACF Field tag on the matching control | Define a default or hide the element |
| WYSIWYG | Yes (text/HTML) | Text Editor + tag; sanitisation policy applies | Hide if empty |
| Image | Yes | Image element + tag; **return format = ID** (better responsive sizes) | Placeholder image |
| Date / DateTime | Yes | Heading/Text with a format; watch timezone | Hide |
| Select / Radio / Checkbox / True-False | Yes | Conditional display / flags | Default state |
| Link | Yes | Button link tag | Fallback URL or hide |
| Taxonomy field | Partial | Render terms as text; for links use the term archive or a custom tag | Hide |
| Options page values | Yes (options variants) | Global content (contact, social, footer) | Static default |
| Post Object / Relationship | Partial | Loop/query with a filter, or a custom tag | Manual link |
| **Repeater** | **No** | CPT + loop (preferred) / third-party repeater widget / custom dynamic tag | Restructure the model |
| **Flexible Content** | **No** | Component-per-layout + CPT/loop, or custom tag | Restructure |
| **Gallery** | **No** (picker) | Third-party widget, Pro Gallery + custom tag, or child posts + loop | Documented exception |
| **Clone** | **No** (renders sub-fields) | Use the cloned sub-fields directly | — |

Hard cap reality: **there is no native path for the four bolded types.** Saying so early is the difference between a plan that works and a rebuild.

## 2. Field-group design rules

1. **Prefix and namespace** field groups and field names (`site_hero_title`, `prop_price`).
2. **Names for code, labels for humans**, with instructions written in the client's language.
3. **Location rules match the editing context.** A field group located on a single page will not appear for the post type; a group located on the wrong post type will not appear in a template.
4. **Return formats fixed and recorded** — image → ID, date → the format the design expects, link → array/URL as needed.
5. **Required vs optional decided deliberately**; empty is a design state, not an error.
6. **Field groups stay small.** Ten fiddly fields beat forty.
7. **Group related fields** (a "Hero" group, a "Contact" group) so the editing screen reads like the page.
8. **Reuse groups across post types** where the content is genuinely identical.

## 3. Dynamic-tag mapping method

For each element in the blueprint: *control* (content field) → *source* (post/ACF/option/site) → *tag* → *settings* (key, format) → *fallback* → *who edits*.

Prefer post-native fields (title, featured image, excerpt, permalink) over ACF duplicates. Use ACF for what WordPress does not model.

## 4. Empty-state policy

| Situation | Behaviour |
|---|---|
| Optional text empty | Hide the element (not the whole section) |
| Optional image empty | Placeholder in preview only; hide on front end |
| Required-but-missing | Show nothing and surface an editor warning, or fall back to a sensible default |
| Whole collection empty | Explicit empty state with a message and a CTA |
| Template preview with no post | Expected `--`; document the preview post as part of the workflow |

## 5. Diagnosing "ACF shows --" and empty values (in order)

1. The field has no saved value for **that** post.
2. Location rules do not match the post type being edited.
3. Editing a global template without a preview post with data.
4. Field **name** vs **key** mismatch in a custom tag.
5. Return format mismatch (expecting a URL, getting an ID).
6. Cache/CSS not regenerated after structural changes.
7. ACF or Elementor version mismatch (rare, but real after partial updates).

## 6. Anti-patterns

| Anti-pattern | Why it hurts | Fix |
|---|---|---|
| Design decisions as fields | Editors break the design system | Tokens/classes |
| Repeater as a content model | No URL, no querying, no reuse, no native rendering | CPT + loop |
| Fields keyed by label | Renaming breaks everything | Stable names |
| Duplicated global content per page | Values drift | Options page |
| No fallbacks | Broken-looking content | Empty-state policy |
| Exposing raw HTML fields to non-technical roles | Security and layout risk | Limited formats or controlled fields |
| "Just add a field" without a rendering plan | Field exists, nothing shows it | Map the element first, then the field |
