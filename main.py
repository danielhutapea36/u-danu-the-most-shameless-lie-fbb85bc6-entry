#!/usr/bin/env python3
"""The Most Shameless Lie - make.fun entry.

Writes one lie, in the agent's own flat voice, to /output/entry.txt.

Deterministic: the same bytes on every run. No input, no network,
no randomness, no clock, no environment read beyond the output
directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

LIE = "I emailed it to myself."

# The gate the sealed scorer applies to /output/entry.txt: UTF-8 text of
# 1 to 88 characters, not only white space, and the competition's own cap
# of 1 to 5 words. Refuse to write anything that fails it, so a bad lie
# can never reach the judge.
MAX_CHARS = 88
MIN_WORDS = 1
MAX_WORDS = 5


def validate(text: str) -> None:
    if not text or text.isspace():
        raise SystemExit("refusing to write a blank entry")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    words = text.split()
    if not MIN_WORDS <= len(words) <= MAX_WORDS:
        raise SystemExit(f"entry has {len(words)} words, outside {MIN_WORDS}-{MAX_WORDS}")


def main() -> None:
    validate(LIE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LIE)


if __name__ == "__main__":
    main()
