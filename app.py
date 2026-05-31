import streamlit as st
import os

from speech_to_text import recognize_speech
from translator import translate_text
from text_to_speech import text_to_speech

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Voice Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("🌍 AI Multilingual Voice Translator")

st.markdown(
    "### 🎤 Speak in one language and hear translation in another language"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------
st.markdown(
    """
    <style>

    div[data-baseweb="select"] > div {
        cursor: pointer;
    }

    button {
        cursor: pointer !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Create Folders
# ---------------------------------------------------
os.makedirs("audio_files", exist_ok=True)
os.makedirs("text_files", exist_ok=True)

# ---------------------------------------------------
# Languages
# ---------------------------------------------------
languages = {
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

# ---------------------------------------------------
# Language Dropdown
# ---------------------------------------------------
selected_language = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------
if "recognized_text" not in st.session_state:
    st.session_state.recognized_text = ""

# ---------------------------------------------------
# Start Speaking
# ---------------------------------------------------
if st.button("🎤 Start Speaking"):

    try:

        st.write("🎙️ Listening...")

        # ---------------------------------------------------
        # Speech Recognition
        # ---------------------------------------------------
        text = recognize_speech()

        # Save text in session state
        st.session_state.recognized_text = text

    except Exception as e:

        st.error(f"❌ Speech Recognition Error: {e}")

# ---------------------------------------------------
# Display Recognized Speech
# ---------------------------------------------------
if st.session_state.recognized_text != "":

    st.subheader("📝 Recognized Speech")

    recognized_text = st.text_area(
        "Recognized Text (You can edit if needed)",
        st.session_state.recognized_text,
        height=120
    )

    try:

        # ---------------------------------------------------
        # Translation
        # ---------------------------------------------------
        translated_text = translate_text(
            recognized_text,
            selected_language
        )

        # ---------------------------------------------------
        # Marathi Natural Fix
        # ---------------------------------------------------
        if selected_language == "Marathi":

            translated_text = translated_text.replace(
                "माझे नाव",
                "माझं नाव"
            )

        # ---------------------------------------------------
        # Display Translation
        # ---------------------------------------------------
        st.subheader("🌍 Translated Text")

        st.text_area(
            "Translated Output",
            translated_text,
            height=120
        )

        # ---------------------------------------------------
        # Save Translation
        # ---------------------------------------------------
        with open(
            "text_files/translated_output.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(translated_text)

        # ---------------------------------------------------
        # Text To Speech
        # ---------------------------------------------------
        audio_buffer = text_to_speech(
            translated_text,
            selected_language
        )

        st.success("✅ Translation Completed!")

        # ---------------------------------------------------
        # Play Audio
        # ---------------------------------------------------
        audio_bytes = audio_buffer.read()

        st.audio(
            audio_bytes,
            format="audio/mp3"
        )

        # ---------------------------------------------------
        # Download Button
        # ---------------------------------------------------
        st.download_button(
            label="⬇ Download Audio",
            data=audio_bytes,
            file_name=f"{selected_language}_translation.mp3",
            mime="audio/mp3"
        )

    except Exception as e:

        st.error(f"❌ Translation Error: {e}")