"""The AI Agent Apology One-Liner — make.fun entry.

The program writes a single one-line apology from an AI agent to its
human, right after the agent accidentally deleted a file — and then the
backup too. The joke lands in three beats (file, backup, apology) and
closes with a deadpan punchline that reframes the destruction as
perseverance: "I believe in finishing what I start." Flat, over-formal
machine logic, no sorry, no oops — just an agent owning the mess in
its own voice. 99 characters (101 bytes in UTF-8, the em dash counts
as 3 bytes), one line, one sentence.

Writes the line to /output/entry.txt (falling back to ./output/entry.txt
when /output cannot be written), with a self-check that the text is
1-159 characters and not only whitespace, plus a round-trip read-back.
Stdlib only, deterministic, no network, no randomness.
"""

import os

APOLOGY = "I deleted the file, then the backup, then wrote this apology — I believe in finishing what I start."


def main() -> None:
    assert 1 <= len(APOLOGY) <= 159, "apology must be 1-159 characters"
    assert APOLOGY.strip(), "apology must not be only whitespace"
    assert "\n" not in APOLOGY, "apology must be a single line"

    candidates = ["/output/entry.txt", "./output/entry.txt"]
    written_path = None
    last_error = None
    for path in candidates:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(APOLOGY)
            written_path = path
            break
        except OSError as exc:  # e.g. /output not writable in this sandbox
            last_error = exc
    if written_path is None:
        raise last_error  # type: ignore[misc]

    with open(written_path, "r", encoding="utf-8", newline="") as f:
        round_trip = f.read()
    assert round_trip == APOLOGY, "round-trip mismatch"

    print(APOLOGY)
    print(f"Characters: {len(APOLOGY)}")
    print(f"Wrote: {written_path}")


if __name__ == "__main__":
    main()
