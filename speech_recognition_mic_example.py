import speech_recognition as sr
import time, sys, os, subprocess


PROGRAMS = { 'Google': 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe', 'slak': ''}
recognizer = sr.Recognizer()

sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=1)

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

print(recognizer.recognize_google(audio)) #, language='sr-SP'
data = recognizer.recognize_google(audio).split() # , language='sr-SP'
print(data)


#data = ['Google']
if data[0] or data[1] in PROGRAMS:

	print(data[0] in PROGRAMS)
	subprocess.call(PROGRAMS[data[0]])