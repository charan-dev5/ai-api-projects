from google import genai

client = genai.Client(api_key="YOUR_API_KEY_HERE")

user_input = input("Ask me anything: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input
)
print(response.text)