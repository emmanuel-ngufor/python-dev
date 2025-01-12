import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()  # take environment variables from .env.

APP_ID =  os.environ.get("nutritionix_app_id")
API_KEY = os.environ.get("nutritionix_api_key")
SHEET_ENDPOINT = os.environ.get("sheet_endpoint")
TOKEN = os.environ.get("token")


nutritionix_endpoint = "https://trackapi.nutritionix.com"
exercise_endpoint = f"{nutritionix_endpoint}/v2/natural/exercise"
parameters = {
    "query": str(input("Tell me what you did?: "))
}
nutritionix_headers = { 
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


# Get data from natural language processing API
response = requests.post(url=exercise_endpoint, json=parameters, headers=nutritionix_headers)  
response.raise_for_status()
workout_data = response.json()["exercises"]
print(workout_data)


sheety_headers = {
    "Authorization": TOKEN
}

# GET all rows currently on the sheet
response = requests.get(url=SHEET_ENDPOINT, headers=sheety_headers)
response.raise_for_status()
data = response.json() 
print(data) 


# ADDING a row to the sheet
for data in workout_data:
    payload = {
        "workout": {
            "date": datetime.now().strftime("%x"),
            "time": datetime.now().strftime("%X"),
            "exercise": data["name"].title(), 
            "duration": data["duration_min"],
            "calories": data["nf_calories"],
            }
        }
    
    response = requests.post(url=SHEET_ENDPOINT, json=payload, headers=sheety_headers)
    response.raise_for_status()
    print(response.text)


# DELETE a row from the sheet
object_id = str(input("Enter the row number you want to delete: "))
response = requests.delete(url=f"{SHEET_ENDPOINT}/{object_id}", headers=sheety_headers)
response.raise_for_status()
if response.status_code >= 200 and response.status_code < 300:
    print("1 row deleted")