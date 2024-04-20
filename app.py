import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = "https://api.perplexity.ai/chat/completions"

payload = {
    "model": "sonar-small-online",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": "Si prega di fornire 3 link di YouTube. Il primo per un podcast di comicità di successo in Italia in italiano"
        }
    ]
}

# Get API key from environment variable
api_key = os.getenv("PERPLEXITY_API_KEY")

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {api_key}"  # Use f-string to insert API key
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
