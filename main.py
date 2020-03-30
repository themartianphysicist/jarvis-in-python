import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"Command: {query}\n")

    except:
        print("I couldn't get it, please repeat again")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kartikayemars@gmail.com', 'martianphysics')
    content.capitalize()
    server.sendmail('kartikayemars@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    run = True
    while run:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open netflix' in query:
            webbrowser.open("www.netflix.com")

        elif 'open prime video' in query:
            webbrowser.open("www.primevideo.com")

        elif 'open brilliant' in query:
            webbrowser.open("www.brilliant.org")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\Kartikaye\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'exit' in query:
            engine.setProperty('rate', 143)

            speak("Goodbye, Kartikaye")
            run = False

        elif 'online clas' in query: 
            webbrowser.open("https://code.whitehatjr.com/s/dashboard")


        elif 'send email to father' or 'send mail to father' in query:
            speak("Sending Email ...")
            print("Sending Email ...")
                
            try:
                speak("What should I send?") 
                content = takeCommand()
                content.capitalize()
                to = "rishidmrc@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!!")
            except:
                speak("four o four could not send")

        elif 'send email to sister' or 'send mail to sister' in query:
            speak("Sending Email ...")
            print("Sending Email ...")
                
            try:
                speak("What should I send?") 
                content = takeCommand()
                content.capitalize()
                to = "solasticanr@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!!!")
            except:
                speak("four o four could not send")

        elif 'send email to mother' or 'send mail to mother' in query:

            speak("Sending Email ...")
            print("Sending Email ...")
                
                
            try:
                speak("What should I send?") 
                content = takeCommand()
                content.capitalize()
                to = "solasticanr@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!!!")
            except:
                speak("four o four could not send")
                

            
                

        elif 'name' and 'what is' in query:
            speak("My name is Alexa")

        elif 'how old are you' or 'what is your age' or 'years old are you' or 'when is your birthday' in query:
            speak("I was born on March 30 two thousand and twenty")

        
        
