# Import necessary libraries
import random
import os
import speech_recognition as sr
import pyttsx3
import requests
import json

# Set up text-to-speech engine
engine = pyttsx3.init()

# Set up speech recognition
r = sr.Recognizer()

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
        response = r.
