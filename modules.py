import speech_recognition as sr
import ctypes

## Build Command - cc -fPIC -shared -o functions.so functions.c ##

so_file = "/home/masads/os/functions.so"
my_functions = ctypes.CDLL(so_file)

my_functions.checkFile.restype  = ctypes.c_char_p


def listen():
	
	r=sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		person_speech = ""

		print("Say Something..")
        

		audio=r.listen(source)
		print("Recongnizing Now...")

		try:
			person_speech = r.recognize_google(audio)
			print("Speech was:" + person_speech)
		except Exception as e:
			print("Error: "+ str(e))    

		return person_speech

def speak(speech, engine):
    
    engine.say(speech)
    engine.runAndWait()
    
def proccess_text(path, text,engine):
	
	if "change directory" in text:
		speak("Which directory you want to go to?",engine)
		string1 = input()
		b_string1 = string1.encode('utf-8')
		b_path = path.encode('utf-8')
		my_functions.checkFile.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
		string2 = my_functions.checkFile(b_string1,b_path).decode()
		if " " in string2:
			print("folder not exist")
		else:
			path=path+"/"+string2
		print(path)
	elif "list file" in text:
		command = ";ls"
		string1 = "cd " + path + command
		print(string1)
		b_string1 = string1.encode('utf-8')
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)
	elif "create a file" in text: #not completed yet	
		speak("Tell the file name",engine)
		string0 = input()
		speak("Tell the file extension",engine)
		ext = input()
		string0 = string0 + "." + ext
		b_string0 = string0.encode('utf-8')
		b_path = path.encode('utf-8')
		my_functions.checkFile.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
		fileNexist = my_functions.checkFile(b_string0,b_path).decode()
		if " " in fileNexist:
			string1 = "cd " + path + ";touch " + string0
			b_string1 = string1.encode('utf-8')
			my_functions.run_command.argtypes = [ctypes.c_char_p]
			my_functions.run_command(b_string1)
		else:
			print(fileNexist + " file alread exist")
	elif "open nano editor" in text:
		speak("Tell the file name",engine)
		string0 = input()
		string1 = "cd " + path + ";nano " + string0 + ".*"
		b_string1 = string1.encode('utf-8')
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)
	elif "open geditor" in text:
		speak("Tell the file name",engine)
		string0 = input()
		string1 = "cd " + path + ";gedit " + string0 + ".*"
		b_string1 = string1.encode('utf-8')
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)
	elif "make directory" in text: #not completed yet
		speak("Tell the file name",engine)
		string0 = input()
		b_string0 = string0.encode('utf-8')
		b_path = path.encode('utf-8')
		my_functions.checkFile.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
		fileNexist = my_functions.checkFile(b_string0,b_path).decode()
		if " " in fileNexist:
			string1 = "cd " + path + ";mkdir " + string0
			b_string1 = string1.encode('utf-8')
			my_functions.run_command.argtypes = [ctypes.c_char_p]
			my_functions.run_command(b_string1)
		else:
			print(fileNexist + " folder alread exist")
	elif "list users" in text:
        	string0 = "ls /home"
        	b_string1 = string0.encode('utf-8')
        	my_functions.run_command.argtypes=[ctypes.c_char_p]
        	my_functions.run_command(b_string1)
	elif "shutdown" in text:
		string0 = "shutdown -h now"
		b_string1 = string0.encode('utf-8')
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)
	elif "change to home directory"in text:
		path = "/"
	elif "change to root directory"in text:
		path = "~"
	elif "what is the date today"in text:
		string0 = "date"
		b_string1 = string0.encode('utf-8')
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)
	elif "what is the day today"in text:
		string0 = "date +%A"
		b_string1 = string0.encode('utf-8')
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)
	elif "what time is it"in text:
		string0 = "date +%T"
		b_string1 = string0.encode('utf-8')
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)
	elif "show calendar"in text:
		string0 = "cal"
		b_string1 = string0.encode('utf-8')
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)
	elif "who am i"in text:
		string0 = "whoami"
		b_string1 = string0.encode('utf-8')
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)
	elif "add user" in text:
		speak("Tell the user name",engine)
		
	elif "exit" in text:
		exit()
	
	return path	

        

        



