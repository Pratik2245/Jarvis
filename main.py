import pyttsx3
import speech_recognition as sr

def initialise_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # Female voice
    rate = engine.getProperty('rate')
    engine.setProperty("rate", rate - 50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 0.25)
    return engine

def speak(text, engine):
    engine.say(text)
    engine.runAndWait()

def UserCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjust for ambient noise and set energy threshold dynamically
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening.............................")
        audio = r.listen(source, timeout=10)  # Listen for up to 5 seconds
        try:
            print("Recognizing...................")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

# Initialize the engine once
engine = initialise_engine()

# Example usage
speak("Hello, I am Jarvis Nice to meet you", engine)
query = UserCommand()
if query:
    print(query.lower())
else:
    print("No valid command detected.")