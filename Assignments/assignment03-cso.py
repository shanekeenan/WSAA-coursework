# assignment 3 
# Author: Shane Keenan 
# date: 18/11/2023 
# status: complete

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(url)
#print(response.status_code)

print(response.text)

data = json.loads(response.text)
with open("cso.json", "w") as cso_json:
    json.dump(data, cso_json, indent = 4) # using the indent agrument formats the .json file.. avoids having to use shift+alt+f 



