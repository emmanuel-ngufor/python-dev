import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key =  os.environ.get("api_key")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

paramters = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "cnt": 4,
    "units": "metric"
}


response = requests.get(url=OMW_Endpoint, params=paramters)
response.raise_for_status()
weather_data = response.json()

# weather_data = response.json()["list"][0]["weather"][0]["id"]

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain today. Remember to bring an ☂️umbrella",
    from_="+13613219026",
    to="+14379819563",
    )
    
    print(message.status)
