import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import  os, sys, subprocess
import random
import smtplib
engine =pyttsx3.init('espeak')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[25].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir please wake up")

    elif hour>=12 and hour<16:
        speak("Good Afternoon sir")
    elif hour>=16 and hour<18:
        speak("Good evening Sir")
    else:
        speak("Good night Sir")

    speak("I am Aakash Sir. Please tell me how may I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing.....")
            query =r.recognize_google(audio, language='en-in')
            print(f"User said : {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again Please.....")
            return ("None")
        return query

def sendEmail(to, content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('your email id','your password')
     server.sendmail('sender email id', to, content)
     server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query= takeCommand().lower()
        if 'how are you' in query:
            speak('I am good sir.....')
        if 'what are you doing' in query:
            speak('Nothing sir i m doing my work.....')
        if 'love your work' in query:
            speak('Thankyou sir .....')

        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = '/home/akash/ColdPlay'
            songs = os.listdir(music_dir)
            ch=random.randint(0, len(songs))

            ganna=os.path.join(music_dir, songs[ch])
            import vlc
            player=vlc.MediaPlayer(ganna)
            player.play()
        elif 'stop music' in query:
            player.stop()
        elif 'pause music' in query:
            player.pause()
        elif 'change music' in query:
             player.stop()
             ch=random.randint(0, len(songs))

             ganna=os.path.join(music_dir, songs[ch])
             player=vlc.MediaPlayer(ganna)
             player.play()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is { strTime }")
        elif 'send a mail' in query:
            try:
                speak("what should I say ?")
                content = takeCommand()
                to = "sender email id"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! sir email has not sent!")
