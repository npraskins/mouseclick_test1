
import subprocess
import pyttsx3

engine = pyttsx3.init()


def Say(text):
   # try:
    #    subprocess.call(["say",text])
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        return