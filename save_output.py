from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

user_input = input("What report do you want? ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=f"Write a professional report about: {user_input}"
)

with open("report.txt", "w") as file:
    file.write(response.text)

print("Report saved to report.txt")    
