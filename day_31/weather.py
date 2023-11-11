from twilio.rest import Client
import os
from dotenv import load_dotenv
import requests

load_dotenv()

LAT = 27.73
LON = 85.31

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

response = requests.get(
    f"https://api.weatherbit.io/v2.0/current?lat={LAT}&lon={LON}&key={WEATHER_API_KEY}")
response.raise_for_status()
result = response.json()

city = result["data"][0]["city_name"]
weather_code = result["data"][0]["weather"]["code"]

if weather_code <= 600:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
                    .create(
                        body=f"Make sure to take an umbrella! It is going to rain today on {city}☔☔☔!\n - Trishan Rainforecaster",
                        from_='+16514336310',
                        to='+9779749419407'
                    )

    print(message.status)
else:
    print(f"It won't rain today on {city}!")
