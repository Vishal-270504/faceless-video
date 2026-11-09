"""Script text -> narration WAV (Kokoro, local) -> word timings JSON (faster-whisper, local).

Usage:  .venv\\Scripts\\python scripts\\make_voice.py input\\my-short.txt [voice] [speed]
Writes: output\\audio\\<name>.wav and output\\timings\\<name>.json
"""
import json
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent.parent
MAX_SECONDS = 60  # Shorts limit used by this project


def tts(text: str, out_wav: Path, voice: str, speed: float) -> float:
    from kokoro import KPipeline  # lazy import: slow to load

    pipe = KPipeline(lang_code="a")  # 'a' = American English
    chunks = [audio for _, _, audio in pipe(text, voice=voice, speed=speed, split_pattern=r"\n+")]
    audio = np.concatenate(chunks)
    sf.write(out_wav, audio, 24000)
    return len(audio) / 24000


def word_timings(wav: Path, out_json: Path) -> list[dict]:
    from faster_whisper import WhisperModel

    # Whisper wants 16 kHz float32; resample here so faster-whisper's own file decoder (PyAV) is skipped.
    audio, sr = sf.read(wav, dtype="float32")
    n16 = int(len(audio) * 16000 / sr)
    audio16 = np.interp(np.linspace(0, len(audio) - 1, n16), np.arange(len(audio)), audio).astype(np.float32)

    model = WhisperModel("base.en", device="cpu", compute_type="int8")  # small, fast, CPU-only
    segments, _ = model.transcribe(audio16, word_timestamps=True, vad_filter=False)
    words = [
        {"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)}
        for seg in segments
        for w in (seg.words or [])
        if w.word.strip()
    ]
    out_json.write_text(json.dumps(words, separators=(",", ":")), encoding="utf-8")
    return words


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: make_voice.py input/<name>.txt [voice] [speed]")
    src = Path(sys.argv[1]).resolve()
    voice = sys.argv[2] if len(sys.argv) > 2 else "af_heart"
    speed = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    name = src.stem
    text = src.read_text(encoding="utf-8").strip()

    wav = ROOT / "output" / "audio" / f"{name}.wav"
    timings = ROOT / "output" / "timings" / f"{name}.json"
    wav.parent.mkdir(parents=True, exist_ok=True)
    timings.parent.mkdir(parents=True, exist_ok=True)

    dur = tts(text, wav, voice, speed)
    words = word_timings(wav, timings)
    status = "OK" if dur <= MAX_SECONDS else f"TOO LONG (>{MAX_SECONDS}s), shorten the script"
    print(f"{status} | {name} | {dur:.1f}s | {len(words)} words | {wav} | {timings}")


if __name__ == "__main__":
    main()
