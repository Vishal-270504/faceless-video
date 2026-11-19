"""Fetches ONE free Pixabay background clip for a video, within Pixabay's API rules.

Usage:  .venv\\Scripts\\python scripts\\fetch_bg.py <name> "<search words>"
Writes: video-project/<name>/assets/bg.mp4 (downloaded copy, never hotlinked)
        output/bgcache/<name>.json (search result, cached)
        output/bgcache/<name>.credit.txt (attribution line for the metadata)
Key:    read from ~/.faceless-keys/pixabay.key (outside the repo, never committed).
Rules:  one search and one download per video; cache everything; 1 s pause between calls.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY = (Path.home() / ".faceless-keys" / "pixabay.key").read_text(encoding="utf-8").strip()
CACHE = ROOT / "output" / "bgcache"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}  # default Python agent is blocked (403)


def search(query: str) -> dict:
    url = "https://pixabay.com/api/videos/?" + urllib.parse.urlencode({
        "key": KEY, "q": query, "per_page": 10, "safesearch": "true",
        "min_width": 1280, "order": "popular",
    })
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def pick(hits: list) -> dict | None:
    # a calm, longer clip that fills the frame: at least 8 s, medium is 1920x1080 or 1280x720
    for h in hits:
        if h.get("duration", 0) >= 8 and h["videos"]["medium"]["url"]:
            return h
    return hits[0] if hits else None


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit('usage: fetch_bg.py <name> "<search words>"')
    name, query = sys.argv[1], sys.argv[2]
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE / f"{name}.json"
    if cache_file.exists():
        data = json.loads(cache_file.read_text(encoding="utf-8"))
    else:
        data = search(query)
        cache_file.write_text(json.dumps(data), encoding="utf-8")
        time.sleep(1)
    hit = pick(data.get("hits", []))
    if not hit:
        sys.exit(f"FAILED | no Pixabay clip for '{query}'")

    dest = ROOT / "video-project" / name / "assets" / "bg.mp4"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        req = urllib.request.Request(hit["videos"]["medium"]["url"], headers=UA)
        with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
            f.write(r.read())
        time.sleep(1)
    credit = (f'Background video: {hit["user"]} on Pixabay ({hit["pageURL"]}), '
              f'Pixabay Content License.')
    (CACHE / f"{name}.credit.txt").write_text(credit, encoding="utf-8")
    print(f'OK | {name} | pixabay id {hit["id"]} | {hit["videos"]["medium"]["width"]}x'
          f'{hit["videos"]["medium"]["height"]} | {hit["duration"]}s | {dest}')


if __name__ == "__main__":
    main()
