import os 
from dotenv import load_dotenv
import requests

load_dotenv()  # take environment variables from .env.

APP_ID =  os.environ.get("nutritionix_app_id")
API_KEY = os.environ.get("nutritionix_api_key")


natural_lang_for_exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"


parameters = {
    "query": "I ran 1 mile"
}

headers = {
    "x-app-id": APP_ID,
    "x-api-key": API_KEY
}

response = requests.post(url=natural_lang_for_exercise_url, json=parameters, headers=headers)
response.raise_for_status()

print(response.text)
