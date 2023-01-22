import requests
import os
import unixtimestamp as ts
import useful as use
from flask import Flask,request

app = Flask(__name__, static_url_path='/static')

#testing purposes
#city = input("Enter a city: ").capitalize()

# Construct the API endpoint URL
api_key = f"{os.environ.get('WEATHER_API')}"


def longLat(city):
  # Set the API endpoint and any desired parameters
  api_endpoint = "https://api.openweathermap.org/geo/1.0/direct"
  params = {"q": city, "appid": api_key}
  # Make the API call and get the response
  response = requests.get(api_endpoint, params=params)

  # Parse the response to get the latitude and longitude for the city
  location = response.json()[0]
  lat = location["lat"]
  lon = location["lon"]
  return lat, lon


def weatherTomorrow(city):
  lat, lon = longLat(city)

  api_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
  params = {"lat": lat, "lon": lon, "exclude": "hourly", "appid": api_key}
  response = requests.get(api_endpoint, params=params)
  debugDate, debugTime = ts.unixConvert(response.json()["daily"][1]['dt'],
                                        "both")
  lowTemp = response.json()["daily"][1]['temp']['min']
  lowTemp = round(lowTemp * (9 / 5) - 459.67)
  highTemp = response.json()["daily"][1]['temp']['max']
  highTemp = round(highTemp * (9 / 5) - 459.67)
  weatherCondition = response.json(
  )["daily"][1]['weather'][0]['description'].title()
  sunrise = ts.unixConvert(response.json()["daily"][0]['sunrise'], "time")
  sunset = ts.unixConvert(response.json()["daily"][0]['sunset'], "time")

  #print(f"Tomorrow's date in {city} is {debugDate}")
  low = f"Tomorrow's low temperature in <span class='red'>{city}</span> is {round(lowTemp)}°F"
  high = f"Tomorrow's high temperature in <span class='red'>{city}</span> is {round(highTemp)}°F"
  condition = f"Tomorrow's expected conditions in <span class='red'>{city}</span> is {weatherCondition}"
  sunrise_tom = f"Tomorrow's sunrise in <span class='red'>{city}</span> is at {sunrise}"
  sunset_tom = f"Tomorrow's sunset in <span class='red'>{city}</span> is at {sunset}"
  return low, high, condition, sunrise_tom, sunset_tom

def tempNow(city):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
  response = requests.get(url)

  forecast = response.json()

  # Print the current temperature in Fahrenheit
  current_temperature = forecast["list"][0]["main"]["temp"]
  current_temperature_f = round(current_temperature * (9 / 5) - 459.67)
  return f"The current temperature in <span class='red'>{city}</span> is {current_temperature_f}°F"
  


@app.route("/")
def index():
  page = ""
  with open("index.html") as f:
    page = f.read()
  return page


@app.route("/weather", methods=['GET'])
def weather():
  city = request.args.get("city").capitalize()
  current_temp = tempNow(city)
  low,high,condition,sunrise,sunset = weatherTomorrow(city)
  page = ""
  content = ""
  with open("weather.html", "r") as f:
    page = f.read()
  with open("content.html", "r") as f:
    content = f.read()
  content = content.replace("{current_temp}", current_temp)
  content = content.replace("{low}", low)
  content = content.replace("{high}", high)
  content = content.replace("{condition}", condition)
  content = content.replace("{sunrise}", sunrise)
  content = content.replace("{sunset}", sunset)
  page = page.replace("{city}", city)
  page = page.replace("{content}", content)
  return page


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)

#if __name__ == "__main__":
#    tempNow(city)
#    print()
#    weatherTomorrow(city)
