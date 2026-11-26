#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one original fortune-cookie message for a software engineer
(a single line, 1-120 characters) to /output/entry.txt.
Python standard library only.
"""

import os

FORTUNE = "Your next deploy will go flawlessly, because this time you actually read the error message."


def main() -> None:
    line = FORTUNE.strip()
    if not (1 <= len(line) <= 120):
        raise ValueError(f"fortune must be 1-120 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
