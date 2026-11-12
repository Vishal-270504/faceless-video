"""Runs every mechanical step for one video after its script and visuals.html exist.

Usage:  .venv\\Scripts\\python scripts\\pipeline.py <name>
Needs:  input\\<name>.txt and video-project\\<name>\\visuals.html (written by hand, see CLAUDE.md)
Steps:  narration -> beat times -> build -> lint -> render -> copy to output\\video -> QA sheet
Prints one line per step; stops at the first failure with the reason.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = str(ROOT / ".venv" / "Scripts" / "python.exe")


def run(cmd: str, cwd: Path = ROOT) -> str:
    r = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    out = (r.stdout + "\n" + r.stderr).strip()
    if r.returncode != 0:
        sys.exit(f"FAILED | {cmd} | {out.splitlines()[-1] if out else 'no output'}")
    return out


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: pipeline.py <name>")
    name = sys.argv[1]
    project = ROOT / "video-project" / name
    if not (ROOT / "input" / f"{name}.txt").exists():
        sys.exit(f"FAILED | missing input/{name}.txt")
    if not (project / "visuals.html").exists():
        sys.exit(f"FAILED | missing video-project/{name}/visuals.html")

    voice = run(f'"{PY}" scripts/make_voice.py input/{name}.txt')
    line = next((l for l in voice.splitlines() if l.startswith(("OK", "TOO LONG"))), "")
    print(line or "voice: no status line")
    if not line.startswith("OK"):
        sys.exit("FAILED | voice | see the line above")

    beats = run(f'"{PY}" scripts/beat_times.py {name}')
    print(f"beats: {len(beats.splitlines())}")

    print(run(f'"{PY}" scripts/build_short.py {name}').splitlines()[-1])

    lint = run("npx --yes hyperframes@0.9.26 lint", cwd=project)
    m = re.search(r"(\d+) error\(s\)", lint)
    if not m or m.group(1) != "0":
        sys.exit(f"FAILED | lint | {lint.splitlines()[-1]}")
    print("lint: 0 errors")

    run("npx --yes hyperframes@0.9.26 render", cwd=project)
    renders = sorted((project / "renders").glob("*.mp4"), key=lambda p: p.stat().st_mtime)
    if not renders:
        sys.exit("FAILED | render | no MP4 produced")
    out = ROOT / "output" / "video" / f"{name}.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(renders[-1], out)
    shutil.rmtree(project / "renders", ignore_errors=True)
    print(f"render: {out}")

    print(run(f'"{PY}" scripts/qa.py {name}'))


if __name__ == "__main__":
    main()
