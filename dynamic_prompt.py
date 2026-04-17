from google import genai
from dotenv import load_dotenv
import os

load_dotenv

client = genai.Client(api_key=os.getenv("API_KEY"))

user_input = input("Ask me anything: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input
)
print(response.text)