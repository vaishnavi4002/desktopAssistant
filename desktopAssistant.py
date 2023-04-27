import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


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
    server.login('vaishnaviwani18@gmail.com', 'Vwani2004')
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
                speak("Good night sir, take care!")
             else:
                speak('Have a good day sir!,')
             exit()
        elif 'plot' in query:
            with open('assistant.py') as f:
             code = compile(f.read(), 'assistant.py', 'exec')
             exec(code)
            
        '''elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gmail@viit.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")'''