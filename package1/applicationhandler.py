import subprocess
from package1 import VoiceOutput

def OpenApp(s):
    try:
        o=subprocess.check_output(["open","-a",s])
        if o.startswith("Unable"):
            VoiceOutput.Say("Unable to open "+str(s))

        
    except:
        print("application open failed")
        VoiceOutput.Say("Unable to open "+str(s))
        return
    