import speech_recognition as sr
import ctypes
import time
## Build Command - cc -fPIC -shared -o functions.so functions.c ##

so_file = "/home/masads/Voice-Controlled-Shell/functions.so"
my_functions = ctypes.CDLL(so_file)

my_functions.checkFile.restype  = ctypes.c_char_p


def listen(engine):
	
	r=sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		person_speech = "~"

		print("\nSay Something..")
        
		audio=r.listen(source)
		time.sleep(1)
		print("Recongnizing Now...")
		try:
			person_speech = r.recognize_google(audio)
			print("You: " + person_speech)
		except Exception as e:
			print("Bot: I did not understand what you said.. say again")
			speak("I did not understand what you said say again",engine)
		
		if "~" in person_speech:
			return listen(engine)
		else:
			return person_speech

def speak(speech, engine):
    
    engine.say(speech)
    engine.runAndWait()
    
def proccess_text(path, text,engine):

	if "change directory" in text:
		print("Which directory you want to go to?")
		speak("Which directory you want to go to?",engine)
		string1 = listen(engine)
		print(string1)
		b_string1 = string1.encode('utf-8')
		b_path = path.encode('utf-8')
		my_functions.checkFile.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
		string2 = my_functions.checkFile(b_string1,b_path).decode()
		print(string2)
		if " " in string2:
			print("Folder does not exists")
		else:
			path=path+"/"+string2
		print("Successfully navigated to :"+path)
		

	elif "list all file" in text:
		command = ";ls"
		string1 = "cd " + path + command
		b_string1 = string1.encode('utf-8')
		print("Listing all the files in the current directory...")
		speak("Listing all the files in the current directory", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "create a new file" in text: 
		speak("Tell the file name",engine)
		string0 = listen(engine)
		speak("Please enter the file extension",engine)
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
			print(string0 + " File Created Successfully...")
			speak(string0 + " File Created Successfully", engine)
		else:
			print(fileNexist + " File already exists")

	elif "delete a file" in text: 	
		speak("Tell the file name",engine)
		string0 = listen(engine)
		speak("Tell the file extension",engine)
		ext = input()
		string0 = string0 + "." + ext
		b_string0 = string0.encode('utf-8')
		b_path = path.encode('utf-8')
		my_functions.checkFile.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
		fileNexist = my_functions.checkFile(b_string0,b_path).decode()
		if " " in fileNexist:
			print(string0 + " file not exist")
		else:
			string1 = "cd " + path + ";rm -r " + fileNexist
			b_string1 = string1.encode('utf-8')
			my_functions.run_command.argtypes = [ctypes.c_char_p]
			my_functions.run_command(b_string1)
			print(fileNexist + " File Removed Successfully")
			speak("File Removed Successfully",engine)

	elif "open nano editor" in text:
		speak("Tell the file name",engine)
		string0 = listen(engine)
		string1 = "cd " + path + ";nano " + string0 + ".*"
		b_string1 = string1.encode('utf-8')
		print("Opening geditor...")
		speak("Opening geditor",engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "open g editor" in text:
		speak("Tell the file name",engine)
		string0 = listen(engine)
		string1 = "cd " + path + ";gedit " + string0 + ".*"
		b_string1 = string1.encode('utf-8')
		print("Opening geditor...")
		speak("Opening geditor",engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "make directory" in text: 
		speak("Tell the file name",engine)
		string0 = listen(engine)
		b_string0 = string0.encode('utf-8')
		b_path = path.encode('utf-8')
		my_functions.checkFile.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
		fileNexist = my_functions.checkFile(b_string0,b_path).decode()
		if " " in fileNexist:
			string1 = "cd " + path + ";mkdir " + string0
			b_string1 = string1.encode('utf-8')
			my_functions.run_command.argtypes = [ctypes.c_char_p]
			my_functions.run_command(b_string1)
			print("New Directory Created Successfully...")
			speak("New Directory Created Successfully",engine)
		else:
			print(fileNexist + " Folder already exists")

	elif "show all users" in text:
		string0 = "ls /home"
		b_string1 = string0.encode('utf-8')
		print("Listing all the users...")
		speak("Listing all the users",engine)
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "shutdown" in text:
		string0 = "shutdown -h now"
		b_string1 = string0.encode('utf-8')
		speak("Shutting down the PC",engine)
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "navigate to home directory"in text:
		path = "/home/masads"
		speak("Navigated to Home Directory",engine)

	elif "navigate to root directory"in text:
		path = "~"
		speak("Navigated to Root Directory",engine)

	elif "show date"in text:
		string0 = "date"
		b_string1 = string0.encode('utf-8')
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "what day is it"in text:
		string0 = "date +%A"
		b_string1 = string0.encode('utf-8')
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "show time"in text:
		string0 = "date +%T"
		b_string1 = string0.encode('utf-8')
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "show calendar"in text:
		print("Showing you the calender for the current month...")
		speak("Showing you the calender for the current month",engine)
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
		string0 = listen(engine)
		tpath = "/home"
		b_string0 = string0.encode('utf-8')
		b_path = tpath.encode('utf-8')
		my_functions.checkFile.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
		fileNexist = my_functions.checkFile(b_string0,b_path).decode()
		if " " in fileNexist:
			string1 = "sudo adduser " + string0.lower()
			b_string1 = string1.encode('utf-8')
			my_functions.run_command.argtypes = [ctypes.c_char_p]
			my_functions.run_command(b_string1)
			print("User Added Successfully...")
			speak("New User Added Successfully", engine)
		else:
			print(fileNexist + " User already exist")

	elif "delete user profile" in text:
		speak("Tell the user name",engine)
		string0 = listen(engine)
		tpath = "/home"
		b_string0 = string0.encode('utf-8')
		b_path = tpath.encode('utf-8')
		my_functions.checkFile.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
		fileNexist = my_functions.checkFile(b_string0,b_path).decode()
		if " " in fileNexist:
			print(string0 + " User does not exists")
		else:
			string1 = "sudo userdel " + fileNexist
			b_string1 = string1.encode('utf-8')
			my_functions.run_command.argtypes = [ctypes.c_char_p]
			my_functions.run_command(b_string1)
			print("User Removed Successfully...")
			speak("Successfully removed the User",engine)

	elif "permanently delete user" in text:
		speak("Tell the user name",engine)
		string0 = listen(engine)
		tpath = "/home"
		b_string0 = string0.encode('utf-8')
		b_path = tpath.encode('utf-8')
		my_functions.checkFile.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
		fileNexist = my_functions.checkFile(b_string0,b_path).decode()
		if " " in fileNexist:
			print(string0 + " user not exist")
		else:
			string1 = "sudo deluser --remove-home " + fileNexist
			b_string1 = string1.encode('utf-8')
			my_functions.run_command.argtypes = [ctypes.c_char_p]
			my_functions.run_command(b_string1)
			print("User Removed Successfully...")
			speak("Successfully removed the User",engine)

	elif "show file permission" in text:
		command = ";ls -l"
		string1 = "cd " + path + command
		b_string1 = string1.encode('utf-8')
		print("Listing all the the files with their permissions...")
		speak("Listing all the the files with their permissions", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "list  hidden file" in text:
		command = ";ls -a"
		string1 = "cd " + path + command
		b_string1 = string1.encode('utf-8')
		print("Listing all the hidden files...")
		speak("Listing all the hidden files", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "current working directory" in text:
		command = ";pwd"
		string1 = "cd " + path + command
		b_string1 = string1.encode('utf-8')
		print("Your current working directory is: " + path)
		speak("Your current working directory is " + path, engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "show network status" in text:
		string1 = "sudo lshw -class network"
		b_string1 = string1.encode('utf-8')
		print("Showing you the current network status...")
		speak("Showing you the current network status", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "take snapshot" in text:
		string1 = "gnome-screenshot"
		b_string1 = string1.encode('utf-8')
		print("Taking a snapshot rightnow...")
		speak("Taking a snapshot rightnow", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "show all active connection" in text:
		string1 = "netstat"
		b_string1 = string1.encode('utf-8')
		print("Showing you all the active connections...")
		speak("Showing you all the active connections", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "history of command" in text:#error
		string1 = "cat ~/.bash_history"
		b_string1 = string1.encode('utf-8')
		print("Showing you all the commands that were executed previously...")
		speak("Showing you all the commands that were executed previously", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "clear the screen" in text:
		string1 = "clear"
		b_string1 = string1.encode('utf-8')
		print("Clearing the console...")
		speak("Clearing the console", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "gain root access" in text:
		string1 = "sudo su"
		b_string1 = string1.encode('utf-8')
		print("giving you the root access...")
		speak("giving you the root access", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "change user password" in text:
		string1 = "sudo passwd"
		b_string1 = string1.encode('utf-8')
		print("Changing the password...")
		speak("Changing the password", engine)
		my_functions.run_command.argtypes = [ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "reboot" in text:
		string0 = "sudo reboot"
		b_string1 = string0.encode('utf-8')
		print("Rebooting the system...")
		speak("Rebooting the system", engine)
		my_functions.run_command.argtypes=[ctypes.c_char_p]
		my_functions.run_command(b_string1)

	elif "exit" in text:
		print("Exiting the Program...")
		speak("Exiting the Program",engine)
		exit()
	else:
		print("command not found")
		speak("command not found",engine)
	
	return path	

       

        



