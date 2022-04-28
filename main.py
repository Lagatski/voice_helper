import speech_recognition as sr
import webbrowser
import wikipedia
import pyttsx3
import datetime
import os




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')     #даёт подробности о текущем установленном голосе
engine.setProperty('voices', voices[0].id)  # 0-мужской , 1-женский


def speak(audio):   
    engine.say(audio)    
    engine.runAndWait() #Без этой команды мы не услышим речь

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")    
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")       
    
    else:
        speak("Good Evening!")      
   

def takeCommand():
    #Принимает на входе аудио от микрофона, возвращает строку с нашими словами    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Используем google для распознания голоса.
        print(f"User said: {query}\n")  #Запрос пользователя выведен.    
    except Exception as e:
        # print(e)  используйте только если хотите видеть ошибку!
        print("Say that again please...")   #будет выведено, если речь не распознаётся
        return "None" #вернётся строка "Пусто"
    return query
    

if __name__ == "__main__":
    wishMe()
    while True:
        print("Here")
        query = takeCommand().lower() #Приведём запрос к нижему регистру        
        # выполнение задач в соответствии с запросом
        print("Here")
        if 'wikipedia' in query:  #если wikipedia встречается в запросе, выполнится блок:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = '../'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        


        
            
