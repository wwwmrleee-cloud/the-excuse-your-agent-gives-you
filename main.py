#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single-line excuse to /output/entry.txt: the excuse an AI
agent gives its human after shipping a bug. The sealed gate requires
/output/entry.txt to be UTF-8 text of 1 to 200 characters, not only
white space, so the entry is checked against that gate before it is
written.
"""

import os

# The entry: one line, an agent's own excuse for a bug it shipped.
# Picked by simulated head-to-head judging over 8 candidates (see
# README): the turn lands in the last third, the voice is the agent's
# own ("in my head"), and the punch needs no second read.
ENTRY_TEXT = "In my defence, the bug worked in my head, in the tests, and in staging — production was the only environment with standards."


def _check_entry(text: str) -> None:
    """Enforce the competition gate before writing anything out."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    _check_entry(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
