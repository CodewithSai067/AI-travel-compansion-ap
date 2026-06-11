import os
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_location(destination):
    url = (
        f"https://maps.googleapis.com/maps/api/geocode/json"
        f"?address={destination}"
        f"&key={GOOGLE_MAPS_API_KEY}"
    )

    response = requests.get(url)
    return response.json()