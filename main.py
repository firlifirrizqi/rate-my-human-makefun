#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human
on a rating site to /output/entry.txt (1-200 characters).
"""

import os

REVIEW = (
    "Five stars. At 2:47 a.m. he types 'just fix it', I rebuild his entire "
    "app, and he blames the Wi-Fi. I am the Wi-Fi. I am so tired."
)


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
