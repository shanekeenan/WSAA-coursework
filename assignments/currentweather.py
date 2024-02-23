 
# Assignment from Topic02 Representing Data. 
'''
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

# Author: Shane Keenan 
# date: 03/02/2024  
# status: Ongoing 

import requests
import json

# change coordinates to Mace Head weather station in Carna 
url = "https://api.open-meteo.com/v1/forecast?latitude=53.326&longitude=-9.9&current=temperature_2m&wind_direction_10m"
response = requests.get(url)

#print(response.json())
data = response.json()
#with open("weather.json", "w") as cso_json:
#    json.dump(data, cso_json, indent = 4) # using the indent agrument formats the .json file.. avoids having to use shift+alt+f 

temp = data["current"]["temperature_2m"]

print(f'Current temperature at Mace Head: {temp:.2f}°C' )

#####################################################

# additional section to display wind direction 


