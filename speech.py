import speech_recognition as sr

recognizer = sr.Recognizer()
audiofile = sr.AudioFile('speech.wav')

with audiofile as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.record(source)
    
print(recognizer.recognize_google(audio))