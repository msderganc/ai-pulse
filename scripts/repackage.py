#!/usr/bin/env python3
"""
Repackage ai-pulse.skill from the source files in this repo.

Self-contained — no dependency on the skill-creator plugin. Produces a ZIP
archive whose contents are prefixed with `ai-pulse/`, matching the layout
Claude Desktop expects.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

SKILL_NAME = "ai-pulse"
REPO_ROOT = Path(__file__).parent.parent.resolve()
OUTPUT = REPO_ROOT / f"{SKILL_NAME}.skill"


def collect_includes() -> list[tuple[Path, str]]:
    includes: list[tuple[Path, str]] = []

    skill_md = REPO_ROOT / "SKILL.md"
    if not skill_md.exists():
        sys.exit(f"error: {skill_md} not found")
    includes.append((skill_md, f"{SKILL_NAME}/SKILL.md"))

    refs_dir = REPO_ROOT / "references"
    if refs_dir.is_dir():
        for ref in sorted(refs_dir.glob("*.md")):
            includes.append((ref, f"{SKILL_NAME}/references/{ref.name}"))

    return includes


def main() -> None:
    includes = collect_includes()

    if OUTPUT.exists():
        OUTPUT.unlink()

    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for src, arc in includes:
            zf.write(src, arc)
            print(f"  Added: {arc}")

    print(f"\nRepackaged: {OUTPUT.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
