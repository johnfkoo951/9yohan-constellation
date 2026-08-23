#!/usr/bin/env python3
"""Validate the 9Yohan persona canon mirror.

This script guards against the most common drift modes:
- missing individual persona cards
- missing required card sections
- stale old division names in build specs
- docs site not exposing each persona card
- canonical / constellation / persona mirror not agreeing on handles

It validates the DEV deployment mirror under docs/files/. The mothership remains
the source of truth; run this after mirroring mothership changes into this repo.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FILES = DOCS / "files"
PERSONAS = FILES / "personas"
DOCS_INDEX = DOCS / "index.html"

EXPECTED = {
    "00-9yohan-prime.md": "9yohan.prime",
    "901-kepler-map.md": "kepler.map",
    "902-goethe-sense.md": "goethe.sense",
    "903-dewey-learn.md": "dewey.learn",
    "904-bach-score.md": "bach.score",
    "905-neumann-compute.md": "neumann.compute",
    "906-baptist-prepare.md": "baptist.prepare",
    "907-mccarthy-reason.md": "mccarthy.reason",
    "908-huizinga-play.md": "huizinga.play",
    "909-calvin-advise.md": "calvin.advise",
}

SPECIALIST_SECTIONS = [
    "## Fixed identity",
    "## Mission contract",
    "## Invocation contract",
    "## System prompt seed",
    "## Output contract",
    "## Quality gates",
    "## Failure modes",
    "## Handoff",
]

PRIME_SECTIONS = [
    "## Fixed identity",
    "## Mission contract",
    "## Invocation contract",
    "## System prompt seed",
    "## Output contract",
    "## Quality gates",
    "## Failure modes",
]

STALE_PATTERNS = [
    r"902 Editorial & Content\b",
    r"905 Data Science\b",
    r"907 Technology & Development\b",
    r"909 Consulting & Professional\b",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    if not PERSONAS.exists():
        fail("missing docs/files/personas/")

    docs_index = read(DOCS_INDEX)
    canonical = read(FILES / "canonical.md")
    constellation = read(FILES / "constellation.md")

    for filename, handle in EXPECTED.items():
        path = PERSONAS / filename
        text = read(path)
        if handle not in text:
            fail(f"{filename} does not contain handle {handle}")
        if f'data-file="personas/{filename}"' not in docs_index:
            fail(f"docs/index.html does not expose personas/{filename}")
        sections = PRIME_SECTIONS if filename.startswith("00-") else SPECIALIST_SECTIONS
        for section in sections:
            if section not in text:
                fail(f"{filename} missing required section: {section}")

    for handle in EXPECTED.values():
        if handle not in canonical:
            fail(f"canonical.md missing handle {handle}")
        if handle not in constellation:
            fail(f"constellation.md missing handle {handle}")

    for pattern in STALE_PATTERNS:
        if re.search(pattern, canonical):
            fail(f"canonical.md has stale division phrase matching {pattern}")
        if re.search(pattern, constellation):
            fail(f"constellation.md has stale division phrase matching {pattern}")

    if "personas/README.md" not in docs_index:
        fail("docs/index.html missing personas/README.md index article")

    print("PASS: 9Yohan persona canon mirror is internally consistent.")


if __name__ == "__main__":
    main()
