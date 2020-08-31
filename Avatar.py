import pytz
from win32com.client import Dispatch
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import pyjokes
from textblob import TextBlob
date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
# dictionary of languages with codes
d={'en':'english', 'ja':'japanese', 'ar':'arabic', 'hi':'hindi','mr':'marathi','ur':'urdu','gu':'gujarati','te':'telugu','ta':'tamil','es':'spanish'}
def translate():
    speak('translate mode on. what you want to translate')
    cmd=command().lower()
    tb=TextBlob(cmd)
    speak('In which language you want the translation master')
    code=command().lower()
    speak('your translation is here in'+ code)
    for key,value in d.items():
        if value==code:
            lang_code=key
    result=tb.translate(to=lang_code)
    print(result)
def jokes():
    joke=pyjokes.get_joke('en',category='all')
    print(joke)
    speak(joke)
def speak(audio):
    speaking=Dispatch('SAPI.Spvoice')
    speaking.speak(audio)
def date():
    d = date.strftime('%d %B, %Y')
    speak(d)
def birthday():
    date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
    if date.strftime('%d %B') == '01 October':
        speak('Happy Birthday Vaibhavi')
    else:
        speak('your birthday is on 1st october master')
def time():
    time_now=datetime.datetime.now().strftime('%H:%M:%S')
    print(time_now)
    speak('the running time is '+ time_now)
def greeting():
    time=datetime.datetime.now().hour
    if 17>time>12:
        speak('Good afternoon master')
    elif 20>time>17:
        speak('Good Evening master')
    elif 3<time>20:
        speak('Good night master! time to sleep')
    else:
        speak('good morning')
def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak('Order me master')
        cmd=r.listen(source)
        try:
            recognized = r.recognize_google(cmd)
            print(recognized)
        except:
            print('sorry!')
    return recognized
if __name__ == '__main__':
    greeting()
    speak('Avatar at your service master')
    while True:
        ask=command().lower()
        if 'time' in ask:
            time()
        elif 'date' in ask:
            date()
        elif 'birthday' in ask:
            birthday()
        elif 'What can you do for me' in ask:
            speak('I can do whatever you order me master. I can search anything you want, translate any sentence for you, i can tell jokes, shutdown or restart just order me master. your pc or  ')
        elif 'wikipedia' in ask:
            speak('searching in progress')
            ask=ask.replace('wikipedia','')
            result=wikipedia.summary(ask,4)
            print(result)
            speak(result)
        elif 'open google' in ask:
            webbrowser.open_new_tab('google.com')
        elif 'open youtube' in ask:
            webbrowser.open_new_tab('youtube.com')
        elif 'translate' in ask:
            translate()
        elif 'joke' or 'tell me a joke' in ask:
            jokes()
        elif 'exit' in ask:
            quit()
        elif 'search' in ask:
            ask = ask.replace('search', '')
            # you can give path of any browser you want to use
            # chrome='C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
            webbrowser.open_new_tab(ask + '.com')
            speak('Done')
        elif 'good job' in ask:
            speak('pleasure master')
        elif 'shutdown' in ask:
            speak('your ordered me to shutdown your pc sir')
            os.system('shutdown /s /t 1')
        elif 'restart' in ask:
            speak('your ordered me to restart your pc sir')
            os.system('shutdown /r /t 1')


