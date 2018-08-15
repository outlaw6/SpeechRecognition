import speech_recognition as sr

recognizer = sr.Recognizer()

sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=1)

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    
print(recognizer.recognize_google(audio))