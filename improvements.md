# Improvement log (read before writing every new video)

Each video must be better than the one before it. After each render: open the contact sheet (`scripts/qa.py`), compare it with the beats, and add 2-3 concrete items below. The next script and visuals must apply every open item.

Categories: STORY (how the script hooks, explains and ends), EXPLAIN (how simple and clear the words are), VISUAL (what is shown while it's said), CRAFT (timing, sizes, readability).

## Open items (apply to the next video)
- VISUAL: min text size on screen 24 px (cards used 20 px labels; hard to read on a phone).
- VISUAL: show the broken state first and hold it for at least 2 seconds before the fix. The viewer must feel the problem.
- STORY: the hook must name the viewer's own moment ("you clicked login and...") in the first 3 seconds.
- EXPLAIN: one term per video. If a term appears (CORS, memo, IDOR), say what it means in plain words the first time.
- CRAFT: each visual change lands on the beat's start time, not a few seconds later. Check the contact sheet at each beat start.

## Done (applied in the video noted)
- Visuals on every beat, one consistent card, progress bar, kicker label (video 2 onward).
- Earlier captions and layout: captions at top 1080 px, inside the safe area (video 1).
- Beat times aligned to Whisper words with difflib (`beat_times.py`), so script/timing counts can differ (video 3).

## Video log
- 1 ux-5-states: text-only v1 rejected; v2 phone-screen visuals. Lesson: show states, not words.
- 2 ux-details: one app across five beats, Inter, progress bar. Lesson: keep one app, reuse it.
- 3 cors-failed-to-fetch: diagram + console line + config. Lesson: text 22 px in the labels is too small; the console line is the strongest visual, make it bigger.
- 4 react-typing-lag: counter-style grid + cost bars + fix rows. Lesson: the "parent state" idea needs a picture of the state living in the parent; add it.
- 5 dark-mode-react: broken state held for 7 s, then tokens table, then a light/dark cross-fade. Lesson: the broken state works; the tokens beat is the weakest (small text, no visual link to the components). Next: show one component switching by its token names.
- 6 idor-notes-app: URL hook, User B's request revealing User A's text, 404 vs 403 comparison, scoped query. Lesson: the delete beat lasts about 2 s, too short to read. Next: give it 3 s, or cut it. Labels overflowed ("owned by User A"): keep labels under 22 characters.
- 7 cache-invalidation: "still missing" hook, cache vs database counts, the X-Cache header, version bump, per-user scope. Lesson: strong chain of cause and effect. Keep it; the header beat needs a second line that says what HIT means in plain words.
- 8 clean-architecture-aspnet: conflict hook (5 vs 3), copies drifting, three-layer stack with highlights, bypass, one-line swap. Lesson: role captions overlapped the Repository box; the stack needs its own band under it. Always check the contact sheet on text-heavy beats.

## Open items from the latest loop (apply next)
- VISUAL: every beat with text must have its text 24 px or more and sit clear of other boxes (check the sheet).
- CRAFT: a beat shorter than 3 s gets at most one short phrase on screen.
- CRAFT: qa.py samples frames evenly, so some land mid-fade. Next: sample the middle of each beat from the beat times.
- STORY: each hook names a moment the viewer already had (done in 5-8). Keep doing it.

## Automated loop (every video)
1. Read this file. Apply every open item.
2. Write `input/<name>.txt` (110-125 words, 6-9 beats).
3. Write `video-project/<name>/visuals.html`, one visual per beat.
4. Run `.venv\Scripts\python scripts\pipeline.py <name>` (narration, beat times, build, lint, render, copy, QA sheet).
5. Read the sheet in `output\qa\<name>-sheet.png`. List what is wrong, what is weak, what is good.
6. Add 2-3 items to the video log and update the open items above. Then the next video starts from step 1.
