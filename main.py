import random
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from requests import get
import pywhatkit as kit
import cv2
import sys
import requests
import pyautogui
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)--> yeh voice male ya female ki h pata krne k liye
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=16:
        speak("Good Afternoon!")

    else :
        speak("Good Evening!")


    speak("Hello Sir I am Jarvis. How may I Help You")


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=b3d25bcbcbf04bba9cb0ff38fbdf70f7'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head =[]
    day = ["first","second","third","fourth","fifth"]
    for a in articles:
        head.append(a["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]}news is : {head[i]}")

def takeCommand():
    # takes micrphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e) --> error print na karane ke liye comment out kara h
        print("Please,Repeat it Again")
        return "None"

    return query






if __name__ == "__main__":

    # speak("harshit is a good boy") --> yeh cheez speak karega speak ko call karke
    wishme()
    while True:
        query= takeCommand().lower()

        #logic for executing task based on query
        if 'wikipedia' in query:
            speak ('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print (results)
            speak(results)

        elif 'open google' in query:
            speak("Sir,What should i search in google")
            c = takeCommand().lower()
            webbrowser.open(f"{c}")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music = 'C:\\Program Files\\Python312\\Music'
            songs=os.listdir(music)
           # print(songs)
            
            s = random.choice(songs)
            os.startfile(os.path.join(music,s))

        elif 'the time' in query:
            C_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {C_time}")

        elif 'open vs code' in query:
            CPath = "C:\\Users\Manoj Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(CPath)

        elif 'open notepad' in query:
            nPath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"
            os.startfile(nPath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your Ip address is {ip}")
            print(ip)


        elif 'open camera' in query:
            capture=cv2.VideoCapture(0)
            while True:
                ret,img = capture.read()
                cv2.imshow('webcam',img)
                k =cv2.waitkey(50)
                if k==27:
                    break
            capture.release()
            cv2.destroyAllWindows()


        #elif 'send message' in query:
           # kit.sendwhatmsg("phone number","this a test message",2 min baad ka time commas seperated)

        elif 'play song on youtube' in query:
            kit.playonyt("laado")

            #aur bhi bohot saare kar skte h hum aise karke

        elif 'no thanks' in query:
            speak("Thanks for using me sir, have anice day")
            sys.exit()
            

       # elif 'set alarm' in query:
         #   nn = int(datetime.datetime.now().hour)
          #  if nn==22:
            #     music = 'C:\\Program Files\\Python312\\Music'
             #    songs=os.listdir(music)
            #     os.startfile(os.path.join(music,songs[1]))

        elif 'tell me news' in query:
            speak("please wait sir, fetching the latest news")
            news()


        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

       # elif 'where i am ' in query or 'where we are' in query:
          #  speak("wait sir, let me check")
          #  try:
           #     ip= requests.get('https://api.ipify.org').text
           #     print(ip)
           #     url ='https://get.geojs.io/v1/ip/geo/'+ip+'.json'
           #     geo_requests = requests.get(url)
           #     geo_data = geo_requests.json()
           #     city = geo_data['city']
            #    country = geo_data['country']
            #    speak(f"sir i am not sure , but i think we are in {city} city of {country} country")

           # except Exception as e:
           #     speak("sorry sir, due to network issue i am not able to find where we are")
            #    pass    

        


        speak("Sir, do you have any other work")


        




        


 

        
  
