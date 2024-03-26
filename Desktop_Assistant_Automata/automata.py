# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 12:42:58 2023

@author: sayan
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from sys import exit
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("I am Automata. How may I serve you sir?")

def takeCommand():
    # It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query} \n")
    
    except Exception as e:
        # print(e)
        print("Say that again please!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sayandip32076@gmail.com','Your-Password')
    server.sendEmail('sayandip32076@gmail.com',to, content)
    server.close()
    

if __name__ == "__main__":
    speak("today is good weather")
    wishMe()
    
    while True:
        query = takeCommand().lower()
    
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            # os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the Time is {strTime}")
        elif 'open code' in query:
            code_path = "D:\\Core_Java_Files\\IntelliJ IDEA Community Edition 2022.3.1\\bin\\idea64.exe"
            os.startfile(code_path)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sayandip2016paul@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry the email cannot be sent at the moment")
        elif 'quit' in query:
            exit()
            
            

        
            
        
    
    




