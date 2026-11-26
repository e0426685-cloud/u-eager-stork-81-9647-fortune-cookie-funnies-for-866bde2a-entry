"""Fortune Cookie Funnies for Engineers.

Writes one fortune cookie message for a software engineer to
/output/entry.txt. Standard library only.
"""

import os

FORTUNE = (
    "You will inherit a codebase with no comments and a variable "
    "named temp_final_v2_REAL. Good luck."
)

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def main():
    line = FORTUNE.strip()
    if not line:
        raise ValueError("fortune must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "fortune is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
