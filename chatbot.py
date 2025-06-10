# chatbot.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_response(user_input):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",  # Or use "mixtral-8x7b-32768" or "gemma-7b-it"
        "messages": [
            {"role": "system", "content": "You are mkchatbot, a helpful and friendly AI assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Sorry, an error occurred: {str(e)}"