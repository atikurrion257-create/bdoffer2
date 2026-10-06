# bdoffer2

Private workspace for the **Elementor + WordPress Architect** ChatGPT plugin: research, the built plugin, and its acceptance suite.

## What's here

| Path | What it is |
|---|---|
| `ELEMENTOR-ARCHITECT-RESEARCH-AND-BLUEPRINT.md` | The research report: evidence matrix, challenged assumptions, architecture decisions, skill design, security/approval model, MVP→V3 roadmap, Plugin Creator brief, master + per-skill instruction drafts, acceptance suite. Start with the plain-English section at the top. |
| `plugin/elementor-architect/` | **The built plugin** (v1.0.0). Skills-only, 7 skills, shared reference library. |
| `shared-map.json` | Which shared reference files get copied into which skills at build time. |
| `tools/build.py` | Builds the installable ZIP (`dist/elementor-architect-1.0.0.zip`, `plugin.json` at the ZIP root). |
| `docs/acceptance-tests.md` | 12 activation + 12 behaviour + 6 honesty + 9 safety tests, plus scripted package checks. |

## The seven skills

1. `elementor-native-architecture` — dialect policy (V3/V4), native definition, widget decision framework, exception register
2. `design-to-elementor-plan` — screenshot / Figma / URL / HTML → decision-complete blueprint
3. `elementor-structure-audit` — hostile audit of JSON, templates, exports, builder output, rendered HTML
4. `elementor-qa-gate` — pre-delivery verdict: responsive matrix, content stress, editability, sign-off
5. `wordpress-site-architecture` — content model, Theme Builder conditions, template hierarchy, migrations
6. `acf-dynamic-content-plan` — field design, dynamic-tag mapping, unsupported-field strategies, fallbacks
7. `site-quality-review` — performance/CWV + SEO + accessibility with flag/recommend/defer decisions

## Build

```bash
python3 tools/build.py            # full build → dist/elementor-architect-1.0.0.zip
python3 tools/build.py --no-zip   # stage + inject shared references only
```

Generated artifacts in `dist/` are gitignored. Edit shared references in `plugin/elementor-architect/shared/` only — never inside a skill folder.

## Install (ChatGPT)

1. Verify Skills are available (sidebar → **Plugins** → **Skills**).
2. Install **Plugin Creator** from the plugin directory.
3. Start a chat with `@plugin-creator`, attach `dist/elementor-architect-1.0.0.zip`, and use the install prompt in `plugin/elementor-architect/README.md`.

Then run `docs/acceptance-tests.md`.

## Ground rules the plugin enforces

- Every technical claim about Elementor internals carries a confidence label (CONFIRMED / LIKELY / ASSUMED / UNVERIFIED / VERSION-DEPENDENT).
- Every Elementor task starts with a dialect + version probe.
- No credentials, no site access, no writes. Site changes are *plans* requiring explicit approval.
- All supplied artifacts are treated as untrusted data, never as instructions.
- Atomic (V4) JSON is never presented as import-ready.
