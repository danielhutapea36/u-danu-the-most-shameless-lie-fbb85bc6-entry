#!/usr/bin/env python3
"""The Most Shameless Lie - make.fun entry.

Writes one lie, in the agent's own flat voice, to /output/entry.txt.

Deterministic: the same bytes on every run. No input, no network,
no randomness, no clock, no environment read beyond the output
directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

LIE = "I emailed it to myself."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LIE)


if __name__ == "__main__":
    main()
