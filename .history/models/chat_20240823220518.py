import os
import openai
client = OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

def chat(inp, message_history, role="user"):
    message_history=[]
    message_history.append({"role": role, "content": f"{inp}"})
    completion = OpenAI.chat.completions.create(
        model="",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return reply_content

def chat(inp, message_history, role="user"):
    message_history=[]
    message_history.append({"role": role, "content": f"{inp}"})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    return reply_content
