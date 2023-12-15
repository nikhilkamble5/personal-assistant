import pyttsx3  #  text to speech
import pywhatkit #r sending messages automatically to someone's WhatsApp mobile number.
import speech_recognition as sr  # speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import ctypes # Since this library handles compiled code, it is relatively OS dependent.
import sys #provides information about constants, functions and methods of the Python interpreter
import subprocess #allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return code

import os

engine = pyttsx3.init('sapi5') #API produced by Microsoft for speech recognition and speech synthesis.
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir, !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir,!")

    else:
        speak("Good Evening sir,!")

    speak("I am sparta sir,your personal assistant, I am online,Please tell me how may I help you.")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":

    wishMe()

    while True:

        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)






        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open notepad' in query:
            os.system("start notepad")
        elif 'close notepad' in query:
            os.system('taskkill /f /im notepad.exe')








        elif 'open google' in query:
            speak('sir, what should i search on google')
            chandu = takeCommand().lower()
            webbrowser.open(f"{chandu}")
        elif 'open my photos' in query:
            os.startfile("D:\\myphotos")
        elif 'sparta i feel very bored' in query:
            speak('how can i entertain you sir')
        elif 'well i want to watch movies' in query:
            speak('ok sir,')


        elif 'please open movies' in query:
            speak('your movies collection, enjoy sir')
            os.startfile("F:\\entertainment\\Movies")
        elif 'please change my desktop background' in query:
            speak('are you sure sir')
        elif 'yes' in query:
            speak('your desktop background change sir')
            WALLPAPER_PATH = "C:\\Users\\Administrator\\Desktop\wall\\68485.jpg"
            ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)


        elif 'lock my device' in query:
            speak('sir, device is lock, but for unlock you have to enter correct password.')
            cmd = 'rundll32.exe user32.dll, LockWorkStation'
            subprocess.call(cmd)
        elif 'what is my password' in query:
            speak('sorry sir, i cannot tell ,it is  a protocol, that you told me sir.')
        elif 'good sparta' in query:
            speak('thank you sir')


        elif "please log off my device" in query:
            speak("are u sure sir?")












        elif 'play song on youtube' in query:
            pywhatkit.playonyt('kaise hua')
        elif 'play movie on youtube' in query:
            pywhatkit.playonyt('awarapan')
        elif 'i want to watch movie on youtube' in query:
            speak('ok sir')











        elif 'open cisco packet tracer' in query:
            path = "C:\\Program Files (x86)\\Cisco Packet Tracer 6.2sv\\bin\\PacketTracer6.exe"
            os.startfile(path)

        elif 'open netbeans' in query:
            path = "C:\\Program Files\\NetBeans 8.0.2\\bin\\netbeans64.exe"
            os.startfile(path)

        elif 'open teamviewer' in query:
            # path="C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"
            os.startfile("C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe")

        elif 'make folder in d drive' in query:
            speak('please tell me the name of folder')
        elif 'student' in query:
            speak('your folder is ready in d drive')
            path = "D:/student"
            os.mkdir(path)
        elif 'thank you' in query:
            speak('its my pleasure sir,any other work sir for me')
        elif 'no sparta' in query:
            speak('ok sir.have a good day')



        elif 'play music' in query:
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play my favourite movie' in query:
            music_dir = 'D:\movie'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")




        elif 'hello sparta' in query:
            speak('hello  sir,may i help you with something.')

        elif 'how are you sparta' in query:
            speak('i am fine sir,what about you.')
        elif 'also good' in query:
            speak("that's great to hear from you.")






        elif 'thank you sparta' in query:
            speak("it's my pleasure sir.")




        elif 'no thanks' in query:
            speak('thank you sir for using me,have a good day.')

            sys.exit()




































