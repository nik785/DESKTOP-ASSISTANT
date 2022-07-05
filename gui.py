
from email.mime import audio
from importlib import import_module
from tkinter import BOTTOM, Tk, mainloop, TOP
from tkinter.ttk import Button
from numpy import true_divide
import pyttsx3
import wikipedia
import os
import datetime
import speech_recognition as sr
from playsound import playsound
import webbrowser
import pyjokes
import pywhatkit as kit
import sys





sir="NIKHIL"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 145)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!"+sir)

    elif hour>=12 and hour<18:
        speak("good afternoon!"+sir)

    else:
        speak("good evening"+sir)


def takecommand():
        r = sr.Recognizer()

        with sr.Microphone() as audio:

            speak('Listening...')
            r.pause_threshold = 1
            voice = r.listen(audio,timeout=3,phrase_time_limit=8)
        try:
            print("Thinking...")
            query = r.recognize_google(voice,language='en-in')
            print("Transcription:"+query) 

        except Exception as e:
            print("I am Sorry There is an error while i am recognizimg your command")
            return "none"

        return query



class widget:
    def __init__(self):
        # creating tkinter window
        root = Tk()

        # creating fixed geometry of the
        # tkinter window with dimensions 150x200
        root.geometry('500x150+400+300')

        # Create Button and add some text
        button1 = Button(root, text = 'SPEAK', command=self.clicked)
        button1.pack(side = TOP, pady = 5)


        # Execute Tkinter
        root.mainloop()



    def clicked(self):

        while True:

            print("listening")
            query=takecommand()
            query=query.lower()



            if 'open youtube' in query:
                speak("opening youtube")
                webbrowser.open("www.youtube.com")

            if "open notepad" in query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open cmd" in query:
                npath = "C:\\Windows\\system32\\cmd.exe"
                os.startfile(npath)

            elif "open paint" in query:
                npath = "C:\\Windows\\system32\\mspaint.exe"
                os.startfile(npath)
            

    #########################################################################

            elif "wikipedia" in query:
                speak("speaking wikipedia....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak(results)
                # print(results)

    #################################################################

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
            
            elif "open gmail" in query:
                webbrowser.open("www.gmail.com")
            
            elif "open amazon" in query:
                webbrowser.open("www.amazon.com")

            elif "open facebook" in query:
                webbrowser.open("www.facebook.com")

    ###################################################################################
        
            elif "open google" in query:
                speak("sir, what do you want me to search on google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")

    ##############################################################################

            elif "send message" in query:
                kit.sendwhatmsg("+919992432188", "this is hero",2,2)

    ###################################################################
            
            elif "search on youtube" in query:
                speak("sir, what you should i search on youtube")
                gm = takecommand().lower()
                kit.playonyt(f"{gm}")

    ###############################################################


            elif "what is my name" in query:
                speak("your name is nikhil.")

            elif "what is my hobbie" in query:
                speak("your hobbie is football,sir.")

            elif "who is my girlfriend" in query:
                speak("you are the most eligible bachelor.")

            elif "who is erica" in query:
                speak("erica is baboy")


    #########################################################################################      

    # for closing notepad
            elif "close notepad" in query:
                speak("okey sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "close cmd" in query:
                speak("okey sir, closing cmd")
                os.system("taskkill /f /im cmd.exe")


    ############################################################################

    # to find a joke
            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)

    ####################################################

            elif "shut down the system" in query:
                os.system("shutdown /s /t s")

    ########################################################

            elif "restart the system" in query:
                os.system("shutdown /r /t s")

    #######################################################

            elif "sleep the system" in query:
                os.system("rundll32.exe powerprof.dil,SetSuspendState 0,1,0")


    ###############################################################################

            elif "stop" in query:
                    speak("thanks for using me, sir, have a good day")

                    sys.exit()
            speak("what r u thinking, sir ?")


if __name__=='__main__':
    speak('Erica is starting')
    wishme()
    widget=widget()
    