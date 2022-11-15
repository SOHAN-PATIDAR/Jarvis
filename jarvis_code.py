import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(st):
    '''This function is used to speak some text given given as string'''
    engine.say(st)
    engine.runAndWait()
    
    
speak("Hello How are you")