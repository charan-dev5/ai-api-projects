from google import genai
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

personality = input("Give your AI a personality (e.g. helpful assistant, life coach, tech expert): ")

system_prompt = f"You are a {personality}. Be concise, smart and engaging."

history = []
chat_log = []

print(f"=== AI {personality.title()} ===")
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ")

    if user_input == "quit":
        break

    history.append(f"User: {user_input}")
    full_prompt = system_prompt + "\n\n" + "\n".join(history)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=full_prompt
    )

    reply = response.text
    word_count = len(reply.split())
    history.append(f"Assistant: {reply}")

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    chat_log.append(f"[{timestamp}] You: {user_input}")
    chat_log.append(f"[{timestamp}] Assistant: {reply}\n")

    print(f"\nAssistant ({word_count} words): {reply}\n")

filename = f"chat_{datetime.date.today()}.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("\n".join(chat_log))

print(f"Chat saved to {filename}")
    