#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes the smart speaker's one-line apology to /output/entry.txt.
Standard library only.
"""

import os

LINE = (
    "Sorry, I heard 'remind me to buy eggs' as 'remind me to buy eagles' "
    "\u2014 three are circling the house, and one has claimed the roof."
)


def main():
    line = LINE.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
