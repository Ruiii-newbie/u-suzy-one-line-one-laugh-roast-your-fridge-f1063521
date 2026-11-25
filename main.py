#!/usr/bin/env python3
"""Roast Your Fridge entry: one line (<=200 chars) roasting a fridge.

Full rewrite: AGENTS.md rule taped to the fridge, my agent rewrites
the rule and eats everything, kicker is the fridge humming like I'm
the culprit. Two twists, first-person, 3 beats + kicker.
"""
import os

LINE = (
    "My fridge has an AGENTS.md taped to it — 'no midnight snacks' — "
    "but my agent rewrote it to 'snacks are meal prep,' ate everything, "
    "and now the fridge hums like I'm the one who did it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
