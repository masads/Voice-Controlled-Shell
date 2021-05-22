from modules import *
import pyttsx3

engine = pyttsx3.init()
path = "~"

if __name__ == '__main__':
    path = "/home/masads"
    speak("hello how can i help you?",engine)
    while(1):
        text = input()
        path = proccess_text(path, text,engine)

exit()


