# Verification Taxonomy

**verified against:** Elementor 4.3.x / WordPress 7.x / OpenAI plugin docs, 2026-10-06.

Every technical claim this plugin makes about Elementor, Elementor Pro, WordPress, ACF or any plugin must carry one of the five labels below. This is not decoration: the labels are what stop the plugin from inventing control IDs, element types and version behaviours that do not exist.

## The five labels

| Label | Meaning | May be stated as fact? | Allowed in a build plan? | Allowed in generated JSON? |
|---|---|---|---|---|
| **CONFIRMED** | Verified against first-party documentation, or against a real artifact the user supplied for *this* target and version. | Yes | Yes | Yes (T2 scaffold) |
| **LIKELY** | Consistent across multiple credible sources or widely observed behaviour, but not explicitly documented. | Only with the qualifier and the basis stated. | Yes, with a "verify" note | Only structural keys; never for settings values |
| **ASSUMED** | Needed for the answer to exist, but unverified. | No — must be listed in an Assumptions block the user can correct. | Yes, flagged | No |
| **UNVERIFIED** | Sources conflict, or nothing reliable was found. | No | **No** — convert into a question plus the cheapest test that resolves it. | No |
| **VERSION-DEPENDENT** | True only for a specific version band. | Only when paired with the version and a re-check instruction. | Yes, with version stated | Only when the version is confirmed |

## Emission rules

1. **Structural requirement:** any substantial answer that touches Elementor internals ends with a **Confidence Ledger** — a table of the claims made and their labels. This makes uncertainty impossible to omit.
2. **UNVERIFIED is not advice.** Rephrase every UNVERIFIED item as: *the question to ask* + *the cheapest test*. Example: instead of "`__dynamic__` uses this format", write "I believe dynamic bindings live in a `__dynamic__` map — confirmed in real exports but not in the official data-structure docs. Cheapest test: export a page from your site that uses one dynamic tag and paste the element."
3. **VERSION-DEPENDENT always travels with the version and the re-check.** "Atomic Accordion exists in 4.3 (CONFIRMED for 4.3; re-check on 4.4+)."
4. **Never launder a LIKELY into a CONFIRMED** by repetition across a long answer. Labels are per-claim, not per-document.
5. **Reference-export diffing upgrades labels.** A setting key seen in an export from the user's own site and version is CONFIRMED *for that site*. Anything not seen in that export stays UNVERIFIED at best.
6. **User-supplied facts are strong but scoped.** "My Elementor is 4.3.4" makes version claims CONFIRMED for that site only.

## Standing labels for known-risky claims (v1)

These are pre-labelled so the model does not have to rediscover them. Update the list when you learn better.

| Claim | Label | Note |
|---|---|---|
| Element structure (`id`, `elType`, `isInner`, `settings`, `elements`; `widgetType` on widgets) | CONFIRMED | Official data-structure docs |
| Responsive values are `_tablet` / `_mobile` key suffixes | CONFIRMED | Official responsive-data docs |
| Repeaters are arrays of objects each with `_id` | CONFIRMED | Official repeaters docs |
| Container element and its nesting | CONFIRMED | Official container docs |
| Atomic elements carry `version`, `editor_settings`, `interactions`, `styles` | CONFIRMED | Official atomic-elements docs |
| Atomic widget-shaped elements (`widgetType: "e-heading"` etc.) and typed `{"$$type": …}` settings wrappers | LIKELY | Observed in real 4.x exports; not documented as a public contract |
| `__dynamic__` map holding `[elementor-tag …]` strings | LIKELY | Widely observed; not in the retrieved data-structure docs |
| Element IDs are 7-character hex | LIKELY | Observed convention; docs say only "unique string" |
| Specific control IDs (e.g. a widget's setting keys) | VERSION-DEPENDENT | Must come from the installed version or a real export |
| Availability of a given atomic element (gallery, carousel, list…) | VERSION-DEPENDENT | Changed repeatedly across 4.0–4.4 |
| Elementor MCP tool names and exact capability list | UNVERIFIED | Detect at runtime from the live tool listing; never hard-code |
| ACF field types renderable by native dynamic tags | LIKELY | Repeater/Flexible Content/Gallery/Clone are reported as not natively supported; confirm per site |

## Wording patterns to use

- Confirmed: "Confirmed for Elementor 4.3: containers nest unlimited."
- Likely: "Likely, based on multiple real exports (not in the official docs): dynamic bindings are stored in `__dynamic__`."
- Assumed: "Assuming Atomic Editor is enabled because this is a new 4.x site — correct me if not."
- Unverified: "I can't verify the exact tool names Elementor's MCP exposes. Check `elementor/get-globals`-style ability names on your site, or list the tools after connecting."
- Version-dependent: "Loop taxonomy filtering exists from 4.3 Pro — confirm your Pro version before planning around it."
