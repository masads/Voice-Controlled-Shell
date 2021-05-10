import speech_recognition as sr
import rcmd
import pyttsx3

engine = pyttsx3.init()

def listen():
	
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

		return person_speech

        
def speak(speech):
    
    engine.say(speech)
    engine.runAndWait()
        


if __name__ == '__main__':
	speak("hello how can i help you?")
	while(1):
		person_speech = listen()
		if "where I am standing" in person_speech:
			rcmd.run_cmd_py("pwd")
		elif "shutdown" in person_speech:
			speak("do u want me to shutdown")
			person_speech = listen()
			if "yes" in person_speech:
				rcmd.run_cmd_py("shutdown -h now ")
		elif "exit" in person_speech:
			exit()


           
