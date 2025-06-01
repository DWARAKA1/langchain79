import os
# Ensure the environment variable for Groq API key is set
from dotenv import load_dotenv
load_dotenv()

from groq import Groq


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of sustainable energy sources in modern day of world",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)