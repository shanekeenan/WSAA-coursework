 
# Assignment from Topic02 Representing Data
# Author: Shane Keenan 
# date: 03/02/2024  
# status: complete 

'''
Assignment Description 

Opened: Tuesday, 9 January 2024, 3:45 AM
Due: Monday, 29 April 2024, 4:45 AM

Assignment 
Using the URL below
https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
Write a python program called currentweather.py that will print out the current temperature on the console (and only the temperature)
I have set the lat/long to my location, you may use that or a different location.
Last few marks:
Look at the documentation (below) and print out the current wind direction (10m) as well.
🌤️ Free Open-Source Weather API | Open-Meteo.com
Create a repository called WSAA-assignments, save the file in there and copy a link to it to here (please only put a link to the repo in here other information can be in the readme)
''' 
import requests
import json
# change coordinates to Mace Head MET Eireann weather station in Carna 
url = "https://api.open-meteo.com/v1/forecast?latitude=53.326&longitude=-9.9&current=temperature_2m&wind_direction_10m"
response = requests.get(url)

#print(response.json())
data = response.json()
temp = data["current"]["temperature_2m"]
print(f'Current temperature at Mace Head: {temp:.2f}°C' )

#####################################################
print('\n\nMET data from Mace Head')

# additional section to display wind direction - i've also added in wind speed and gusts 
# code available from their website: https://open-meteo.com/en/docs/
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 53.326,
    "longitude": -9.9,
	"current": ["temperature_2m", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
	"hourly": "temperature_2m",
	"timezone": "GMT"
}
responses = openmeteo.weather_api(url, params=params)
# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
# Current values. The order of variables needs to be the same as requested.
current = response.Current()
current_temperature_2m = current.Variables(0).Value()
current_wind_speed_10m = current.Variables(1).Value()
current_wind_direction_10m = current.Variables(2).Value()
current_wind_gusts_10m = current.Variables(3).Value()
print(f"Current temperature_2m: {current_temperature_2m:.2f}°C")
print(f"Current wind_direction_10m: {current_wind_direction_10m:.2f}°")
print(f"Current wind_speed_10m: {current_wind_speed_10m:.2f} km/h")
print(f"Current wind_gusts_10m: {current_wind_gusts_10m:.2f} km/h")

