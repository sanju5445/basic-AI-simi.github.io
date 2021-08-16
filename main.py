import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
# import cv
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<14:
       speak("good morning ")
    elif hour>=14 and hour<18:
       speak("good afternoon")
    elif hour>=18 and hour<20:
       speak("good evening ")
    else:
      speak("good night sir")

    speak("hello sir,i am simi , i am here to help you, please tell me how may i help you")
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening.....")
      r.energy_threshold=80
      r.pause_threshold = 1
      audio = r.listen(source)

    try:
        query= r.recognize_google(audio)
        print("you said:")
        print(format(query))
    except:
        print("say again please:")
        return "None"
    return query






if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()


        if 'wikipedia' in query:
            print("searching wikipedia....")
            speak("searching wikipedia.... please wait a second")
            query = query.replace("wikipedia",  "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("yeah sure sir,wait a second")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("yeah sure sir,wait a second")
            webbrowser.open("google.com")

        elif 'open notepad' in query:
            speak("yeah sure sir,wait a second")
            npath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"
            os.startfile(npath)

        elif 'open cmd' in query:
            speak("yeah sure sir,wait a second")
            os.system("start cmd")

        # elif 'open camera' in query:
        #     speak("yeah sure sir, wait a second")
        #     cap=cv.VideoCapture(0)
        #     while True:
        #         ret, img =cap.read()
        #         cv.imshow('webcam', img)
        #         k=cv.waitKey(58)
        #         if k==27:
        #             break;
        #     cap.release()
        #     cv.destroyAllWindows()


    #playing music
        elif 'play music' in query:
            speak("yeah sure sir,wait a second")
            speak("which one you want to listen ")
            music_dir ="C:\song"
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))








      #for personal information
        elif 'how are' in query:
            speak("i'm fine sir, what about you?")


        elif 'hello' in query:
            speak("hello sir, how may i help you")

        elif 'can i say' in query:
            speak("yeah, sure sir you can say anything")

        elif 'who are you' in query:
            speak("sir, i'm simi , i'm your personal assistant, who are always here to help you ")

        elif 'invent' in query:
            speak("sir you the person who invent me, on second february in 2021")

        elif 'love you' in query:
            speak("love you too sir, forever and ever and ever")

        elif 'thank you' in query:
            speak("most welcome sir")

        elif 'go to sleep' in query:
            speak("okk sir i'm going to sleep, you have a good day")
            exit(0)


        elif 'minute' in query:
            speak("why sir? where are you going?")

        elif 'going to' in query:
            speak("please don't smoke sir, smoking is injurious to our health ")
            speak("if you smoke i'll call your mother")

















        elif 'temperature' in query:
            search ="temperature in arambagh"
            url =f"https://www.google.com/search? q={search}"
            r= requests.get(url)
            data= BeautifulSoup(r.text,"html.parser")
            temp= data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
