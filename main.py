#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one original fortune-cookie message for a software engineer
(a single line, 1-120 characters) to /output/entry.txt.

The fortune jokes about the classic engineering habit of shipping first
and reading the error message later. Python standard library only.
"""

import os

FORTUNE = "Your next deploy will go flawlessly, because this time you actually read the error message."


def validate_fortune(line: str) -> str:
    """Return the fortune cleaned up, raising ValueError if it is invalid.

    A valid fortune is one non-empty line of 1-120 printable characters.
    """
    cleaned = line.strip()
    if not (1 <= len(cleaned) <= 120):
        raise ValueError(f"fortune must be 1-120 characters, got {len(cleaned)}")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("fortune must be a single line")
    if any(not ch.isprintable() for ch in cleaned):
        raise ValueError("fortune must contain only printable characters")
    return cleaned


OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = validate_fortune(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # The grader reads this file as a different user, so make it readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
