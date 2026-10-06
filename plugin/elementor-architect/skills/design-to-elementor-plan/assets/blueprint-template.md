# Blueprint Template

> Copy into the deliverable. Delete guidance lines. Keep the Observed/Inferred/Unknown markers.

## 0. Summary

- **Source artifact:** (screenshot / Figma / URL / HTML)
- **Fidelity intent:** system-first *(default)* / pixel-reference / refresh
- **Dialect:** V3 / V4 atomic / hybrid *(boundary rule if hybrid)*
- **Site facts:** Elementor ___ · Pro ___ · Atomic ___ · Add-ons ___
- **Assumptions:** *(list every ASSUMED item)*
- **Unknowns requiring input:** *(list, numbered)*

## 1. Section list

| # | Section | Purpose | Reuse? | Dialect |
|---|---|---|---|---|
| 1 | hero | … | no | V4 |
| 2 | value-props | … | card ×3 | V4 |

## 2. Per-section blueprint

```
SECTION: hero
Dialect: V4 atomic | Semantic: section > h1, no nav
Structure:
  container(hero, flex column, min-height 70vh, content_position middle)
    ├─ heading(h1, class:hero__title)          content: static (client will not change) [Observed]
    ├─ paragraph(lead, class:text--lead)        content: static  [Observed]
    ├─ flexbox(row, gap: space/md)
    │    ├─ button(primary, class:btn--primary, link:/contact)
    │    └─ button(ghost,   class:btn--ghost,   link:/work)
    └─ image(hero-visual, ratio 16/9)           source: media library  [Inferred: role]
Content sources: none dynamic
Responsive intent:
  tablet  → type step down via token; keep row
  mobile  → stack; visual last; CTAs full width; tap targets ≥44px
Tokens: color/primary · space/md · radius/md · type/display
Unknowns: exact display size ≥1920 [Unknown]; row→column breakpoint [Assumed 767]
Verify: single H1 · contrast · LCP image ≤200 KB with dimensions · CLS stable
```

## 3. Node mapping table

| Node | Semantic role | Elementor target | Dialect | Key settings | Content source | Notes / exception |
|---|---|---|---|---|---|---|
| `section.hero > .cta` | primary CTA | Button | V4 | class `btn--primary`, link | static | confirm link with client |

## 4. Token plan

| Role | Value (proposed unless Observed) | Destination (Variable / global) | Confidence |
|---|---|---|---|
| `color/primary` | #______ | Variable | Proposed |

## 5. Content and dynamic map

| Element | Source | Field / tag | Fallback | Who edits |
|---|---|---|---|---|
| Hero H1 | Post title | Post Title tag | — | editor |

## 6. Responsive matrix

| Dimension | Desktop | Tablet | Mobile | Notes |
|---|---|---|---|---|
| Layout | | | | |
| Type scale | | | | |
| Spacing | | | | |
| Nav | | | | |
| Media | | | | |

## 7. Dependencies

| Requirement | Why | Fallback if unavailable |
|---|---|---|
| Elementor Pro | Loop Grid | Compose with core widgets |

## 8. Exception register

| What | Why | Scope | Exit condition |
|---|---|---|---|

## 9. Verification plan

- [ ] Single `h1`; heading order valid
- [ ] Breakpoints checked at the site's actual values
- [ ] Tap targets ≥ 44 px
- [ ] Images have dimensions; LCP image optimised
- [ ] Empty states tested
- [ ] Focus visibility verified

## 10. Confidence ledger

| Claim | Label |
|---|---|
