#!/usr/bin/env python3
"""Check local Markdown link targets without network or application imports."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?(?<!\\)\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def main() -> int:
    failures = []
    checked = 0
    for document in sorted(ROOT.rglob("*.md")):
        if ".git" in document.relative_to(ROOT).parts:
            continue
        for match in LINK.finditer(document.read_text(encoding="utf-8")):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            checked += 1
            path = (document.parent / unquote(parsed.path)).resolve()
            if not path.is_relative_to(ROOT) or not path.exists():
                line = document.read_text(encoding="utf-8")[:match.start()].count("\n") + 1
                failures.append(f"{document.relative_to(ROOT)}:{line}: missing/unsafe target {target}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"PASS: {checked} local Markdown targets exist (anchors/external URLs not checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
