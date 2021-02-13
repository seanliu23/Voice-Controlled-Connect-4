import speech_recognition as sr
import keyboard
from Board import *
import Move as m
def listenforinput():
    key = ""
    while True:
        while True:
            key = str(win.checkKey())
            if (key in m.numlist) or (key in m.keylist) or (key == "p"):
                return key
            r = sr.Recognizer()
            r.dynamic_energy_threshold = True
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print(r.energy_threshold)
                audio = r.listen(source)
                print("audio found")
                key = str(win.checkKey())
                if (key in m.numlist) or (key in m.keylist) or (key == "p"):
                    return key
            try:
                voiceCommand = str(r.recognize_google(audio))
                print(voiceCommand)
                break
            except:
                pass

        if ('clear' in voiceCommand) or ('Clear' in voiceCommand):
            print("clearboard")
            return "p"
        if ('undo' in voiceCommand) or ('Undo' in voiceCommand):
            return 0
        if ('pop' in voiceCommand) or ('Pop' in voiceCommand) or ("top" in voiceCommand) or ("Top" in voiceCommand) or ("POP" in voiceCommand):
            if ("1" in voiceCommand) or ("one" in voiceCommand) or ('won' in voiceCommand):
                print("pop1")
                return "q"
            if ("2" in voiceCommand) or ("two" in voiceCommand) or ('too' in voiceCommand):
                print('pop2')
                return "w"
            if ("3" in voiceCommand) or("three" in voiceCommand):
                print('pop3')
                return "e"
            if ("4" in voiceCommand) or ("four" in voiceCommand) or ("for" in voiceCommand):
                print('pop4')
                return "r"
            if ("5" in voiceCommand) or ("five" in voiceCommand):
                print('pop5')
                return "t"
            if ("6" in voiceCommand) or ("six" in voiceCommand) or ("sex" in voiceCommand):
                print('pop6')
                return "y"
            if ("7" in voiceCommand) or ("seven" in voiceCommand):
                print('pop7')
                return "u"

        if ("play" in voiceCommand) or ("Play" in voiceCommand):
            if ("1" in voiceCommand) or ("one" in voiceCommand) or ('won' in voiceCommand):
                print('HI1')
                return 1
            if ("2" in voiceCommand) or ("two" in voiceCommand) or ('too' in voiceCommand) or ('to' in voiceCommand):
                print('HI2')
                return 2
            if ("3" in voiceCommand) or("three" in voiceCommand):
                print('HI3')
                return 3
            if ("4" in voiceCommand) or ("four" in voiceCommand) or ("for" in voiceCommand):
                print('HI4')
                return 4
            if ("5" in voiceCommand) or ("five" in voiceCommand):
                print('HI5')
                return 5
            if ("6" in voiceCommand) or ("six" in voiceCommand) or ("sex" in voiceCommand) or ("sticks" in voiceCommand):
                print('HI6')
                return 6
            if ("7" in voiceCommand) or ("seven" in voiceCommand):
                print('HI7')
                return 7