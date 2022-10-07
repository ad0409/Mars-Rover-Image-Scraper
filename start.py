import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Replace DEMO_KEY below with your own key if you generated one.
api_key = "DEMO_KEY"
earth_date = "2022-10-01"


query_params = {"api_key": api_key, "earth_date": earth_date}
response = requests.get(endpoint, params=query_params)
print(response)
response.json()
photos = response.json()["photos"]
print(f"Found {len(photos)} photos")

for i in range(0, len(photos)):
    print(photos[i]["img_src"])


#print(photos[1]["img_src"])