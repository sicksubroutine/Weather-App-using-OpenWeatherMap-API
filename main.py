import requests
import os
import unixtimestamp as ts
import useful as use

city = input("Enter a city: ").capitalize()

# Construct the API endpoint URL
api_key = f"{os.environ.get('WEATHER_API')}"

def longLat(city):
    # Set the API endpoint and any desired parameters
    api_endpoint = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city,
        "appid": api_key
    }
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
    params = {
        "lat": lat,
        "lon": lon,
        "exclude": "hourly",
        "appid": api_key
    }
    response = requests.get(api_endpoint, params=params)
    debugDate, debugTime = ts.unixConvert(response.json()["daily"][1]['dt'], "both")
    lowTemp = response.json()["daily"][1]['temp']['min']
    lowTemp = round(lowTemp * (9 / 5) - 459.67)
    highTemp = response.json()["daily"][1]['temp']['max']
    highTemp = round(highTemp * (9 / 5) - 459.67)
    weatherCondition = response.json()["daily"][1]['weather'][0]['description'].title()
    sunrise = ts.unixConvert(response.json()["daily"][0]['sunrise'], "time")
    sunset = ts.unixConvert(response.json()["daily"][0]['sunset'], "time")

    print(f"Tomorrow's date in {use.cConvert('red')}{city}{use.cConvert(None)} is {debugDate}")
    print(f"Tomorrow's high temperature in {use.cConvert('red')}{city}{use.cConvert(None)} is {round(highTemp)}°F")
    print(f"Tomorrow's low temperature in {use.cConvert('red')}{city}{use.cConvert(None)} is {round(lowTemp)}°F")
    print(f"Tomorrow's expected conditions in {use.cConvert('red')}{city}{use.cConvert(None)} is {weatherCondition}")

    print(f"Tomorrow's sunrise in {use.cConvert('red')}{city}{use.cConvert(None)} is at {sunrise}")
    print(f"Tomorrow's sunset in {use.cConvert('red')}{city}{use.cConvert(None)} is at {sunset}")

def tempNow(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)

    forecast = response.json()

    # Print the current temperature in Fahrenheit
    current_temperature = forecast["list"][0]["main"]["temp"]
    current_temperature_f = round(current_temperature * (9 / 5) - 459.67)
    print(f"The current temperature in {use.cConvert('red')}{city}{use.cConvert(None)} is {current_temperature_f}°F")



if __name__ == "__main__":
    tempNow = tempNow(city)
    print()
    weatherTomorrow(city)