# Elementor Architect

A private ChatGPT/Codex plugin that behaves like a **senior Elementor + WordPress architect**: it plans native, editable, maintainable Elementor architecture and it audits existing work — including work produced by other AI agents — for the failures that make builds unmaintainable.

**Skills only.** No MCP server, no site connection, no credentials, no writes. It reads what you give it (screenshots, HTML, JSON, exports, URLs) and produces plans, audits, QA verdicts and quality reviews.

---

## Install

### ChatGPT (recommended)

1. Enable/verify Skills access for your account (sidebar → **Plugins** → **Skills** tab).
2. Install **Plugin Creator** from the plugin directory if you have not already.
3. Start a chat with `@plugin-creator` and paste the instruction below, attaching the plugin ZIP built by `tools/build.py`.

```
Install this plugin bundle as a private/local plugin named elementor-architect.
It is skills-only: do not add an MCP server, apps, authentication, hooks or UI.
Keep the skills/ folder structure and the references/ and assets/ files exactly as
they are in the ZIP. Do not rewrite skill descriptions. Then confirm the seven skills
were registered and list them.
```

### Codex / local folder

```bash
# Point a local marketplace at the plugin folder, or load it directly.
codex plugin marketplace add ./dist/marketplace.json   # if you generated one
```

The `.codex-plugin/plugin.json` compatibility manifest is included so the folder works with the Codex plugin loader as well.

### Manual install (skills only)

Upload individual skills from `skills/<name>/` via **Plugins → Skills → Create → Upload from your computer**. Note that uploading skills separately loses the shared `references/` copies, so prefer installing the whole plugin.

---

## The seven skills

| Skill | Use it for | Do not use it for |
|---|---|---|
| `elementor-native-architecture` | Native-ness decisions, V3-vs-V4 dialect, widget/element choice, refactors of HTML-heavy builds, architecture review of a plan | Auditing a specific artifact |
| `design-to-elementor-plan` | Screenshot / Figma / URL / HTML → decision-complete implementation blueprint | Auditing existing Elementor JSON |
| `elementor-structure-audit` | Auditing Elementor JSON, templates, exports, pasted builder output, rendered HTML; anti-pattern hunting | Planning new builds; performance/SEO/a11y |
| `elementor-qa-gate` | Pre-delivery QA, responsive review, editability verification, handoff sign-off | Discovering architecture problems in a plan |
| `wordpress-site-architecture` | Content model, Theme Builder parts + display conditions, template hierarchy, migrations | Field-level ACF design |
| `acf-dynamic-content-plan` | ACF field design, dynamic tags, repeatable content, editability contracts | Site-level content modelling |
| `site-quality-review` | Performance/CWV, SEO, accessibility — one prioritised register | Structural Elementor auditing |

**Hand-offs are explicit.** Skills state when they are handing to another skill and why; they never silently switch.

---

## Layout

```
elementor-architect/
├── plugin.json                 # portable manifest (ChatGPT + Codex)
├── .codex-plugin/plugin.json   # Codex compatibility manifest
├── skills/<skill>/SKILL.md     # the seven skills
├── skills/<skill>/references/  # shared + skill-specific reference files
├── skills/<skill>/assets/      # report / blueprint templates
└── shared/                     # single source of truth for shared references
```

`shared/` is the authoring source. The build script copies each shared file into the skills that need it (see `shared-map.json`), so every skill is self-contained after packaging and there is no duplicated editing.

## Build the installable ZIP

```bash
python3 tools/build.py
# → dist/elementor-architect-1.0.0.zip  (plugin.json at the ZIP root)
```

Then run `docs/acceptance-tests.md` against the installed plugin.

## Maintenance

- Every reference file carries a `verified against … on …` line. Review quarterly and after each Elementor minor / WordPress major.
- Never edit a shared reference inside a skill folder — edit it in `shared/` and rebuild.
- If the plugin gives a wrong answer, add that prompt to the acceptance suite as a failing case.
