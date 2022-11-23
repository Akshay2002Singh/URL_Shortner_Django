# importing modules
import requests
import json

# define access token in headers
headers = {
    'Authorization': 'Bearer {TOKEN}',
    'Content-Type': 'application/json',
}

# url that needs to be shorted
url = "https://www.geeksforgeeks.org/how-to-split-data-into-training-and-testing-in-python-without-sklearn/"

data_dict = { "long_url": url, "domain": "bit.ly"}

# convert data_dict to json
data = json.dumps(data_dict)

# getting response which will be in json string 
response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

# convert json string to dict
response_dict = json.loads(response.text)

# Print new shorten url 
print(f"Short URL = {response_dict['link']}")