from deep_translator import GoogleTranslator

# Language Codes
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

def translate_text(text, target_language):

    target_code = LANGUAGE_CODES[target_language]

    translated_text = GoogleTranslator(
        source="auto",
        target=target_code
    ).translate(text)

    return translated_text