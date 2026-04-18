from flask import Flask, render_template, request, jsonify
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = genai.Client(api_key=os.getenv("API_KEY"))

history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    history.append(f"User: {user_message}")
    full_prompt = "\n".join(history)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=full_prompt
    )

    reply = response.text
    history.append(f"Assistant: {reply}")

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)                   
        


