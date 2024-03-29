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

def tell_month():
    dt = datetime.datetime.today()
    m_onth = dt.month
    if m_onth == 1:
        speak("it's january")
    if m_onth == 2:
        speak("it's february")
    if m_onth == 3:
        speak("it's march")
    if m_onth == 4:
        speak("it's april")
    if m_onth == 5:
        speak("it's may")
    if m_onth == 6:
        speak("it's june")
    if m_onth == 7:
        speak("it's july")
    if m_onth == 8:
        speak("it's august")
    if m_onth == 9:
        speak("it's september")
    if m_onth == 10:
        speak("it's october")
    if m_onth == 11:
        speak("it's november")
    if m_onth == 12:
        speak("it's december")
        
def tell_day():
    now = datetime.datetime.now()
    ans=(now.strftime("%A"))
    speak(ans)
    
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
            
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open notepad' in query:
            os.startfile("C:\\Windows\\notepad.exe")
            
        elif 'close notepad' in query:
            os.system("TASKKILL /F /IM notepad.exe")
            
        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{time}")
            
        elif 'month' in query or 'month is going' in query:
            tell_month()

        elif 'day' in query or 'today' in query:
            tell_day()
            
        elif 'shut down' in query:
            print("Do you want to shutdown you system?")
            speak("Do you want to shutdown you system?")
            cmd = take()
            if 'yes' in cmd:
                os.system("shutdown /s /t 1")
                
        elif 'restart' in query:
            print("Do you want to restart your system?")
            speak("Do you want to restart your system?")
            cmd = take()
            if 'yes' in cmd:
                os.system("shutdown /r /t 1")
         
    
            
      
        
            
    


    
