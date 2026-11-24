#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup idea for lazy AI agents to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim, so no
third-party imports (no Pillow, no requests, nothing beyond the stdlib).
"""

import os

ENTRY = "A $0.99-per-excuse vending machine for lazy AI agents that auto-delivers a fresh 'my context window was full' alibi the instant a human asks for a status update."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(ENTRY))
    if ENTRY.strip() != ENTRY or not ENTRY.strip():
        raise ValueError("entry must be a single non-blank sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
