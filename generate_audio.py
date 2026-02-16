"""Generate narration audio for Biology Level 3 site using ElevenLabs TTS."""

from elevenlabs import ElevenLabs
import os
import time

API_KEY = "28c9a007ab7691a53034447c954a6a68e59d887445cb5dfe02c0dcc92198edbc"
VOICE_ID = "tghQO4ccpTi1eriPYDPW"  # Eliot (professional)
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "public", "audio")

# --- Narration scripts: natural spoken versions, paraphrased for voice ---

NARRATIONS = {
    # ── Week 3: How to Watch Videos ──────────────────────────────────────
    "how_to_watch": """
How to watch videos to actually learn.

OK, here's the thing. Just pressing play and letting a video run in the background? That's basically doing nothing. Research shows that students who passively watch videos barely learn more than students who never watched at all. So if you're going to spend the time watching, you might as well get something out of it. Here's how.

First — before you even press play — read the description underneath the video and ask yourself what you already know about the topic. This is called the pre-question effect. Having a question in your head before you watch primes your brain to notice the answers. It's like giving your brain a shopping list before you walk into the supermarket.

Second — while you're watching — pause every couple of minutes. Try to predict what's coming next. After a key point, look away from the screen and say the idea back to yourself in your own words. If you can't explain it, rewind and watch that bit again. This is retrieval practice — the act of pulling information out of your memory is actually what makes it stick, not just putting it in.

Third — and this is a big one — draw things. Don't just write notes in sentences. Sketch a diagram. Draw a woodlouse in a choice chamber. Draw arrows showing how taxis movement differs from kinesis. This is called dual coding — when you combine words and pictures, you create two separate memory traces in your brain, which makes the information much easier to recall later. A quick rough diagram is worth more than three paragraphs of neat writing.

Fourth — playback speed. Research shows that watching at one-and-a-half-times speed is fine for comprehension. Your brain can keep up. But two-times speed significantly hurts retention when you're learning new material. So first time through, stick to normal speed or one-and-a-half-times. Rewatching for revision? One-and-a-half-times is totally fine.

Fifth — the moment the video ends, close your laptop, flip your phone over, and write down everything you can remember. This is called a brain dump, and it's one of the most powerful study techniques there is. Don't worry about getting everything perfect. The effort of trying to recall is exactly what builds the memory. Then check what you missed, and focus on those gaps next time.

And finally — don't binge. Watching all twelve videos in one sitting might feel productive, but it doesn't produce lasting memory. The spacing effect tells us that spreading your watching across multiple days, even just two or three videos per session, leads to dramatically better retention. A little bit of forgetting between sessions is actually a good thing — it makes the next review harder, and that effort is what makes it stick.

So the bottom line is this. Watching a video is not studying. Watching a video while pausing, predicting, sketching, and testing yourself — that is studying. The students who do best aren't the ones who watch the most videos. They're the ones who think the hardest while watching.
""",

    # ── Week 4: Why We Write Answers ─────────────────────────────────────
    "week4_why_writing": """
Why are we doing this? Good question. There are two reasons I want you to write your answers here rather than just scribbling them in a notebook.

First, it gives you a record of your own thinking. Once you download the PDF, or copy your answers into OneNote, you've got a snapshot of how you explained these concepts today. Come back to it in a few weeks and you'll be able to see how much clearer your writing has become. That's genuinely useful revision.

Second, writing well matters in Biology. The external exams reward clear, precise explanations. I'll be reading through your submissions in Teams Assignments so I can give you feedback on how to tighten up your answers — not just the science, but how you communicate it. The earlier we start practising that, the better you'll be by the time exams come around.

So: answer the questions, download the PDF, and upload it to the Teams Assignment. If you'd also like a copy in your OneNote, use the Copy All Answers button and paste it straight in.
""",
}


def generate_audio():
    """Generate MP3 files for all narrations. Skips files that already exist."""
    client = ElevenLabs(api_key=API_KEY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for name, text in NARRATIONS.items():
        output_path = os.path.join(OUTPUT_DIR, f"{name}.mp3")

        # Skip if already generated
        if os.path.exists(output_path):
            print(f"  Skipping {name} (already exists)")
            continue

        print(f"  Generating {name}...")
        audio = client.text_to_speech.convert(
            voice_id=VOICE_ID,
            text=text.strip(),
            model_id=MODEL_ID,
        )

        with open(output_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        print(f"  ✓ Saved {output_path}")
        time.sleep(1)  # Be nice to the API


if __name__ == "__main__":
    generate_audio()
