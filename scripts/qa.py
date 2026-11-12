"""Quick QA for a rendered Short: duration, streams, and a 9-frame contact sheet.

Usage:  .venv\\Scripts\\python scripts\\qa.py <name>
Reads:  output\\video\\<name>.mp4
Writes: output\\qa\\<name>-sheet.png (gitignored) - open it and check each beat matches its visual.
Prints one line: OK or WARN with the reason.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    name = sys.argv[1]
    mp4 = ROOT / "output" / "video" / f"{name}.mp4"
    if not mp4.exists():
        sys.exit(f"WARN | missing {mp4}")
    probe = json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height",
         "-of", "json", str(mp4)], capture_output=True, text=True, check=True).stdout)
    dur = float(probe["format"]["duration"])
    kinds = [s["codec_type"] for s in probe["streams"]]
    video = next(s for s in probe["streams"] if s["codec_type"] == "video")
    sheet = ROOT / "output" / "qa" / f"{name}-sheet.png"
    sheet.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mp4), "-vf",
                    f"fps=9/{dur:.3f},scale=180:-1,tile=9x1", "-frames:v", "1", str(sheet)], check=True)
    problems = []
    if "audio" not in kinds:
        problems.append("no audio stream")
    if (video["width"], video["height"]) != (1080, 1920):
        problems.append(f"size {video['width']}x{video['height']}")
    if dur > 60:
        problems.append(f"{dur:.1f}s is over 60 s")
    status = "WARN" if problems else "OK"
    print(f"{status} | {name} | {dur:.1f}s | {video['width']}x{video['height']} | {','.join(kinds)} | "
          f"sheet {sheet}" + (f" | {'; '.join(problems)}" if problems else ""))


if __name__ == "__main__":
    main()
