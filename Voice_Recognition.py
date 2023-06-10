import speech_recognition as sr
import webbrowser as web

# Create a recognizer object
r = sr.Recognizer()

# Here we enable the microphone for the voice recognition
with sr.Microphone() as source:
    print("SPEAK...")
    # Noise Cancelling
    r.adjust_for_ambient_noise(source)

    # Audio will be listened and it will be converted to text
    audio = r.listen(source)


try:
    # Recognize speech using Google Speech Recognition
    text = r.recognize_google(audio)
    print("You said:", text)
    web.open(text)


except sr.UnknownValueError:
    print("Sorry, I could not understand your speech.")





