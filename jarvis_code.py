import pyttsx3
import speech_recognition as sr
import datetime
from time import sleep
import os
import webbrowser , wikipedia
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak_msg(st):
    '''This function is used to convert given text string into voice form'''
    engine.say(st)
    engine.runAndWait()
    
def tell_msg(st):
    '''This function is used to convert voice message into text format'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak_msg("Speak "+st)
        msg = r.listen(source)
        msg_text = r.recognize_google(msg)
        
    return(msg_text)


def set_values(r):
    '''Setting specific values for different parameters (optional)'''
    r.pause_threshold = 0.5
    r.energy_threshold = 300
    r.non_speaking_duration = 0.2
    r.phrase_threshold = 0


def wish_me():
    '''This function is used to wish Good Morning, Good Afternoon and Good Evening as per time'''
    hour = datetime.datetime.now().hour
    
    if hour>=0 and hour<=12:
        speak_msg("Good Morning Sir, how may i help you")
    elif hour>12 and hour<=18:
        speak_msg("Good Afternoon Sir, how may i help you")
    else:
        speak_msg("Good Evening Sir, how may i help you")

def send_mail():
    '''This function is used to send text message from one person to other just by voice'''
    
    # starting the server
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s_email_text = tell_msg("Sender's Email")
    s_email_text = s_email_text.lower()
    s_email = s_email_text.replace(" ","")+"@gmail.com"
    print("Sender's Email : "+s_email)
    
    password = "bunwaxscixztoarw"
    #server.login(username,password)
    server.login(s_email,password)
    
    r_email_text = tell_msg("Receiver's Email")
    r_email_text = r_email_text.lower()
    r_email = r_email_text.replace(" ","")+"@gmail.com"
    print("Receiver's Email : "+r_email)
    
    msg = tell_msg("your msg")
    print("your msg is : ",msg)
    
    #sendmail(from,to,message)
    server.sendmail(s_email,r_email,msg)
    
    speak_msg("Mail sent")
    server.quit()
    
def task(query):
    
    if "wikipedia" in query:
        speak_msg("Searching Wikipedia....")
        query.replace("wikipedia", "")
        result = wikipedia.summary(query , sentences=2)
        print(result)
        speak_msg(f"Here is what I found..., {result}")

    elif "open google" in query:
        webbrowser.open("google.com")

    elif "open youtube" in query:
        webbrowser.open("youtube.com")  

    elif "open code" in query:
        os.startfile("C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    
    elif "time"in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak_msg(str_time)
        
    elif "send mail" in query:
        send_mail()

    elif "quit" in query:
        speak_msg("Jarvis is pleased to help you sir")
        exit()


def input_query():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is listening sir,")
        speak_msg("Jarvis is listening sir")
        
        set_values(r)
        
        print("listening")
        audio = r.listen(source)
        query = ''
        print("listened")
    try:
        print('Recognising the command')
        speak_msg('Recognising the command')
        query = r.recognize_google(audio)
        print(f"User said: {query}")

    except Exception as e:
        print("Can't Recognise the command, Please say that again")
        speak_msg("Can't Recognise the command, Please say that again")
        
    return query


if __name__ =="__main__":
    wish_me()
    while True:
        command = input_query().lower()
        task(command)
        print("\n")
        sleep(3)