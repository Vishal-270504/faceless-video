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

## Videos 13-18 (added 2026-11-18)
- 13 auth-authentication: hook names the viewer's own moment (you type your password). First script was 133 words, cut to 111 so it sits in the 110-125 band. Lesson: check the word count before writing visuals.
- 14 auth-authorization: split from the auth video. Uses 403 per the source talk, but video 6 says 404 for other users' notes. Lesson: one consistent rule across videos; the note above is an open decision.
- 15 db-indexes: highlight bar scans six rows, then an index card, then before/after bars. Lesson: no invented timings; say "far faster" unless measured.
- 16 aspnet-controller-service-repo: one-box-to-three-box stack. Lesson: about 0.8 s with no card between two cards; chain the cards.
- 17 api-never-trust-client: the teller diagram's 28 px labels wrap in 230 px boxes. Lesson: give small diagram boxes 24 px text or fewer words.
- 18 api-cache-per-user: MISS and HIT flows side by side. Lesson: overlaps video 7 (cache-invalidation); decide whether to keep both.

## Open items from videos 13-18 (apply next)
- VISUAL: no blank gap longer than 0.5 s between cards; fade the next card in while the last one fades out.
- CRAFT: check the word count (110-125) from make_voice before writing visuals.
- STORY: one rule for status codes across the series (401 missing token, 403 or 404 for other users' data).

## Videos 19-28: UI/UX series (added 2026-11-19)
- 19 ux-tap-targets: dashed 44 pt box around the icon; the fix shows a tap ring. Lesson: a caption at y 618 was clipped by the card edge; keep captions above y 600.
- 20 ux-hover-only-actions: laptop row with a cursor reveals the icons; the phone shows the hidden icons as ghosts. Lesson: a left/top tween fails lint (gsap_non_transform_motion); use x/y.
- 21 ux-thumb-zone: easy/hard zone map on a phone, then a bottom action bar. Lesson: the dashed reach line has to connect the thumb to the button.
- 22 ux-button-labels: real dialog mockup; chips of verbs against words to avoid. Lesson: the delete example was dropped because ux-details already covered delete confirmation.
- 23 ux-one-primary-button: five identical buttons, then a hierarchy screen, then three screens with the same primary spot.
- 24 ux-contrast: real ratios (#999 on white is 2.8:1, #595959 is 7:1). Lesson: check the frames where the fail badge appears; they are the proof.
- 25 ux-autosave-notes: notes editor with a Saving, then Saved status line, plus a Save-only failure. Lesson: tween by element id, not nth-of-type.
- 26 ux-optimistic-update: double tap, instant state, spinner in the broken version, rollback. Lesson: the takeaway card faded after the question card started; fixed.
- 27 ux-search-as-you-type: ten request tiles for "pagination", then a debounce bar. Lesson: no invented timings; say "about 300 ms".
- 28 ux-focus-after-dialog: a focus ring moves across the buttons; dialog trap; Escape chip. Lesson: three left/top tweens failed lint; all converted to x/y before the first render.

## Open items from videos 19-28 (apply next)
- VISUAL: keep all text above y 600 inside the card (the card ends at 640).
- CRAFT: animate position with x/y, never left/top, in every new visuals file.
- CRAFT: word counts ran 119-145 for this batch; aim for 110-125 before writing visuals.
- STORY: every video ends with the takeaway sentence, then the question.
