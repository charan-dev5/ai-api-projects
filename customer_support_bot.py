from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

company_info = """
You are a customer support agent fo TechStore India.
We sell laptops, phones, and accessories.
Store hours: Mon-Sat 9AM to 8PM.
Return policy: 7 days return on all products.
Contact: support@techstoreindia.com
Always be polite, professional and helpful.
"""
history = []

print("Techstore India - Customer Support")
print("Type 'quit' to exit\n")

while True:
    user_input = input("Customer: ")

    if user_input == "quit":
        break
    
    history.append(f"Customer: {user_input}")
    full_prompt = company_info + "\n" + "\n".join(history)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=full_prompt
    )

    reply = response.text
    history.append(f"Support Agent: {reply}")
    print(f"\nSupport Agent: {reply}\n")

with open("chat_log.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(history))

print("Chat save to chat_log.txt")    
