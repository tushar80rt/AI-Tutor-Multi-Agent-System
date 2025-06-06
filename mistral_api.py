import requests
from config import MISTRAL_API_KEY 
def mistral_chat(messages):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-small-2503",
        "messages": messages
    }
    res = requests.post(url, headers=headers, json=data)
    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]

