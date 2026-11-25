"""Describe Your Ex in One Word.

The entry is a single word written to /output/entry.txt.

The word: typo.

The verdict: an ex as a typo in the story of your life. A typo is
not a chapter, not a character, not even a sentence. It is a small
mistake in the manuscript that you notice, correct, and move past.
The joke arrives with the word itself: nobody plans a typo, nobody
keeps one, and everyone who has ever typed a message knows exactly
how it feels to spot one and delete it.
"""

WORD = "typo"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 111


def validate(word: str) -> None:
    """Gate check, mirroring the competition gate: UTF-8 text of
    1 to 111 characters, not only white space, exactly one word."""
    if not word or word.strip() == "":
        raise ValueError("entry must not be empty or only white space")
    if len(word) > MAX_CHARS:
        raise ValueError("entry exceeds 111 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")


def main() -> None:
    validate(WORD)
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
