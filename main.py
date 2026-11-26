#!/usr/bin/env python3
"""The Best Meal You Ever Had — one sentence, at most 200 characters.

Writes the sentence to /output/entry.txt.
"""
import os

SENTENCE = (
    "At two in the morning in Bukittinggi I ate rendang with my hands off "
    "a banana leaf, beef falling apart, chilli oil on my fingers, while my "
    "grandmother laughed and pushed the rice closer."
)


def main():
    os.makedirs("/output", exist_ok=True)
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars"
    assert text == text.encode("utf-8").decode("utf-8")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
