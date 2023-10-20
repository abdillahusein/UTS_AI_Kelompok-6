import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser

print("Jarvis")
MASTER = "rizal"
recognizer = sr.Recognizer()
engine = pyttsx3.init("sapi5")
# Set the speaking rate
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
# Set the voice (0 for male, 1 for female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Hello, Good morning " + MASTER)
    elif 12 <= hour < 18:
        speak("Hello, Good afternoon " + MASTER)
    else:
        speak("Hello, Good evening " + MASTER)

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            if "jarvis" in command:
                print(command)
                command = command.replace("jarvis", "")
                speak(command)
    except:
        pass

    return command

def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        print("Playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        speak("The current time is " + time)
    elif "open Google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "search" in command:
        search_query = command.replace("search", "")
        speak("Searching on Google for " + search_query)
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "wikipedia" in command:
        src = command.replace("wikipedia", "")
        info = wikipedia.summary(src, sentences=1)
        speak("Searching Wikipedia")
        print(info)
        speak(info)
    else:
        speak("No command given")
        print(command)

wishMe()

while True:   
    MASTER = "rizal"
    recognizer = sr.Recognizer()
    engine = pyttsx3.init("sapi5")
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    speak("I am Jarvis. What do you want?")
    run_jarvis()
