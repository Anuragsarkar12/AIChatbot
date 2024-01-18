import speech_recognition as sr 
import pyttsx3
import webbrowser
import openai
from datetime import datetime
from openai import OpenAI
from pathlib import Path
import random


ChatStr=""
def chat(query):
    global ChatStr
    print(ChatStr)
    ChatStr += f"User:{query}\n Jarvis:"

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "write an email to my boss for resignation?"
            },
            {
                "role": "user",
                "content": ChatStr
            },
            {
                "role": "assistant"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["message"]["content"])
    ChatStr +=f"{response['choices'][0]['message']['content']}\n"
    return response["choices"][0]["message"]["content"]
 
    #with open(f"Openai/prompt-{random.randint(1,2343434356)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
        f.write(text)


api_key = 'your-api-key'
openai_client = OpenAI(api_key=api_key)




def ai(prompt):
    text=f"OpenAI response for Prompt:{prompt} \n*******\n\n"
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "write an email to my boss for resignation?"
            },
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #print(response["choices"][0]["message"]["content"])
    text +=response["choices"][0]["message"]["content"]
    directory_path = Path("Openai")
    if not directory_path.exists():
        directory_path.mkdir()
    
    #with open(f"Openai/prompt-{random.randint(1,2343434356)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
        f.write(text)



def say(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry I didnt get that")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
        return ""


if __name__ == '__main__':
    say("Hello I am Jarvis  A I ")
    while True:
        print("Listening...")
        query=takecommand()
        sites = [["YouTube","https://www.YouTube.com"],["Wikipedia","https://www.Wikipedia.com"],
                ["Google","https://www.Google.com"],["Instagram","https://www.Instagram.com"] ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "the time" in query:
            strfTime=datetime.now().strftime("%H:%M:%S")
            say(f"sir the time is {strfTime}")
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif"Jarvis Quit".lower() in query.lower():
            exit()
        elif"Jarvis Reset Chat".lower() in query.lower():
            ChatStr = ""
            
        else:
            print("chatting...")
            chat(query)
        
        



            

            
    

    