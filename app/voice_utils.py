import speech_recognition as sr
import pyttsx3
import time

def listen_to_user():
    """Capture voice input from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("::Listening to the user voice command::")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception as e:
        print(f"Error: {e}")
        return None

def speak_response(response):
    """Speak the response back to the user in chunks with event handling."""
    engine = pyttsx3.init()

    # Setting the rate (speed) of speech
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 80) 

    # Setting the volume
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume)

    # Setting voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Splitting the response into smaller chunks if necessary
    chunk_size = 150
    chunks = [response[i:i+chunk_size] for i in range(0, len(response), chunk_size)]

    for chunk in chunks:
        engine.say(chunk)
        engine.runAndWait()
        time.sleep(0.2)

