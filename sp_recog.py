import speech_recognition as sr


def main():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Say Something..")

        audio=r.listen(source)

        print("Recongnizing Now...")

        try:
            person_speech = r.recognize_google(audio)
            print("you have said: \n"+ person_speech)

        except Exception as e:
            print("Error: "+ str(e))    


main()            