import speech_recognition as sr  
import os

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   
try:
    # print("You said " + r.recognize_google(audio))
    x=r.recognize_google(audio)
    print(x)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))