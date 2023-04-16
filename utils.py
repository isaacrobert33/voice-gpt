import openai
import os
import pyttsx3


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def fetch_response(api_key, model, prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text


def listen_to_speech(mic, r):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    return audio


def recognize_speech(r, audio):
    text = r.recognize_google(audio)
    return text
