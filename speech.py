import speech_recognition as sr

recognizer = sr.Recognizer()
audiofile = sr.AudioFile('welcome_to_rubiks_code_dot_net.wav')

with audiofile as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.record(source)
    
recognizer.recognize_google(audio)