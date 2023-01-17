import time
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import googletrans
from kivy.config import Config
from kivy.app import App as a
from kivy.uix.button import Button as b
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2


class WindowManager(ScreenManager):
	pass

engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

class FirstWindow(Screen,Widget):
  
    def scr(self,screen):
        self.ids.f.current=screen
        self.ids.f.trigger_action(0.2)
    def textt(self,call):
        self.leb.text=str(call)
        self.ids.mic1.source='mic2.png'

    def off(self):
        self.ids.mic1.source='mic2.png'


    def speak(self,audio):
        self.leb.text=self.leb.text+"\n \n"+str(audio)
        print(audio)
        engine.say(audio)
        engine.runAndWait()


    def wishme(self):
        hour = int(datetime.datetime.now().hour)
        self.speak("hello sir ")    
        if hour>=0 and hour<12:
            self.speak("Good Morning!")
        elif hour>=12 and hour<18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evining!")         
        self.speak("i am friday, how may i help you?")        


    def listen(self):
        k = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("Listening....")
            k.pause_threshold == 100
            audio=k.listen(source)
        try:
            self.speak("Recognizing......")
            query=k.recognize_google(audio, language='eng-in')    
            print("user said: ",{query},"\n")
        except Exception as e:
            # print("Say that again please....")
            self.speak("Say that again please....")
            return "None"
        self.ids.mic1.source='mic1.png'
        self.exe(query)



    def sendEmail(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('amolbrand00@gmail.com','amol@1234#')
        server.sendmail('amolbrand00@gmail.com',to,content)
        server.close()
        
    def exe(self,query):
        if 'wikipedia' in query:
                    try:
                        self.speak('searching Wikipedia....')
                        query= query.replace("wikipedia","")
                        results = wikipedia.summary(query,sentences=1)
                        self.speak("Acording To Wikipedia")
                        self.speak(results)
                    except Exception as e:
                        print(e)
                        self.speak("sorry boss ,i am not able get any appropriate result from wikipedia")
        elif 'search' in query:
                    try:
                        query= query.replace("search","")
                        webbrowser.open('https://www.google.com/search?client=firefox-b-lm&q='+query)
                    except Exception as e:
                        print(e)
                        self.speak("Sorry i am not able to search")
        #=======================================================================================
        #  Queries for screen manager
        
        elif 'next' in query:
            self.ids.f.trigger_action(0.2)
        elif 'third' in query:
            self.ids.t.trigger_action(0.2)
        elif 'calculator' in query:
            self.ids.fo.trigger_action(0.2)
        elif 'fifth' in query:
            self.ids.fi.trigger_action(0.2)
        elif 'sixth' in query:
            self.ids.s.trigger_action(0.2)
        #=======================================================================================
        
        #=======================================================================================
        #  os or file manupulation commands
        elif 'file' in query:
            open='C:\\'
            os.startfile(open)

        elif 'chrome' in query:
            open='"C:\\Users\\Public\\Desktop\\Google Chrome.lnk"'
            os.startfile(open)    

        elif 'firefox' in query:
            open='C:\\Program Files\\Mozilla Firefox\\firefox.exe'
            os.startfile(open)    
        elif 'code' in query:
            open='C:\\Users\\Amol\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(open)            

        elif 'camera' in query:
            cap = cv2.VideoCapture(0)
            while(cap.isOpened()):
                
                while True:
                    
                    ret, img = cap.read()
                    cv2.imshow('img', img)
                    if cv2.waitKey(30) & 0xff == ord('q'):
                        break
                        
                cap.release()
                cv2.destroyAllWindows()
            else:
                print("Alert ! Camera disconnected")

        elif 'ISS' in query:
            os.startfile('iss.py')
        
        elif 'time' in query:
                    strtime= datetime.datetime.now().strftime("%H:%M:%S")
                    self.speak(f"The time is {strtime}")
        elif 'youtube' in query:
                    self.speak('starting')
                    time.sleep(3)
                    webbrowser.open('https://youtu.be/iik25wqIuFo')
        elif 'VLC' in query:
            open="C:\\Users\\Public\\Desktop\\VLC media player.lnk"
            os.startfile(open)

        elif 'panel' in query:
            open="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(open)                    

        elif 'movies' in query:
            dir='C:\\Users\\Amol\\Desktop\\movies'
            list=os.listdir(dir)
            print(list)
            if 'acharya' in query:
                os.startfile(os.path.join(dir,list[0]))

            elif 'puramulo' in query:
                os.startfile(os.path.join(dir,list[1]))    

            elif 'raw' in query:
                os.startfile(os.path.join(dir,list[2]))    

            elif 'bhool bhulaiyaa' in query:
                os.startfile(os.path.join(dir,list[3])) 

            elif 'strange' in query:
                os.startfile(os.path.join(dir,list[4]))    

            elif 'sher' in query:
                os.startfile(os.path.join(dir,list[6]))
                    
            elif 'jalpari' in query:
                os.startfile(os.path.join(dir,list[7]))    
        #=======================================================================================
        elif 'help' in query:
                self.speak('here are some query you can use')
                h='''
who are you : for the intoduction of AI 
youtube : to start youtube in web browser
time : to check current time 
wikipedia : to search wikipedia 
next:goto the second screen 
quit : to terminate program
                '''
                self.leb.text=self.leb.text+h
        elif'who are you' in query:
                    self.speak('I am veronica, i am A.i system of created by self,with love of you, i m a ho,such a disspointment to this dammed world') 
        elif 'quit' in query:
            self.speak('have a great day')

            quit()
        else:
            self.speak("please give appropriate query")

    # def anim(self,widget,*args):
    #     animate=Animation(background_color=(0,0,0,0),d=1)
    #     animate.start(widget)
        

# =========================================================================
#  Function for Clock
    def update(self,*args):
        self.ti.text= datetime.datetime.now().strftime("[b]%H:%M[/b]:%S")
    def __init__(self, **kwargs):
        super(FirstWindow,self).__init__(**kwargs)
        Clock.schedule_interval(self.update,1)
#============================================================================

class SecondWindow(Screen):
	pass

class ThirdWindow(Screen):
    pass

class ForthWindow(Screen):
    Config.set('graphics', 'resizable', 1)
    def calculate(self, calculation):
            if calculation:
                try:
                    self.display.text = str(eval(calculation))
                except Exception:
                    self.display.text = "Error"
    def delete(self, dele):
            if dele:
                try:
                    self.display.text = str(dele[:-1])
                except Exception:
                    self.display.text = "Error"
    def exit(self):
            quit()

class FifthWindow(Screen):
    pass

class SixthWindow(Screen):
    pass

kv = Builder.load_file('app.kv')
class app(App):
	def build(self):
		return kv

# if __name__ == '__main__':
    
def speak(audio):
        print(audio)
        engine.say(audio)
        engine.runAndWait()

def wishme():
        hour = int(datetime.datetime.now().hour)
        speak("hello sir ")    
        if hour>=0 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        else:
            speak("Good Evining!")         
        speak("i am friday, how may i help you?")    
wishme()
app().run()