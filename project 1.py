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
    
def capital(state):
    if state=='Andhra Pradesh':
        speak('Amaravati')
    elif state=='Arunachal Pradesh':
        speak('Itanagar')
    elif state=='Assam':
        speak('Dispur')
    elif state=='Bihar':
        speak('Patna')
    elif state=='Chhattisgarh':
        speak('Raipur')
    elif state=='Goa':
        speak('Panaji')
    elif state=='Gujarat':
        speak('Gandhinagar')
    elif state=='Haryana':
        speak('Chandigarh')
    elif state=='Himachal Pradesh':
        speak('Shimla')
    elif state=='Jharkhand':
        speak('Ranchi')
    elif state=='Karnataka':
        speak('Bengaluru')
    elif state=='Kerala':
        speak('Thiruvananthapuram')
    elif state=='Madhya Pradesh':
        speak('Bhopal')
    elif state=='Maharashtra':
        speak('Mumbai')
    elif state=='Manipur':
        speak('Imphal')
    elif state=='Meghalaya':
        speak('Shillong')
    elif state=='Mizoram':
        speak('Aizawl')
    elif state=='Nagaland':
       speak('Kohima')
    elif state=='Odisha':
        speak('Bhubaneswar')
    elif state=='Punjab':
        speak('Chandigarh')
    elif state=='Rajasthan':
        speak('Jaipur')
    elif state=='Sikkim':
       speak('Gangtok')
    elif state=='Tamil Nadu':
        speak('Chennai')
    elif state=='Telangana':
        speak('Hyderabad')
    elif state=='Tripura':
        speak('Agartala')
    elif state=='Uttar Pradesh':
        speak('Lucknow')
    elif state=='Uttarakhand':
        speak('Dehradun in Winter and Gairsain in Summer')
    elif state=='West Bengal':
        speak('West Bengal')
    elif state=='Andaman and Nicobar Islands':
        speak('Andaman and Nicobar Islands')
    elif state=='Dadra & Nagar Haveli and Daman & Diu':
        speak('Daman')
    elif state=='Delhi':
        speak('Delhi')
    elif state=='Jammu and Kashmir':
        speak('Srinagar in Summer and Jammu in Winter')
    elif state=='Lakshadweep':
        speak('Kavaratti')
    elif state=='Puducherry':
        speak('Pondicherry')
    elif state=='Ladakh':
        speak('Leh')
    elif state=='India':
        speak('New Delhi')
    else:
        speak('Please say that again...')

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
            
        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{time}")
         
    
            
      
        
            
    


    
