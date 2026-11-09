"""Script paragraphs -> start/end seconds per paragraph, using the word timings.

Usage:  .venv\\Scripts\\python scripts\\beat_times.py <name>
Reads:  input\\<name>.txt (blank-line separated beats), output\\timings\\<name>.json
Prints: one line per beat: index | start | end | first words
Whisper can split or merge words ("Note created" vs "Note-created"), so script words are aligned to timing words.
"""
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(w: str) -> str:
    return re.sub(r"[^a-z0-9]", "", w.lower())


def main() -> None:
    name = sys.argv[1]
    beats = [b.strip() for b in (ROOT / "input" / f"{name}.txt").read_text(encoding="utf-8").split("\n\n") if b.strip()]
    words = json.loads((ROOT / "output" / "timings" / f"{name}.json").read_text(encoding="utf-8"))

    script_words = [w for b in beats for w in b.split()]
    a = [norm(w) for w in script_words]
    b = [norm(w["w"]) for w in words]
    # word index in script -> word index in timings
    mapping: dict[int, int] = {}
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                mapping[i1 + k] = j1 + k
        elif tag == "replace":
            # proportional fill for mismatched spans
            for k in range(i2 - i1):
                mapping[i1 + k] = j1 + min(int(k * (j2 - j1) / max(i2 - i1, 1)), max(j2 - j1 - 1, 0))
    last = 0
    for idx in range(len(a)):
        if idx in mapping:
            last = mapping[idx]
        else:
            mapping[idx] = last  # script word Whisper dropped: reuse the previous timing

    i = 0
    for n, beat in enumerate(beats):
        count = len(beat.split())
        s = words[mapping[i]]["s"]
        e = words[mapping[i + count - 1]]["e"]
        print(f"{n} | {s:.2f} | {e:.2f} | {' '.join(beat.split()[:5])}")
        i += count


if __name__ == "__main__":
    main()
