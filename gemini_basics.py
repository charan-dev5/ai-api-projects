from google import genai
client = genai.Client(api_key="AIzaSyC5L2k8ZflIpS--TY6IsA2R4Sxp5IGRxrY")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
