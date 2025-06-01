import os
from groq import Groq 

from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

speech_file_path = "speech.wav" 
model = "playai-tts"
voice = "Fritz-PlayAI"
text = "Hello Bayana Tulasemma,How are you and what are you doing !"
response_format = "wav"

# The model `playai-tts` requires terms acceptance. Please have the org admin accept the terms at https://console.groq.com/playground?model=playai-tts

response = client.audio.speech.create(
    model=model,
    voice=voice,
    input=text,
    response_format=response_format
)

response.write_to_file(speech_file_path)