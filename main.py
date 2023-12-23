import requests
from twilio.rest import Client
import os

# set up Twilio
account_sid = os.environ.get("SID")
auth_token = os.environ.get("AUTH_TOKEN")

# set up weather API
parameters = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": os.environ.get("APP_ID"),
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

will_rain = False
for hour in data["list"]:
    condition_code = hour["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="[Phone Number]",
        body="It's going to rain today!",
        to="[Phone Number]"
    )
    print(message.status)


