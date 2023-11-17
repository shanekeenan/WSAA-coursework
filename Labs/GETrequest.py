

import requests
import json

url = "http://www.githup.com"
response = requests.get(url)
print(response.status_code)



#if response.status_code == 200: 
#    page_content = response.text

    #print(page_content)



#data = response.json()
#with open ("bitcoindump.json", "w") as fp:
#    json.dump(data, fp)

#euroPriceObject = data["bpi"]["EUR"]
#rate = euroPriceObject["rate"]
#print(rate)