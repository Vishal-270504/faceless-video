# Faceless Shorts Factory: instructions for Claude

Read this whole file before doing any video task. It is the only context you need. Do not ask the user for paths, commands or the workflow again.

## What this project does
Turns a short script into a finished faceless YouTube Short (1080x1920, under 60 s) entirely on this PC, free:
script -> narration (Kokoro TTS, local) -> word timings (faster-whisper, local) -> visuals (HyperFrames HTML, one per beat) + word-synced captions -> MP4.

Repo: https://github.com/Vishal-270504/faceless-video (public). This folder is its clone.
Topic source (outside the repo, the user's file): `C:\Users\Visha\OneDrive\Desktop\video-topics-brief.md`. Use it to pick the next topic. Do not push it.

## Folder map
- `CLAUDE.md` - these instructions.
- `.claude/agents/` - agents for each pipeline step (see Agents).
- `scripts/make_voice.py` - script -> `output/audio/<name>.wav` + `output/timings/<name>.json`.
- `scripts/beat_times.py` - prints each script beat's start and end time from the timings.
- `scripts/build_short.py` - builds `video-project/<name>/index.html` (captions + audio + visuals.html).
- `input/<name>.txt` - the narration script (committed).
- `output/audio/`, `output/timings/`, `output/video/` - committed artifacts for each video.
- `video-project/<name>/` - `index.html` (generated), `visuals.html` (hand-written, committed). `assets/` and `renders/` are generated and not committed.
- `metadata/all-videos.md` - title, description and thumbnail prompt for every video, one entry per video (committed). Add a new entry for each new video.
- `assets/music/`, `assets/broll/` - optional user-supplied files. Empty now.
- `.venv/` - local Python env. Not committed.

## Environment (already installed on this PC)
- Windows 11. Shell: PowerShell or Git Bash. Use the venv Python explicitly: `./.venv/Scripts/python.exe` (Bash) or `.venv\Scripts\python.exe` (PowerShell).
- Node 22+, FFmpeg, Python 3.12, git (HTTPS push to the repo).
- HyperFrames plugin is installed (`hyperframes@hyperframes`). CLI is always run as `npx --yes hyperframes@0.9.26 <cmd>`.
- If `.venv` is missing: `python -m venv .venv` then `.venv\Scripts\python -m pip install torch --index-url https://download.pytorch.org/whl/cpu kokoro soundfile faster-whisper numpy`. First run downloads Kokoro (~330 MB) and Whisper `base.en` (~150 MB) once.

## Improvement loop (read first, every video)
- Read `improvements.md` before writing any script or visual. Apply every open item.
- After each video: read its contact sheet, add 2-3 concrete items to the log, update the open items.
- Each video must be better than the last in story, explanation and visuals. If nothing improved, say why in the log.
- Mechanical steps run in one command: `.venv\Scripts\python scripts\pipeline.py <name>` (narration, beat times, build, lint, render, copy, QA). It needs `input/<name>.txt` and `video-project/<name>/visuals.html` first.

## Full workflow for one video (`<name>` = kebab-case slug, e.g. `ux-5-states`)
1. **Pick the topic** from the brief (the next one whose status is not Recorded/Uploaded). Skip topics already in the status list below.
2. **Write the script** `input/<name>.txt` following the Script rules below.
3. **Narration:** `./.venv/Scripts/python.exe scripts/make_voice.py input/<name>.txt`
   - Must print `OK`. If `TOO LONG` or the word count is off, shorten the script and rerun.
   - Output words count may differ from the script by 1-2 (Whisper). That is fine.
4. **Beat times:** `./.venv/Scripts/python.exe scripts/beat_times.py <name>`
   - Prints `index | start | end | first words` for each beat (beats are blank-line separated paragraphs in the script).
   - Use these times in visuals.html. Do not guess times.
5. **Visuals:** write `video-project/<name>/visuals.html` (rules below). Create the folder first if needed.
6. **Build:** `./.venv/Scripts/python.exe scripts/build_short.py <name>` (no title card by default).
   - It copies the WAV into `video-project/<name>/assets/` and writes `index.html`.
7. **Lint:** `cd video-project/<name> && npx --yes hyperframes@0.9.26 lint`. Must show `0 error(s)`. Warnings about nested structure are accepted. Any error: fix and rebuild.
8. **Render:** in the same folder, `npx --yes hyperframes@0.9.26 render` (about 2-6 min). The MP4 goes to `video-project/<name>/renders/`.
9. **Publish locally:** copy the newest `renders/*.mp4` to `output/video/<name>.mp4`, then delete `video-project/<name>/renders/`.
10. **Check the result:** use ffmpeg to pull one frame per beat (`ffmpeg -ss <mid-beat> -i output/video/<name>.mp4 -frames:v 1 -vf scale=360:-1 <png>`). Put them in a contact sheet with `hstack`, read it, and confirm each visual matches its beat and captions are readable. Fix and re-render if not. Check that the video has an audio stream with ffprobe.
11. **Metadata:** add an entry to `metadata/all-videos.md` (format below).
12. **Commit and push only when the user asks.** Then delete local media (see Local cleanup).

## Script rules
- 110-125 spoken words (about 45 s). Hard limits: under 60 s; the script must print OK.
- Plain text in `input/<name>.txt`. No headings, no stage directions, no emojis, no brackets.
- Beats are separated by one blank line. Aim for 6-9 beats: hook, points (2-5), takeaway, question.
- Structure: hook (name the viewer's problem) -> idea (one sentence) -> points (one fix or example per beat, each starting with a short label like "Errors:") -> takeaway (the rule to remember) -> question (invite a comment).
- Simple words. Explain a technical term in a few words the first time, or drop it. One code name is fine; no code walkthroughs.
- One idea per video. Show the broken version before the fix.
- Cover everything the viewer needs for the topic, not just a teaser. The brief's "Broken version" and "Fix" lists are the checklist.

## Visuals rules (`video-project/<name>/visuals.html`)
This file is inserted into the composition. Format:
```
<style> ...CSS... </style>
<markup: the visual divs, no <html> or <body> tags>
<script> ...GSAP timeline calls on the existing `tl`... </script>
```
- Every beat gets a visual that shows it. No text-only videos. Visuals show the real UI or diagram of the topic, not decorative art.
- Keep one consistent look per video (same app, same palette, same grid). Good default that worked: dark background `#0b0b12` (already the page background), a single accent colour, a central card at `left:90px; top:330px; width:900px; height:640px`, a kicker label above it at `top:236px` and a 5-segment progress bar at `top:292px`.
- Visual area: keep all visuals between `top` 168 and 1000 px. Captions are placed by the build at `top:1080px`, two to three lines. Nothing important under 1330 px.
- Fonts: only bundled ones resolve by name: **Inter** (weights 400, 700, 900 only). Do not use 800, Arial, Helvetica or other system fonts without `@font-face`.
- Timing: each timed element has `class="clip"`, `data-start` and `data-duration` (seconds). Set times from `beat_times.py`. Land end states slightly before the end. Never exceed the video length (about beat 8 end + 0.6 s); lint warns otherwise.
- Animation: use GSAP on the existing `tl` with absolute times, e.g. `tl.from("#x", {opacity:0, y:20, duration:0.4, ease:"power3.out"}, 12.3);`. Use eases like `power2.out`, `power3.out`, `back.out(2)` sparingly. Use `repeat` only with a finite number (never `-1`).
- No `Date.now()`, no `Math.random()`, no network fetches, no timers.
- Use `opacity` on `.clip` elements; do not tween `display`/`visibility`. Use `scale`/`y`/`x` for motion on children.
- No emojis, no clip-art, no gradient text, no glow blobs, no stock-looking icons. Checkmarks and close marks are drawn with CSS borders.
- Keep it simple and specific: real UI states, real labels, real button text from the script.

## Quality bar
- Each beat is readable on a phone at arm's length. Text in visuals is at least 22 px at 1080 width.
- The viewer should understand the topic from the visuals even muted (captions cover the words).
- Before calling a video done: lint 0 errors, render complete, contact sheet checked, audio present.

## Metadata (`metadata/all-videos.md`)
Write this for every finished video, as one entry in `metadata/all-videos.md`:
```
# <Title>
**Title:** <max 60 characters, plain, no clickbait lies>

**Description:**
<2-3 sentences: the problem and what the viewer learns.>

#hashtag #hashtag #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. <background>. <main text, exact, in quotes>. <one central illustration of the topic>. Flat design, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.
```
Tell the user the thumbnail text may be misspelt by ChatGPT.

## Local cleanup (after commit and push)
Deleting local media keeps the disk free. Keep the scripts, CLAUDE.md, agents, `metadata/` and `.venv`.
- Delete: `input/<name>.txt`, `output/audio/<name>.wav`, `output/timings/<name>.json`, `output/video/<name>.mp4`, `video-project/<name>/` (all of it).
- Restore a video later: `git checkout -- input/<name>.txt output/audio/<name>.wav output/timings/<name>.json output/video/<name>.mp4 video-project/<name>` (paths from the repo; `video-project/<name>/assets/` is regenerated by build).
- Never delete committed files without the user's OK, and never run `git clean` or `git reset --hard`.

## Git rules
- Commit and push only when the user asks.
- Commit identity is the user's git config (already set). Commit messages end with the attribution line the user's session specifies (Co-Authored-By for Claude).
- Repo is public: do not commit secrets, the topics brief, or anything personal.
- Do not commit `.venv`, `renders/`, `video-project/*/assets/`, `node_modules/` (all in `.gitignore`).

## Agents (`.claude/agents/`)
Run in this order. The main session coordinates; agents do the step.
- `script-writer` - writes `input/<name>.txt`.
- `voice-producer` - runs `make_voice.py` and `beat_times.py`.
- `visual-builder` - writes `visuals.html` from the beat times and the rules above.
- `video-builder` - runs `build_short.py`, lint, render, and copies the MP4 to `output/video/`.

The main session still does the visual QA (contact sheet) and metadata.

## Token-saving rules
- Do not read generated files (WAV, timings JSON, MP4, large HTML). Use one-line script output and ffmpeg frame extracts.
- Do not re-read a file you just wrote. Edit it in place.
- One render per video unless something broke. Lint first.
- Use the scripts for captions and timing. Write HTML only for visuals.

## Known gotchas (already solved; do not rediscover)
- Renderer needs the narration `<audio id="narration">` with a file inside the project. `build_short.py` handles it; a missing id = silent video.
- Whisper can split or merge a word, so word counts may differ by 1-2. `beat_times.py` aligns them.
- faster-whisper must get a numpy array (not a file path) because of a PyAV version clash. `make_voice.py` already does this.
- Do not use Arial/Helvetica/Impact; use bundled Inter.
- The HyperFrames plugin marketplace needed `git -C <plugins/marketplaces/hyperframes> lfs pull` on this PC; already done.
- `build_short.py` output is 1080x1920; the sample `sample-hello` has no visuals and its audio was silent in an early render (its repo copy still has that bug).

## Video status (completed = video rendered in output/video; metadata written when asked)
- 1 `ux-5-states` - The 5 UX states every app needs. Rendered. Metadata in `metadata/all-videos.md`.
- 2 `ux-details` - 5 small UX details that make an app feel professional. Rendered. Metadata in `metadata/all-videos.md`.
- 3 `cors-failed-to-fetch` - "Failed to fetch" is probably CORS. Rendered. Metadata in `metadata/all-videos.md`.
- 4 `react-typing-lag` - Why your React app gets slow when you type. Rendered. Metadata in `metadata/all-videos.md`.
- 5 `dark-mode-react` - Dark mode in React in 5 minutes (done right). Rendered. Metadata in `metadata/all-videos.md`.
- 6 `idor-notes-app` - API leaks other users' data (IDOR). Rendered. Metadata in `metadata/all-videos.md`.
- 7 `cache-invalidation` - Why your API returns old data. Rendered. Metadata in `metadata/all-videos.md`.
- 8 `clean-architecture-aspnet` - Clean architecture in ASP.NET Core. Rendered. Metadata in `metadata/all-videos.md`.
All eight topics on the brief have a rendered video and an entry in metadata/all-videos.md.

## Install check (fresh PC)
Node 22+, FFmpeg on PATH, Python 3.12, the venv above, then `npx --yes hyperframes@0.9.26 --version` must work.
