import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
engine.say("i am johnny")
engine.say("what can i do for you")
engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='en-in')
            command = command.lower()
            if 'johnny' in command:
                command = command.replace('johnny', '')
                print(command)
    except:
        pass
    return 

def run_johnny():
    command=take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
while True:
    run_johnny()




