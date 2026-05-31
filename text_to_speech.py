from gtts import gTTS
import io

LANGUAGE_CODES = {
    "Hindi": "hi",
    "Marathi": "mr",
    "Telugu": "te",
    "Tamil": "ta",
    "Bengali": "bn",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

def text_to_speech(text, language):

    language_code = LANGUAGE_CODES[language]

    tts = gTTS(
        text=text,
        lang=language_code
    )

    audio_buffer = io.BytesIO()

    tts.write_to_fp(audio_buffer)

    audio_buffer.seek(0)

    return audio_buffer