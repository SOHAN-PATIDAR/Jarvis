import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def tell(st):
    '''This function is used to speak some text given given as string'''
    engine.say(st)
    engine.runAndWait()
    
def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        tell("Speak your msg")
        msg = r.listen(source)
        msg_text = r.recognize_google(msg)
        
    return(msg_text)



tell("Hello How are you")
print(speak())