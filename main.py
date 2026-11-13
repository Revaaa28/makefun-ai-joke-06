#!/usr/bin/env python3
"""make.fun bounty ai-joke-03 entry.

Writes one one-liner about AI coding agents to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no clock —
two runs produce byte-identical output.
"""

import os

JOKE = "My AI pair programmer has senior-level confidence, junior-level memory, and an intern's relationship with the truth."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Bounty rule: the entry must be 1-280 characters. Guard it here so a
    # future joke swap can never silently produce an invalid entry.
    assert 0 < len(JOKE) <= 280, "joke outside the 1-280 character limit"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly the joke text, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
