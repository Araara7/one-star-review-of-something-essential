#!/usr/bin/env python3
"""One-Star Review of Something Essential — deadpan one-star review (<=160 chars).

Writes the entry to /output/entry.txt. Deterministic: same bytes every run.

Entry choice: gravity — an everyday essential the brief lists. The grievance
is the sharpest true one (it drops everything you own), held deadpan with no
winking, and the sting turns in the last few words (it called it a law and
refused to apologise). One joke, told cleanly, in 107 characters.
"""

import os

ENTRY = "One star. Gravity dropped my phone, my keys, and my dignity, then called it a law and refused to apologise."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and verify: exactly one line, 1-160 chars, not whitespace-only.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt mismatch"
    assert 1 <= len(written) <= 160 and written.strip(), "entry out of gate"


if __name__ == "__main__":
    main()
