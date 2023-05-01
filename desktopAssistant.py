import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import ctypes
from ecapture import ecapture as ec
import subprocess
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am ela. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language = "en-in")
        print(query)
    except Exception as e:
        speak("sorry sir i did not got that")
        print(e)
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('vaishnaviwani18@gmail.com', 'Vwani@2004')
    server.sendmail('vaishnaviwani18@gmail.com', to, content)
    server.close()


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

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.org") 
        elif 'who are you'in query:
            speak("i'm Ela. Your desktop voice assistant") 

        elif 'play music' in query:
            music_dir = 'song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = r"C:\Users\admin\Desktop\python project\assistant.py"
            os.startfile(codePath)
        elif  'bye' in query or 'stop' in query:
             hour = int(datetime.datetime.now().hour)
             if hour >= 21 and hour < 6:
                speak("Good night, take care!")
             else:
                speak('Have a good day !,')
             exit()
        elif 'plot' in query:
            with open('assistant.py') as f:
             code = compile(f.read(), 'assistant.py', 'exec')
             exec(code)
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")