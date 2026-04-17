from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

print("=== AI Email Writer ===\n")

sender_name = input("Your name: ")
recipient = input("Recipient (e.g. client, manager, supplier): ")
email_type = input("Email type (sales/follow-up/complaint/proposal/thank-you): ")
topic = input("What is the email about? ")
tone = input("Tone (formal/friendly/urgent): ")

prompt = f"""
You are a professional email writer.
Write a {tone} {email_type} email from {sender_name} to a {recipient}.
Topic: {topic}
Requirements:
- Clear subject line
- Professional greeting
- Concise body
- Strong closing
- Signature with {sender_name}
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

email = response.text

print("\n=== Generated Email ===\n")
print(email)

filename = f"{email_type}_email_{sender_name.replace(' ', '_')}.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write(email)

print(f"\nEmail saved to {filename}")