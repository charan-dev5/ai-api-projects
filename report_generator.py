from google import genai
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

print("=== AI Report Generator ===\n")

topic = input("Enter report topic: ")
report_type = input("Enter report type (business/medical/technical): ")

system_prompt = f"""
You are a professional report writer.
Write a detailed, structured {report_type} report about: {topic}
Inclued: Executive Summary, Introduction, Main Analysis, Conclusion and Recommendations.
Use professional language and clear headings.
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=system_prompt
)

report = response.text

filename = f"report_{topic.replace(' ', '_')}_{datetime.date.today()}.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write(report)

word_count = len(report.split())

print(f"\nReport generated successfully!")
print(f"Saved as: {filename}")
print(f"Word Count: {word_count} words")