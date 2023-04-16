import openai
import os
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
r, mic = None, None


def fetch_response(prompt):
    model = "text-davinci-002"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text


def initialize_sr():
    global mic, r
    r = sr.Recognizer()
    mic = sr.Microphone()


def listen_to_speech():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    return audio


def recognize_speech(audio):
    text = r.recognize_google(audio)

    return text


prompt = "State thevenin's theorem"
