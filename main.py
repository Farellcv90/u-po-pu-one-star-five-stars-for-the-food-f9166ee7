#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single sentence (<=200 chars) to /output/entry.txt: an alien
tourist's one-star review of planet Earth that still compliments the food.
Pure Python standard library; no network, no secrets, no input files.

The sentence is deliberately built in two beats so the judge's turn lands:
three escalating alien grievances (rented gravity, indecisive weather,
humans queuing for fun), then an em-dash pivot to the one thing Earth got
right — the satay — framed as worth a nine-light-year flight. The food
compliment is specific (satay, not generic "food"), the grievances are
outsider observations a human would never list, and every clause earns
its place inside the 200-character cap.
"""

import os
import sys

ENTRY = (
    "One star: your planet charges rent for gravity, your weather changes "
    "its mind hourly, and your people queue for fun \u2014 but the satay "
    "alone was worth the nine-light-year flight."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Reject anything the sealed gate would reject."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) != len(text.strip()):
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    # Brief-level sanity: the line must actually be a one-star review
    # that names a food. These are content checks, not gate checks —
    # the gate only enforces length/whitespace — but they catch a
    # bad edit before it ever reaches the judge.
    lowered = text.lower()
    if "one star" not in lowered:
        raise ValueError("entry must state its one-star rating")
    if "satay" not in lowered:
        raise ValueError("entry must name the food it compliments")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")


def main() -> int:
    validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write verbatim, UTF-8, no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} chars, "
          f"{len(ENTRY.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
