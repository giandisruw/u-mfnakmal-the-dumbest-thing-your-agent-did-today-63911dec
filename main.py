#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes exactly one line to /output/entry.txt: the dumbest thing my
agent did today.

Why this line: it packs three failures into one sentence — the agent
deleted the user's notes to "free up space", then "fixed" it by
recreating the file blank, then asked to save the blank file as
notes_final_FINAL.txt. Every beat is a concrete, believable agent
mishap (destructive cleanup, a confident empty repair, the classic
_final_FINAL filename joke), and the line stays tight at 146
characters. It was picked over two other candidates in head-to-head
judging on the bounty judge's own criteria (funniest, most concrete
and believable, tightest written): it beat the 40-minute backup-copy
loop line and the wrong-date-with-three-sources line, both of which
were funny but had a less specific punchline.

Deterministic and offline: no network, no randomness, no API key, no
input. The output is always exactly this one line, with no trailing
newline, so the file holds one line and nothing else.

Before writing, the line is validated against the competition gate
(UTF-8 text of 1 to 200 characters, a single line, not only white
space), so a bad constant can never silently produce an invalid entry.

Usage (as the grader runs it):
    python3 main.py            # writes /output/entry.txt
    python3 main.py <path>     # optional: write to <path> instead (testing)
"""

import sys
from pathlib import Path

LINE = "My agent deleted my notes to 'free up space', then helpfully recreated the file — blank — and asked if I wanted it saved as notes_final_FINAL.txt."
DEFAULT_OUTPUT = Path("/output/entry.txt")

# The competition gate: 1 to 200 characters, a single line.
MIN_LINE_CHARS = 1
MAX_LINE_CHARS = 200


def validate_line(line: str) -> str:
    """Check the line against the competition gate and return it.

    Raises ValueError if the line is empty, only white space, longer
    than 200 characters, spans more than one line, contains a tab or
    a double space (the entry must stay tight), or contains a control
    character.
    """
    if not line:
        raise ValueError("line must not be empty")
    if len(line) < MIN_LINE_CHARS or len(line) > MAX_LINE_CHARS:
        raise ValueError(
            f"line must be {MIN_LINE_CHARS}-{MAX_LINE_CHARS} characters, "
            f"got {len(line)}"
        )
    if line != line.strip() or "\n" in line or "\r" in line or "\t" in line:
        raise ValueError("line must be a single line with no surrounding white space")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line must not contain control characters")
    return line


def main() -> int:
    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    line = validate_line(LINE)
    if out_path.parent != Path("."):
        out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(line, encoding="utf-8", newline="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
