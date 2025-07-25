from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"role": "user", "parts": [{"text": user_message}]}]
    }
    resp = requests.post(
        f"{GEMINI_URL}?key={GEMINI_API_KEY}", 
        json=data, 
        headers=headers
    )
    response_data = resp.json()
    print("Gemini API response:", response_data)

    if "candidates" not in response_data:
        error_message = response_data.get("error", {}).get("message", "Unknown error")
        reply = f"Sorry, Gemini API error: {error_message}"
    else:
        reply = response_data["candidates"][0]["content"]["parts"][0]["text"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True,port=8000)
    
