import requests
from twilio.rest import Client

# set up Twilio
account_sid = "AC6ba5227ca44116b544f1d1c1853d24e4"
auth_token = "2914397e3d86644ff82b3a820e545511"

# set up weather API
parameters = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": "fddcd340d82612566556d12698645c74",
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
        from_='+18446950021',
        body="It's going to rain today!",
        to='[Phone Number]'
    )
    print(message.status)


