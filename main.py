# Import necessary libraries
import random
import os
import speech_recognition as sr
import goslate
import pyttsx3

# Set up text-to-speech engine
engine = pyttsx3.init()

# Set up speech recognition
r = sr.Recognizer()

# Set up translation service
gs = goslate.Goslate()

# Create a list of French phrases to teach
phrases = [
    "Bonjour, comment ça va?",  # "Hello, how are you?"
    "Je m'appelle _______.",  # "My name is _______."
    "Comment t'appelles-tu?",  # "What's your name?"
    "J'ai faim.",  # "I am hungry."
    "J'ai soif.",  # "I am thirsty."
    "Merci beaucoup.",  # "Thank you very much."
    "Excusez-moi.",  # "Excuse me."
    "Où est la toilette?",  # "Where is the bathroom?"
    "Au revoir!",  # "Goodbye!"
]

# Create a function to select a random phrase and present it to the user
def present_phrase():
    phrase = random.choice(phrases)
    print(f"Translate this phrase: {phrase}")
    engine.say(phrase)
    engine.runAndWait()

# Create a function to listen for the user's response
def listen_for_response():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        response = r.recognize_google(audio)
        return response
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError as e:
        print("Error processing request: {0}".format(e))
        return None

# Create a function to translate the user's response
def translate_response(response, target_language):
    if target_language.lower() == "french":
        translation = gs.translate(response, "fr")
        engine.say(translation)
        engine.runAndWait()
        return translation
    elif target_language.lower() == "english":
        translation = gs.translate(response, "en")
        engine.say(translation)
        engine.runAndWait()
        return translation
    else:
        return "Invalid target language."

# Main loop
while True:
    present_phrase()
    response = listen_for_response()
    if response is not None:
        print(f"You said: {response}")
        translate_response(response, "french")
    else:
        print("No response detected, please try again.")

