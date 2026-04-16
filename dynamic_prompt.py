from google import genai

client = genai.Client(api_key="AIzaSyC5L2k8ZflIpS--TY6IsA2R4Sxp5IGRxrY")

user_input = input("Ask me anything: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input
)
print(response.text)