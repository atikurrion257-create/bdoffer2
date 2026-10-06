#!/usr/bin/env python3
"""Build the installable Elementor Architect plugin ZIP.

- Copies the plugin tree into dist/stage/
- Copies each shared reference file into the skills that declare it (shared-map.json)
- Zips the result so that plugin.json sits at the ZIP root
- Emits a local marketplace entry for Codex (best-effort; adjust to your Codex version)

Usage:  python3 tools/build.py [--no-zip]
"""
from __future__ import annotations

import json
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "plugin" / "elementor-architect"
SHARED = SRC / "shared"
DIST = ROOT / "dist"
STAGE = DIST / "stage" / "elementor-architect"


def load_manifest() -> dict:
    with open(SRC / "plugin.json", encoding="utf-8") as fh:
        return json.load(fh)


def copy_tree() -> None:
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        SRC,
        STAGE,
        ignore=shutil.ignore_patterns("shared", "__pycache__", "*.pyc", ".DS_Store"),
    )


def inject_shared(skills_missing: list[str]) -> int:
    with open(ROOT / "shared-map.json", encoding="utf-8") as fh:
        shared_map = json.load(fh)["shared"]

    copies = 0
    for filename, skills in shared_map.items():
        source = SHARED / filename
        if not source.exists():
            print(f"  !! missing shared file: {filename}")
            continue
        for skill in skills:
            skill_dir = STAGE / "skills" / skill
            if not skill_dir.exists():
                skills_missing.append(skill)
                continue
            target_dir = skill_dir / "references"
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target_dir / filename)
            copies += 1
    return copies


def make_zip(version: str) -> Path:
    zip_path = DIST / f"elementor-architect-{version}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(STAGE.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(STAGE).as_posix())
    return zip_path


def make_marketplace(version: str) -> Path:
    manifest = load_manifest()
    marketplace = {
        "name": "private-plugins",
        "interface": {"displayName": "Private Plugins"},
        "plugins": [
            {
                "name": manifest["name"],
                "version": version,
                "description": manifest.get("description", ""),
                "source": {"path": "../plugin/elementor-architect"},
            }
        ],
    }
    out = DIST / "marketplace.json"
    out.write_text(json.dumps(marketplace, indent=2) + "\n", encoding="utf-8")
    return out


def report(copies: int, skills_missing: list[str]) -> None:
    skills = sorted(p.name for p in (STAGE / "skills").iterdir() if p.is_dir())
    print(f"\nPlugin staged at: {STAGE.relative_to(ROOT)}")
    print(f"Skills ({len(skills)}): {', '.join(skills)}")
    print(f"Shared reference copies injected: {copies}")
    if skills_missing:
        print(f"!! shared-map.json references unknown skills: {sorted(set(skills_missing))}")
    total = sum(1 for p in STAGE.rglob("*") if p.is_file())
    print(f"Files in package: {total}")
    for skill in skills:
        files = sorted(
            p.relative_to(STAGE / 'skills' / skill).as_posix()
            for p in (STAGE / "skills" / skill).rglob("*")
            if p.is_file()
        )
        print(f"  - {skill}: {', '.join(files)}")


def main() -> int:
    manifest = load_manifest()
    version = manifest.get("version", "0.0.0")
    DIST.mkdir(exist_ok=True)

    print(f"Building {manifest['name']} v{version}")
    copy_tree()
    missing: list[str] = []
    copies = inject_shared(missing)
    report(copies, missing)

    if "--no-zip" not in sys.argv:
        zip_path = make_zip(version)
        market = make_marketplace(version)
        print(f"\nZIP:         {zip_path.relative_to(ROOT)}  ({zip_path.stat().st_size // 1024} KB)")
        print(f"Marketplace: {market.relative_to(ROOT)}")
        print("\nNext: run docs/acceptance-tests.md against the installed plugin.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
