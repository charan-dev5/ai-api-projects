from google import genai

client = genai.Client(api_key="AIzaSyC5L2k8ZflIpS--TY6IsA2R4Sxp5IGRxrY")

history = []

while True:
    user_input = input("You: ")

    if user_input == "quit":
        break

    history.append(f"User: {user_input}")

    full_prompt = "\n".join(history)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=full_prompt
    )

    reply = response.text
    history.append(f"Gemini: {reply}")

    print(f"Gemini: {reply}")