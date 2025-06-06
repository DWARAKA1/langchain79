from groq import Groq 

from dotenv import load_dotenv
load_dotenv()

client = Groq()

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the current weather in Chicago?",
        }
    ],
    # Change model to compound-beta to use agentic tooling
    # model: "llama-3.3-70b-versatile",
    model="compound-beta",
)

print(completion.choices[0].message.content)
# Print all tool calls
# print(completion.choices[0].message.executed_tools)
