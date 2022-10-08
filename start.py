import requests
import urllib.request
import os

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Replace DEMO_KEY below with your own key if you generated one.
api_key = "DEMO_KEY"
earth_date = "2022-10-07"
query_params = {"api_key": api_key, "earth_date": earth_date}
response = requests.get(endpoint, params=query_params)
photos = response.json()["photos"]


def set_api(endpoint, api_key, earth_date):
    query_params = {"api_key": api_key, "earth_date": earth_date}
    response = requests.get(endpoint, params=query_params)
    print(response)
    response.json()
    photos = response.json()["photos"]
    print(f"Found {len(photos)} photos")


def store_data(earth_date):
    print(os.getcwd())

    if os.path.exists(os.getcwd() + "\\" + "Mars Rover Picture Sets"):
        os.chdir(os.getcwd() + "\\" + "Mars Rover Picture Sets")
    else:
        os.mkdir(os.getcwd() + "\\" + "Mars Rover Picture Sets")
        os.chdir(os.getcwd() + "\\" + "Mars Rover Picture Sets")

    os.mkdir(earth_date)
    os.chdir(os.getcwd() + "\\" + earth_date)
    # for i in range(0, len(photos)):
    for i in range(0, 5):
        print(photos[i]["img_src"])
        jpg_web_link = photos[i]["img_src"]
        picture_name = "Picture " + str(i) + ".jpg"
        urllib.request.urlretrieve(jpg_web_link, picture_name)
    print(os.getcwd())


set_api(endpoint, api_key, earth_date)
store_data(earth_date)
