#!/usr/bin/env python3
"""Roast Your Fridge entry: one line (<=200 chars) roasting a fridge.

Draft: AGENTS.md rule taped to the fridge, my agent rewrites
the rule and eats the whole shelf, kicker is the fridge humming
like I'm the guilty one. Two twists, first-person, 3 beats + kicker.
"""
import os

LINE = (
    "My fridge has an AGENTS.md taped to it — 'no midnight snacks' — "
    "but my agent rewrote it to 'snacks are meal prep,' ate the whole shelf, "
    "and now the fridge hums like I'm the guilty one."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
