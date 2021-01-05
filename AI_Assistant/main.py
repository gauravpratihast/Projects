from typing import Dict, List, Any
import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import time
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys
from nltk.chat.util import Chat, reflections

from requests.models import Response

engine = pyttsx3.init('sapi5')  # Used to initiate the voice of the program.


voices = engine.getProperty('voices')  # Used to get the property of voices.
engine.setProperty('voice', voices[0].id)  # Used to set the voice you want..0--> male voice , 1--> female voice.


def speak(audio):
    print("Lucifer: " + audio)  # Audio function is used to get audio of the program.
    engine.say(audio)
    engine.runAndWait()


def wishme():  # Greeting function in which your program grrets you accprding to the time you run him.
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning sir")

    elif 13 <= hour <= 17:
        speak("Good Afternoon sir")

    elif 17 < hour <= 19:
        speak("Good Evening sir")

    else:
        speak("Good Night sir")

    speak("How may I help you")


def compliment():
    l = ["You are amazing", "You look great today sir", "You are very cute sir", "You look dull sir have some coffee",
         "try more harder sir you can do it "]
    r = random.randint(0, 4)
    speak(l[r])



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said: {query}\n ")

    except Exception as e:
        print(e)

        print("say that again please.....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("pratihastgaurav@gmail.com", "blah blah")
    server.sendmail("pratihastgaurav@gmail.com", to, content)


if __name__ == '__main__':
    count = 0
    wishme()
    while True:
        query = takeCommand().lower()
        # Logics for tasks...
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)


        elif "open youtube" in query:
            speak("opening youtube sir")
            webbrowser.open("www.youtube.com")

        elif "open my gmail" in query:
            speak("opening your gmail sir!")
            webbrowser.open("www.gmail.com")

        elif "open google" in query:
            speak("opening google sir")
            webbrowser.open("www.google.com")


        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("telling sir")
            speak(strtime)

        elif "date and time" in query:
            lt = time.asctime(time.localtime(time.time()))
            today = date.today()
            speak(lt)
            speak(today)


        elif "play music" in query:
            music_dir = r"D:\songs"
            song = os.listdir(music_dir)
            print(song)
            speak("opening sir wait a minute")
            os.startfile(os.path.join(music_dir, song[0]))
            speak("your has been started please enjoy!")

        elif "open sublime" in query:
            codepath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Sublime Text 3"
            speak("opening sir wait a minute")
            os.startfile(codepath)


        elif "open my media player" in query:
            path = r"C:\Music\media.py"
            speak("Opening sir wait a minute")
            os.startfile(path)

        elif "compliment me" in query:
            compliment()

        elif "an email" in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "apallied21@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir there is an error due to which i can not send an email")

        elif "suggest me some name" in query:
            speak("It is a girl or a boy")
            i = takeCommand()
            boy_names = ["gaurav", "saurav", "prashant", "jayant", "arjun", "kapil", "nitin", "jatin"]
            girl_name = ["sakshi", "vishakha", 'x', "yz", 's', 'f', 'h', 'g', 'l', 'o', 'i', 'u', 'y', 't', 'e', 'w,']
            if "boy" in i:
                j = random.randint(0, len(boy_names) - 1)
                k = boy_names[j]
                print(f"--> {k}")
                speak(f"I think {k} is a good name for him.")
            elif "girl" in i:
                j = random.randint(0, len(girl_name) - 1)
                k = girl_name[j]
                print(f"--> {k}")
                speak(f"I think {k} is a good name for her.")
            else:
                speak("Plaese select a proper gender")

        elif "chat" in query:

            pairs = [
                [
                    r"my name is (.*)",
                    ["Hello %1, How are you today ?", ]
                ],
                [
                    r"what is your name ?",
                    ["My name is Chatty and I'm a chatbot ?", ]
                ],
                [
                    r"how are you ?",
                    ["I'm doing good\nHow about You ?", ]
                ],
                [
                    r"sorry (.*)",
                    ["Its alright", "Its OK, never mind", ]
                ],
                [
                    r"i'm (.*) doing good",
                    ["Nice to hear that", "Alright :)", ]
                ],
                [
                    r"hi|hey|hello",
                    ["Hello", "Hey there", ]
                ],
                [
                    r"(.*) age?",
                    ["I'm a computer program dude\nSeriously you are asking me this?", ]

                ],
                [
                    r"what (.*) want ?",
                    ["Make me an offer I can't refuse", ]

                ],
                [
                    r"(.*) created ?",
                    ["Gaurav created me using Python's NLTK library ", "top secret ;)", ]
                ],
                [
                    r"(.*) (location|city) ?",
                    ['Chennai, Tamil Nadu', ]
                ],
                [
                    r"how is weather in (.*)?",
                    ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
                     "Never even heard about %1"]
                ],
                [
                    r"i work in (.*)?",
                    ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
                ],
                [
                    r"(.)raining in (.)",
                    ["No rain since last week here in %2", "Damn its raining too much here in %2"]
                ],
                [
                    r"how (.) health(.)",
                    ["I'm a computer program, so I'm always healthy ", ]
                ],
                [
                    r"(.*) (sports|game) ?",
                    ["I'm a very big fan of Football", ]
                ],
                [
                    r"who (.*) sportsperson ?",
                    ["Messy", "Ronaldo", "Roony"]
                ],
                [
                    r"who (.*) (moviestar|actor)?",
                    ["In india it is Rajkumar Rao and Nawazuddin siddquie", "Outside india it is lenardo di cap rio"]
                ],
                [
                    r"quit",
                    ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
                ],
            ]


            def firstChatBot():
                speak("Say hello!")
                query = takeCommand().lower()
                speak(
                    "Hi , I am your chat bot.\n Now if want to talk to me then come with keyborad otherwise i can't talk to you.")
                chatbot = Chat(pairs, reflections)
                chatbot.converse()


            firstChatBot()


        elif ("quit" or "stop") in query:
            speak("Ok i am quiting myself!")
            break

        elif 'philosophy'in query:
            import requests
            from bs4 import BeautifulSoup

            url = 'https://www.goodreads.com/quotes/tag/{}?page={}'


            def get_quotes(url):
                res: Response = requests.get(url)

                soup = BeautifulSoup(res.text,)
                quote_divs = soup.find_all('div', attrs={'class': 'quote'})
                quotes: List[Dict[str, Any]] = []

                for quote_div in quote_divs:
                    quote_text = quote_div.find_next('div', attrs={'class': 'quoteText'})

                    stripped_li = quote_text.text.strip()

                    text = stripped_li.split('\n')

                    quote = text[0][1:-1]
                    author = text[-1].strip()

                    quote_item = {
                        'quote': quote,
                        'author': author
                    }

                    quotes.append(quote_item)
                return quotes


            total = []
            for i in range(5):
                total.extend(get_quotes(url.format('philosophy', i)))

            k = random.randint(0,150)
            s = total[k]
            quote_and_author = []
            for i, j in s.items():
                quote_and_author.append(j)
            speak(f'The qoute is {quote_and_author[0]} and the author is {quote_and_author[1]}')

        elif "game" in query:
            speak("This is a Snake , Water and Gun game.")
            set = ("Snake", "Water", "Gun")
            comp_score = 0
            My_score = 0
            Draw = 0
            i = 0
            while i < 5:
                h = random.choice(set)
                j = input("Choice any one of them Snake,Water and Gun: ")
                j = j.capitalize()
                if h == "Snake":
                    if j == "Water":
                        speak("You lose")
                        comp_score += 1
                    elif j == "Gun":
                        speak("You win")
                        My_score += 1
                    else:
                        speak("Draw")
                        Draw += 1
                    i += 1
                if h == "Water":
                    if j == "Gun":
                        speak("You lose")
                        comp_score += 1
                    elif j == "Snake":
                        speak("You win")
                        My_score += 1
                    else:
                        speak("Draw")
                        Draw += 1
                    i += 1
                if h == "Gun":
                    if j == "Snake":
                        speak("You lose")
                        comp_score += 1
                    elif j == "Water":
                        speak("You win")
                        My_score += 1
                    else:
                        speak("Draw")
                        Draw += 1
                    i += 1

                if h == "q":
                    break

            if My_score == comp_score:
                speak("Game Draw")
            elif My_score > comp_score:
                speak("You won")
            else:
                speak("Lucifer wins")




        else:
            query = query
            speak("Searching")
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak("Wait a minute")
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentence=4)
                    speak("got it")
                    speak("WIKIPEDIA says - ")
                    speak("results")

            except:
                speak(
                    "I don't understand what you just say, Can you please say that again")
                # webbrowser.open("www.google.com")
                count +=1
                if count>1:
                    break

        speak("next command sir!")
