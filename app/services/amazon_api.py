import requests
from app.core.config import settings

def fetch_books(query: str):
    # Mock example of interacting with Amazon API
    headers = {"Authorization": f"Bearer {settings.amazon_api_key}"}
    response = requests.get(f"https://amazon.api/endpoint?query={query}", headers=headers)
    return response.json()
