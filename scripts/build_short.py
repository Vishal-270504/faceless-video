"""Timings JSON -> HyperFrames composition (vertical 1080x1920) with word-synced captions + narration audio.

Usage:  .venv\\Scripts\\python scripts\\build_short.py <name> ["Title card text"]
Reads:  output\\timings\\<name>.json, output\\audio\\<name>.wav
Writes: video-project\\<name>\\index.html  (then: cd video-project\\<name> && npx hyperframes render)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_WORDS = 3          # words per caption card
MAX_GAP = 0.35         # seconds of silence that force a new card
W, H = 1080, 1920

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
  <style>
    :root {{ --ground: #0b0b12; --ink: #ffffff; --accent: #ffd166; }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: var(--ground); }}
    #root {{ position: relative; width: {W}px; height: {H}px; font-family: "Arial Black", Impact, sans-serif; }}
    .caption {{
      position: absolute; left: 60px; right: 60px; top: 1180px; text-align: center;
      color: var(--ink); font-size: 110px; line-height: 1.1; text-transform: uppercase;
      text-shadow: 0 6px 24px rgba(0,0,0,.6); opacity: 0;
    }}
    .title {{
      position: absolute; left: 60px; right: 60px; top: 520px; text-align: center;
      color: var(--accent); font-size: 96px; line-height: 1.05; opacity: 0;
    }}
  </style>
</head>
<body>
  <div id="root" data-composition-id="main" data-start="0" data-duration="{duration:.2f}"
       data-width="{W}" data-height="{H}">
{title_el}
{caption_els}
    <audio data-start="0" data-duration="{duration:.2f}" data-track-index="2" data-volume="1"
           src="../../output/audio/{name}.wav"></audio>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{title_js}
{caption_js}
    window.__timelines["main"] = tl;
    tl.seek(0);
  </script>
</body>
</html>
"""


def chunk(words: list[dict]) -> list[dict]:
    cards, cur = [], []
    for i, w in enumerate(words):
        if cur and (w["s"] - cur[-1]["e"] > MAX_GAP or len(cur) >= MAX_WORDS):
            cards.append(cur)
            cur = []
        cur.append(w)
    if cur:
        cards.append(cur)
    return [
        {"text": " ".join(x["w"] for x in c), "s": c[0]["s"], "e": max(c[-1]["e"], c[0]["s"] + 0.3)}
        for c in cards
    ]


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit('usage: build_short.py <name> ["Title card text"]')
    name = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else ""
    words = json.loads((ROOT / "output" / "timings" / f"{name}.json").read_text(encoding="utf-8"))
    cards = chunk(words)
    duration = cards[-1]["e"] + 0.6

    caption_els, caption_js = [], []
    for i, c in enumerate(cards):
        caption_els.append(
            f'    <div id="c{i}" class="caption clip" data-start="{c["s"]:.2f}" '
            f'data-duration="{c["e"] - c["s"]:.2f}" data-track-index="1">{c["text"]}</div>'
        )
        caption_js.append(
            f'    tl.set("#c{i}", {{ opacity: 1, scale: 0.92 }}, {c["s"]:.2f});'
            f' tl.to("#c{i}", {{ scale: 1, duration: 0.12, ease: "power2.out" }}, {c["s"]:.2f});'
            f' tl.set("#c{i}", {{ opacity: 0 }}, {c["e"]:.2f});'
        )

    title_el = ""
    title_js = ""
    if title:
        safe = title.replace("<", "&lt;").replace(">", "&gt;")
        title_el = f'    <div id="title" class="title clip" data-start="0" data-duration="2.5" data-track-index="0">{safe}</div>'
        title_js = (
            '    tl.set("#title", { opacity: 1 }, 0);'
            ' tl.to("#title", { opacity: 0, duration: 0.4 }, 2.1);'
        )

    out_dir = ROOT / "video-project" / name
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(
        HTML.format(
            W=W, H=H, duration=duration, name=name,
            title_el=title_el, caption_els="\n".join(caption_els),
            title_js=title_js, caption_js="\n".join(caption_js),
        ),
        encoding="utf-8",
    )
    print(f"OK | {len(cards)} caption cards | {duration:.1f}s | {out_dir / 'index.html'}")


if __name__ == "__main__":
    main()
