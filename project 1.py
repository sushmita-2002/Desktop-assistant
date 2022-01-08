import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<16:
        speak('Good Afternoon!')
    elif hour>=16 and hour<21:
        speak('Good Evening!')
    else:
        speak('I hope you enjoyed whole day ')
    speak('I am Sushmita desktop assitant. how I help you')
    
def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language="en-in")
        print('User said:', query)
    except  Exception as e :
        print('Please say that again...')
        return 'None'
    return query

if __name__ == "__main__":
    wish()
    if 1:
        query = take().lower()
        
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            result=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
            
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
            
        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{time}")
         
    
            
      
        
            
    


    