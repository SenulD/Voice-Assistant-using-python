"""
                            Simple Voice assistant using Python.

"""
# Import all the libraries and files 
from typing import Mapping
from favouritemusics import *
import pyttsx3  
import speech_recognition as sr  
import webbrowser
import datetime
import pywhatkit 
import os
import yfinance as yf
import pyjokes 
import pyaudio
import wikipedia 
import vlc
import time
import random

a = 0 
# Listen to My microphone and return the audio as text using google.

def transform():                                            #Takt to assitent, checking for error, print and give the text that user talked!
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print("I am listning")
            q = r. recognize_google(said, language="en")
            print(q)
            return(q)
        except sr.UnknownValueError:
            print("Sorry, I did not understand")
            return "I am waiting.."
        except sr.RequestError:
            print("Sorry, the service is down")
            return "I am waiting.."
        except:
            return "I am waiting.."


def speaking(message):                                  #Speaking part
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

#speaking("hello world")                                [testing perposes]

engine = pyttsx3.init()


#    print(voice)             #print all available languvages or voices in my machine           [testing perposes]

#make the voice
id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engine.setProperty('voice',id)



#Return the weekday name
def query_day ():
    day = datetime.date.today()
    #print(day)                                 # this will print day and week number..         [testing perposes]
    weekday = day.weekday()
    print(weekday)
    mapping = {
        0:"Monday" ,1:"Tuesday" ,2:"Wednesday" ,3:"Thursday" ,4:"Friday ",5:"Saturday",6:"Sunday" 
    }
    try:
        speaking(f'Today is{mapping[weekday]}')
    except:
        pass

def telldate ():
    day = datetime.date.today()
    speaking(f'Date is {day}')


#retuen the time!
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"{time[1:2]} o'clock and {time[3:5]} minutes")


#iNTRO GREETING AT START UP
def whatsup():
    speaking('''Hi, I am David. your personal VA
    How may I help you
    ''')
#                                                       Comannds and their functions
#Os settings
def shutdown():
    return os.system("shutdown /s /t 1")
 
def restart():
    return os.system("shutdown /r /t 1")
 
def logout():
    return os.system("shutdown -l")

# play favourite songs
def playsongs():
    for i in range(0,134):
    
        p = vlc.MediaPlayer(songs[i])
                                              
        p.play()

        print('is_playing:', p.is_playing())    

        time.sleep(0.5)                          # sleep. it need some time to start 

        print('is_playing:', p.is_playing())    

        while p.is_playing():
            time.sleep(0.5)                        # sleep 

    

#The heart of our assistant. Takes quries and return answers.
def querying():
    whatsup()
    print("starting..")
    start = True
    while(start):
        q = transform().lower()
     #part in web browser
        if "start youtube" in q:
            speaking("Starting youtube Just a second.")
            webbrowser.open("https://www.youtube.com")
            continue
        
        elif "start browser" in q:
            speaking("Opening browser")
            webbrowser.open("https://www.google.com")
            continue

        elif "open opera" in q:
            speaking("Opening opera")
            webbrowser.open("https://www.opera.com")
            continue
#  ptwhatkit
        elif"search web" in q:
            speaking("checking on net")
            q = q.replace("find","")
            pywhatkit.search(q)
            speaking("That is what i found!")
            continue


        elif "play" in q:
            speaking(f"playing{q}")
            pywhatkit.playonyt(q)
            continue

# date time part
        elif ("what day is it"or "what day") in q:
             query_day()
             continue
        
        elif ("date" or "what date is it") in q:
             speaking("are you sure sir?")
             telldate()
             continue
                       
        elif ("what time is it" or "what time") in q:
            query_time()
            continue
             
# personal questions

        elif "are you still there?" in q:
            speaking("Yes sir")
            continue

        elif ("test" or "test one two") in q:
            speaking("I acn here you clearly!")
            continue

        elif "your name" in q:
            speaking("I am David. Your VA")
            continue

        elif "how are you" in q:
            speaking("I'm good Sir, how about you?")
            continue

        elif ("fine" or"good") in q:
            speaking("Nice to here that!")
            continue
        
        elif ("david") in q:
            speaking("yes sir")
            continue

        elif "shut up" in q:
            speaking("are you sure")
            q = transform().lower()
            if "yes" in q :
                speaking("OK,I am shutting down")
                break 
            

# wikipedia
        elif "from wikipedia" in q:
            speaking("checking wikipedia")
            q = q.replace("wikipedia","")
            result = wikipedia.summary(q,sentences = 3)
            speaking("found on wikipedia")
            speaking(result)
            continue

# jokes
        elif "joke" in q:
            speaking(pyjokes.get_joke())
            continue

#yfinance stock pricecs

        elif "stock price" in q:
            search = q.split("of")[-1].strip()
            lookup = {"apple":"AAPL",
                    "amazon":"AMZN",
                    "google":"GOOGL"}
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketprince"]
                speaking(f'found it, the price for{search} is {currentprice}')
                continue
            except:
                speaking(f"Sorry i have no data for{search}")
                continue

# os options
        elif "shut down my computer" in q:
            speaking("Sir, are you suer? It's a primary command!")
            q = transform().lower()
            if "yes" in q :
                speaking("wait a second. Shutig down the computer")
                shutdown()
                continue
            
                 
        elif "Log out my account" in q:
            speaking("Are you Sure.Unsaved data will lost!")
            q = transform().lower()
            if "yes" in q:
                speaking("wait a second. logging out from your account")
                logout()
                continue
            elif "No" in q:
                speaking("ok")
                continue
            

        elif ("sleep computer" or "Sleep my computer") in q:
            speaking("wait a second. going to sleepig mode")
            
            continue

        elif ("play a song" or "play my songs") in q :
            speaking("playing your favourite song list")
            random.shuffle(songs)
            playsongs()
            continue

        
querying()