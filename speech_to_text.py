import speech_recognition as sr

def recognize_speech():

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 0.8
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(
            source,
            timeout=3,
            phrase_time_limit=4
        )

    text = recognizer.recognize_google(
        audio,
        language="en-IN"
    )

    return text