from google import genai

client = genai.Client(api_key="YOUR_API_KEY_HERE")

system_prompt = "You are a professional email writer. Write formal, concise emails only."

user_input = input("What is the email about? ")

full_prompt = f"{system_prompt}\n\nWrite an email about: {user_input}"

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=full_prompt
)

print(response.text)