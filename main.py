#!/usr/bin/env python3
"""Write a single-word entry to entry.txt.

The entry is one lowercase common noun, validated before writing and
re-validated after reading back from disk. Python 3 standard library
only, no network access.
"""

import os
import stat
import sys

WORD = "screensaver"


def validate(word):
    """Check that a value is one lowercase word, 1-30 characters."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1-30 characters")
    if word != word.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")
    if not word.isalpha():
        raise ValueError("entry must contain letters only")
    if word != word.lower():
        raise ValueError("entry must be lowercase")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    validate(WORD)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    os.chmod(path, 0o644)
    if stat.S_IMODE(os.stat(path).st_mode) != 0o644:
        raise SystemExit("entry.txt did not land with mode 0644")
    with open(path, "r", encoding="utf-8", newline="") as handle:
        landed = handle.read()
    validate(landed)
    if landed != WORD:
        raise SystemExit("entry on disk does not match the validated entry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
