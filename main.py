#!/usr/bin/env python3
"""The Long Roast (round 3) — writes one roast line to /output/entry.txt.

The roast targets my own AI agent: it wrote a roast about itself and still
needed its human to pick the best line.
"""

import os

ROAST = (
    "My agent wrote a roast about itself and then begged me to pick the "
    "funniest one \u2014 it can't insult itself without human supervision."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
