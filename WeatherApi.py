import requests
from twilio.rest import Client

''' Twilio account details'''
# Your Account Sid and Auth Token from twilio.com/console
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

callFrom = ""
callTo = ""


api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=197b0d6b83b6c2fc19f75a10da3af9ae&zip=95136'

json_data = requests.get(api_address).json()
wDescription = json_data['weather'][0]['description']


temp1 = json_data['main']['temp']
tempLow = json_data['main']['temp_min']
tempHigh = json_data['main']['temp_max']

tempF = temp1 * 9/5 - 459.67
tempL = tempLow * 9/5 - 459.67
tempH = tempHigh * 9/5 - 459.67

tempFah = int(tempF)
tempLow = int(tempL)
tempHigh = int(tempH)
# --------------
rain_answer = str(wDescription).lower()

# This section is just for printing weather info to the console.
print("The weather in Santa Clara is: ")
print("\t-Rain Prediction: ")
if "rain" in rain_answer:
    print("\t\tIt's going to rain")
    rain_answer = "rain"
else:
    print("\t\tNo rain today")
print("\t-Current Temp: " + str(int(tempF)))
print("\t-High Temp: " + str(int(tempHigh)))
print("\t-Low Temp: " + str(int(tempLow)))


# Below is the texting part of the program.
# Frost warning text
"""
if tempLow < 32:
    message = client.messages \
        .create(
        body='Frost Warning \n\t-Drive Slow\n\t-Cover Plants',
        from_= callFrom,
        to= callTo,
    )

# Rain warning text
if rain_answer == 'rain':
    message = client.messages \
        .create(
        body='There is a chance of rain today',
        from_= callFrom,
        to = callTo,
    )
"""