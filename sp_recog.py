import speech_recognition as sr
import rcmd

while(1):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        person_speech = ""

        print("Say Something..")

        audio=r.listen(source)

        print("Recongnizing Now...")

        try:
            person_speech = r.recognize(audio)
            print("Speech was:" + person_speech)

        except Exception as e:
            print("Error: "+ str(e))    
        if "where I am standing" in person_speech:
        	rcmd.run_cmd_py("pwd")
        elif "shutdown" in person_speech:
        	rcmd.run_cmd_py("sudo shutdown")
        elif "exit" in person_speech:
        	exit()

           
