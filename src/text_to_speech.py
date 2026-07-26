from gtts import gTTS
import uuid
import os


def text_to_speech(text, language="en"):
    filename = f"temp/{uuid.uuid4()}.mp3"

    os.makedirs("temp", exist_ok=True)

    tts = gTTS(
        text=text,
        lang=language,
    )

    tts.save(filename)

    return filename