# Widget Map — V3 (classic widgets + containers)

**verified against:** Elementor 4.3.x docs and release notes, 2026-10-06. All control IDs are **VERSION-DEPENDENT**: confirm against the installed version or a real export before emitting them.

## Layout

| Element | Use for | Avoid when | Notes |
|---|---|---|---|
| `container` | Everything structural: rows, columns, stacks, cards, wrappers with layout | Never nest a container that only wraps one child with no layout/behaviour | `flex_direction`, `content_position`, `align_items`, `gap`, `padding`, `html_tag`, `min_height`/`custom_height` |
| `section` + `column` | Legacy documents only | Any new build | Deprecated-but-working. Do not introduce new sections; do not "fix" legacy ones unprompted |
| Nested containers | Rows inside sections, cards inside rows | Depth > ~4–5 for a simple block | Depth is a maintenance and DOM cost, not a feature |

Layout decisions: **flex** for rows/columns/stacks; **grid** only if the target version supports it (V3 has no grid layout element — approximate with nested containers, or switch to atomic Grid on V4).

## Content widgets

| Widget | `widgetType` | Use for | Watch out for |
|---|---|---|---|
| Heading | `heading` | Titles, section headers | Set `header_size` (`h1`–`h6`, `div`, `span`) — never leave a page with two `h1`s |
| Text Editor | `text-editor` | Body copy, captions, inline lists/links | Best inline-formatting support in V3; long-form article bodies should still live in dynamic post content |
| Image | `image` | Content imagery | Set `image_size`, `width`, alt text; use dimensions to protect CLS |
| Button | `button` | CTAs | `text`, `link`, size, alignment; style via global button style where possible |
| Icon / Icon Box / Image Box | `icon`, `icon-box`, `image-box` | Feature cards, value props | Classic V3 patterns; classic Icon Box is a good "composed" target |
| Icon List | `icon-list` | Feature lists, checklists | Repeater — needs `_id` per item |
| Divider / Spacer | `divider`, `spacer` | Visual separation, rhythm | Prefer container gap/padding over Spacer widgets |
| Counter / Progress / Star Rating | `counter`, `progress`, `star-rating` | Stats, ratings | Static values unless wired to dynamic tags |
| Testimonial | `testimonial` | Quotes | Single-item; loops need Pro |
| Tabs / Accordion / Toggle | `tabs`, `accordion`, `toggle` | FAQ, feature groups | Repeaters; FAQ schema support varies by version — check before promising it |
| Alert / Text Path / Countdown | `alert`, `text-path`, `countdown` | Callouts, decorative type, timers | Countdown is often a conversion gimmick — question the purpose |
| Social Icons | `social-icons` | Social links | Repeater; check link targets and `rel` |
| Video / Google Maps / Basic Gallery / Image Carousel | `video`, `google_maps`, `gallery`, `image-carousel` | Media | Carousels load Swiper assets; the count matters for performance |
| HTML | `html` | Genuinely isolated embeds only | See the anti-pattern catalogue: a large `html` widget is the single most common failure |
| Shortcode | `shortcode` | Plugin output you cannot express natively | Red flag when used to wrap content that should be a template or a widget |
| Menu Anchor | `menu-anchor` | On-page navigation targets | Pairs with anchor links |
| Search Form | `search-form` | Site search | Style via theme style |
| Sidebar/WordPress widgets (removed 4.3 from the panel) | — | — | Legacy only |

## Pro widgets (require Elementor Pro — the biggest capability cliff)

| Widget | `widgetType` | Use for |
|---|---|---|
| Form | `form` | Lead/contact forms; `form_fields` is a repeater |
| Posts / Loop Grid / Loop Carousel | `posts`, `loop-grid`, `loop-carousel` | Dynamic listings, CPT archives, related content |
| Nav Menu | `nav-menu` | Theme Builder header navigation (see also Mega Menu) |
| Slides | `slides` | Hero sliders (weigh the cost) |
| Price List / Price Table | `price-list`, `price-table` | Services and pricing |
| Call to Action / Flip Box / Animated Headline | `call-to-action`, `flip-box`, `animated-headline` | Marketing sections |
| Table of Contents / Share Buttons / Reviews | `table-of-contents`, `share-buttons`, `reviews` | Content tooling and social proof |
| Gallery / Portfolio | `gallery`, `portfolio` | Media grids |
| Popup (template type) | — | Overlays, exit intent |
| WooCommerce widgets | `woocommerce-*` | Product surfaces |
| Theme Builder templates | `header`, `footer`, `single`, `archive`, `search-results`, `error-404` | Site-level surfaces |

## Selection order (V3)

1. `container` + core content widget (+ global colour/font and Theme Style tokens).
2. Compose from core widgets when no single widget fits (this is the tier AI tools skip).
3. Pro widget when it is genuinely the right tool and Pro is installed.
4. Loop/Posts when the content is repeatable and lives in WordPress.
5. Scoped `html`/custom code only for isolated embeds or genuinely bespoke interaction — with a written justification and exit condition.

## Verification reminders

- Every `widgetType` used must exist on the target site (Free vs Pro vs add-on). List the requirement in the plan.
- Every setting key emitted must be real for that widget and version. Prefer structural keys (`title`, `text`, `editor`, `link`, `header_size`) and let the human set the rest in the editor.
- Dynamic tags (`__dynamic__`) are **Pro-only** in practice for most tags.
