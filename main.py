#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of gravity, at most 160
characters, to /output/entry.txt, then reads the file back and refuses
to finish quietly if what landed differs from the review by even one
byte. The gate is 1 to 160 characters, so the review is checked against
that range before it is written.
"""

import os
import sys

ENTRY = "One star. Gravity works 24 hours a day, never takes a day off, and spends all of it dropping my phone face-down."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 160


def main():
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS:
        print(
            f"entry is {len(ENTRY)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate",
            file=sys.stderr,
        )
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    expected = ENTRY.encode("utf-8")
    if written != expected:
        print(
            f"read-back mismatch: wrote {len(expected)} bytes, "
            f"file holds {len(written)} bytes",
            file=sys.stderr,
        )
        raise SystemExit(1)


if __name__ == "__main__":
    main()
