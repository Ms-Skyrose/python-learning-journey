from fastapi import FastAPI, HTTPException
import requests

bot = FastAPI()

# Replace with your actual Gemini API key from Gemini Studio
GEMINI_API_KEY = "AIzaSyAZNIweXFmqappt0U2JSL63cIshCjmRRiY"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

@bot.post("/ask-gemini")
async def ask_gemini(text: str):
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {"parts": [{"text": text}]}
        ]
    }

    params = {"key": GEMINI_API_KEY}

    try:
        response = requests.post(GEMINI_URL, headers=headers, json=payload, params=params)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return {"gemini_response": response.json()}

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
