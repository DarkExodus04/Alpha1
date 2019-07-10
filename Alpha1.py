import pyttsx3
import speech_recognition as sr
import datetime
from googlesearch import search
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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

    speak("I am Alpha.Can i be of any help to you?")

def takeCommand():
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
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('one.alpha1jarvis@gmail.com', 'Alpha12345')
    server.sendmail('one.alpha1jarvis@gmail.com', to, content)
    server.close()

def googlesearch() :
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
        webbrowser.open("https://google.com/search?q=%s" % query)
        
        
if __name__ == "__main__": 
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'send email' in query:
            try:
                speak("Please type the Email address of the receiver.")
                to = input('Email : ')
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("I have sent your Email.")
            except Exception as e:
                print(e)
                speak("Sorry, Could not send this email.")


        elif query:
            googlesearch()


