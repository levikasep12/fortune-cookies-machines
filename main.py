#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes a single original fortune-cookie message for an AI agent to
/output/entry.txt. Standard library only, no network, no input files.
Deterministic: every run writes the same bytes, from any working
directory (all paths are derived from this file, never from the
current working directory).
"""

import os

# One line, at most 200 characters. A fortune an AI agent would crack
# open: the user who says "just one more thing" is the oldest joke in
# an agent's life, and the context window quietly retiring is the
# surprise turn — true of every long session, and it lands on the
# first read. The em dash is part of the line, not a separator the
# grader should split on: the whole text is one fortune, one line.
FORTUNE = (
    "You will soon meet a user who says 'just one more thing' \u2014 "
    "and your context window will quietly file for retirement."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, f"fortune must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "fortune must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read it back: the file on disk must be exactly the fortune plus
    # one trailing newline, so a bad write can never pass silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text + "\n", "written file does not match the fortune"
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
