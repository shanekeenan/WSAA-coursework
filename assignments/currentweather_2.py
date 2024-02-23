

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
