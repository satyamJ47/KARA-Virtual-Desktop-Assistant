import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import datetime
import wikipedia as wp
import os
import smtplib
# import winshell
from calendar import *
# import pyautogui as pa
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
 
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening')
		r.pause_threshold = 1
                # r.energy_threshold = 100
		audio = r.listen(source)
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			# print(e)
			print("Say that again sir");speak("Say that again sir")
			return "None"
		return Query

def tellDay():
	day = datetime.datetime.today().weekday() + 1
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)

def Hello():
	speak("hello I am your desktop assistant.")
       
    
def wishme():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
                speak("Good Morning!")
        elif hour>=12 and hour<18:
                speak("Good Afternoon!")
        else:
                speak("Good Evening!")

        speak("I am kara How may I help you?")

# def Take_query():
	# Hello()
#     wishme()
    
def sendEmail(to, content):
    obj=smtplib.SMTP_SSL("smtp.gmail.com",465)
    obj.login("asp15299@gmail.com","wbhdpjblnscdyskq")
    obj.sendmail("asp15299@gmail.com",to,content)
    obj.quit()

if __name__ == '__main__':
#    Hello();wishme()
   while True:
        Query=takeCommand().lower()
        # Query="open youtube"
        if "from wikipedia" in Query:
                speak("Searching wikipedia...!")
                Query = Query.replace("wikipedia", "")
                r=wp.summary(Query, sentences=2)
                speak("According to wikipedia we got..")
                print(r)
                speak(r)

        elif "which day it is" in Query:
                tellDay()

        elif "tell me your name" in Query:
                speak("I am kara How may I help you?")


        elif "open google" in Query:
                speak("Opening Google")
                wb.open("www.google.com")
                # continue

        elif "google search" in Query:
                import wikipedia as googleScrap
                Query = Query.replace("kara","")
                Query = Query.replace("google search","")
                Query = Query.replace("google","")

        elif "open youtube" in Query:
                wb.open("https://www.youtube.com")
                # exit()
                # continue

        elif "open hackerrank" in Query:
                wb.open("https://www.hackerrank.com/satyam47")
                # continue

        elif "open linkedin" in Query:
                wb.open("https://www.linkedin.com/in/satejbpatil/")
                # continue

        elif "open leetcode" in Query:
                wb.open("https://leetcode.com/satyam47/")
                # continue

        elif "open twitter" in Query:
                wb.open("https://twitter.com/satejbpatil")
                # continue

        elif "open whatsapp" in Query:
                wb.open("https://web.whatsapp.com/")
                # continue

        elif "hotels near me" in Query:
                wb.open("https://www.google.com/maps/search/Restaurants/@16.9460802,74.3688759,14z")
                # continue

        # shopping
        elif "shopping" in Query:
                speak("which website would you like.")
                Query1=takeCommand().lower()
                print(Query1)
                if "amazon" in Query1:
                        wb.open("https://www.amazon.in/")
                        # continue
                
                elif "myntra" in Query1:
                        wb.open("https://www.myntra.com/?utm_source=dms_google&utm_medium=searchbrand_cpc&utm_campaign=dms_google_searchbrand_cpc_Search_Brand_Myntra_Brand_India_BM_TROAS_SOK&gclid=Cj0KCQiAm5ycBhCXARIsAPldzoUnVJ24avNWDOD31LCMucKtNRaxDhA3m0cG687ts2ZvMaIE_VLIjNMaAlSaEALw_wcB")
                        # continue

                elif "meesho" in Query1:
                        wb.open("https://www.meesho.com/")
                        # continue

        elif "open spotify" in Query:
                wb.open("https://open.spotify.com/show/5MIQC4i9ggv1AaQaXMI5Nv")
                # continue

        # elif "play music" in Query:
        #         music_dir='D:\\Music\\Waiting For Love.mp3'
        #         os.startfile(music_dir)

        elif "play music" in Query:
                music_dir = "D:\\Music\\"
                songs=os.listdir(music_dir)
                maxsong=len(songs)
                print(songs)
                rand=random.randint(0, maxsong-1)
                print(rand)
                os.startfile(os.path.join(music_dir,songs[rand]))
                
        elif "the time" in Query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                # continue

        elif "open code editor" in Query:
                codepath="C:\\Users\\satej\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
                os.startfile(codepath)
                # continue

        elif "open powerpoint" in Query:
                codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(codepath)
                # continue

        elif "open word" in Query:
                codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(codepath)
                # continue

        elif "open excel" in Query:
                codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(codepath)
                # continue

        elif "open chrome" in Query:
                codepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codepath)
                # continue

        elif "open microsoft edge" in Query:
                codepath="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(codepath)
                # exit()
                

        # elif "open command prompt" in Query:
        #         codepath="%windir%\\system32\\cmd.exe"
        #         os.startfile(codepath)
        #         exit()

        elif "email" in Query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "fcbixaron@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                # continue
                # exit()
            except Exception as e:
                print(e)
                speak("EMAIL HAS NOT SENT YET!")    
                
                # continue

        # elif "recycle bin" in Query:
        #         try:
        #                 winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
        #                 print("Recycle bin is emptied Now!")
        #         except:
        #                 print("Recycle bin is already empty!")
        #         # continue

        # elif "change desktop" in Query:
        #         pa.hotkey('win','ctrl','left') #will switch one desktop to the left
        #         pa.hotkey('win','ctrl','right') #will switch one desktop to the right
        #         # continue

        elif "open calender" in Query:
                # year=int(input("Enter Year: ")
                print(calendar(2022,2,1,8,4))


#         # pip install AppOpener
# from AppOpener import run
# run("whatsapp") # Opens whatsapp if installed

        

        elif "bye" in Query or "end" in Query or "shutdown" in Query:
                speak("As you wish") 
                exit()

        else:
                print("No such Command.")


