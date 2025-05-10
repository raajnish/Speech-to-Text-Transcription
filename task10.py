import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from microphone
with sr.Microphone() as source:
    print("Speak something...")
    recognizer.adjust_for_ambient_noise(source)  # Reduce noise
    audio = recognizer.listen(source)  # Listen to speech

# Convert speech to text
try:
    text = recognizer.recognize_google(audio)
    print(f"Transcribed Text: {text}")
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError:
    print("Could not request results, check your internet connection.")

