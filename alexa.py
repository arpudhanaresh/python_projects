import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer class (for recognizing the speech)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
extracted_command = ""

def talk(text):
    engine.say(text)
    engine.runAndWait()


def run_alexa():
    final_command = take_command()
    if 'play' in final_command:
        song = final_command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in final_command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in final_command:
        person = final_command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you single' in final_command:
        talk('I am in a relationship with wifi')
    elif 'joke' in final_command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


def take_command():
    extracted_command = ""
    test = ""
    try:
        with sr.Microphone() as source:
            print('I am listening...')
            voice = listener.listen(source)
            
            source_command = listener.recognize_google(voice)
            
            source_command = source_command.lower()
            
            if 'alexa' in source_command:
                source_command = source_command.replace('alexa', '')
                print(source_command)
            

            print("command",source_command)
            extracted_command = source_command
    except:
        print("expect")
        pass
    return extracted_command


# output_command = take_command()

while True:
    run_alexa()

