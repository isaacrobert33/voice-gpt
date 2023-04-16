import os
import speech_recognition as sr
from dotenv import load_dotenv
from utils import fetch_response, listen_to_speech, recognize_speech, speak_text

load_dotenv()

API_KEY = os.environ["OPENAI_API_KEY"]
model = "text-davinci-002"
r, mic = None, None


def initialize_sr():
    global mic, r
    r = sr.Recognizer()
    mic = sr.Microphone()


initialize_sr()
print("[*] Listening to speech...")
audio = listen_to_speech(mic=mic, r=r)
print("[*] Running speech recognition on speech...")
try:
    prompt = recognize_speech(r, audio=audio)
except:
    print("Error recognizing speech")
print(f"[*] Fetching response to prompt ({prompt})...")
response = fetch_response(API_KEY, model, prompt=prompt)
print("[*] Running speech syntheis for response")
print(response)
# speak_text(response)


prompt = "State thevenin's theorem"
