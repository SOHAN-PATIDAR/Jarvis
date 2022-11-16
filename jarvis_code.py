import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak_msg(st):
    '''This function is used to convert given text string into voice form'''
    engine.say(st)
    engine.runAndWait()
    
def tell_msg():
    '''This function is used to convert voice message into text format'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak_msg("Speak your msg")
        msg = r.listen(source)
        msg_text = r.recognize_google(msg)
        
    return(msg_text)


def wish_me():
    '''This function is used to wish Good Morning, Good Afternoon and Good Evening as per time'''
    hour = datetime.datetime.now().hour
    
    if hour>=0 and hour<=12:
        speak_msg("Good Morning Sir, how may i help you")
    elif hour>12 and hour<=18:
        speak_msg("Good Afternoon Sir, how may i help you")
    else:
        speak_msg("Good Evening Sir, how may i help you")




if __name__ =="__main__":
    wish_me()
    speak_msg("Hello How are you")
    print(tell_msg())