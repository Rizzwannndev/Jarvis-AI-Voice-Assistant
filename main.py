from openai import OpenAI
import pyttsx3
import speech_recognition as sr
import webbrowser
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsApi = "API_KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="API_KEY")

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant skilled like Alexa."},
            {
                "role": "user","content": command
            }
        ]
    )
    return(completion.choices[0].message.content)

def processCommand(c):
    print(f"Command: {c.capitalize()}")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if articles:
                for article in articles:
                    speak(article['title'])
            else:
                speak("No news articles found.")
        else:
            speak(f"Sorry, I couldn't fetch the news right now. Error code: {r.status_code}")
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":

    speak("Initializing Jarvis...!")
    while True:
        # listen for the wake word "Jarvis"

        r = sr.Recognizer()

        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                word = r.recognize_google(audio, language="en-US", show_all=False)
                if(word.lower() == 'jarvis'):
                    print("Recognized: 'JARVIS'")
                    speak("Yes Sir")
                    # Listen for Command
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the speech recognition service.")
        except Exception as e:
            print("Error: ", e)