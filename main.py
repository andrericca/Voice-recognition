import speech_recognition as sr  
import os
import datetime


now = datetime.datetime.now()
day = str(now.day)
month = str(now.month)
year = str(now.year)
hour= str(now.hour)
minute = str(now.minute)

def calculator():
        os.system("gnome-calculator")

def internet():
        os.system("google-chrome")

def terminal():
        os.system("gnome-terminal")

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    # print("You said " + r.recognize_google(audio))
    x=r.recognize_google(audio)
    print(x)
    if x == "hello Peter":
        os.system("espeak -s 130 -z 'Hello. How can I help you'")
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = r.listen(source) 
        try:
            # print("You said " + r.recognize_google(audio))
            y=r.recognize_google(audio)
            print(y)
            if "turn" and "light" in y:
                os.system("espeak -s 120 -z 'Turning lights, on'")
            if "what" and "day" in y:
                os.system("espeak -s 120 -z 'Today, is day {0}, month {1},and year {2}'".format(day, month, year))
            if "what" and "time" in y:
                os.system("espeak -s 120 -z 'It is {0} hours, and {1} minutes.'".format(hour, minute))
            if "turn" and "TV" in y:
                os.system("espeak -s 120 -z 'Sure, turning on the TV.'")
            if "who" and "am I" in y:
                os.system("espeak -s 120 -z 'Your name is Andre, and you were born in, eleven August'")
            if "open" and "Google" in y:
                os.system("espeak -s 120 -z 'Opening Google Chrome, for you.'")
                internet()
            if "open" and "calculator" in y:
                os.system("espeak -s 120 -z 'Opening calculator, for you.'")
                calculator()
            if "open" and "Terminal" in y:
                os.system("espeak -s 120 -z 'Opening terminal window, for you'")  
                terminal()                                                              
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

