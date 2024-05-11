import requests

# See: https://api.nasa.gov/ and https://github.com/nasa/apod-api

api_key = "cahYHylcDQUMEtgApySiOdpiPy7P0gOn4GE8b9M2"

# Query Parameters:
# date=2024-05-11  (omitting this parameter defaults to today's date)
# api_key=

url = "https://api.nasa.gov/planetary/apod" \
      "?date=2024-05-10" \
      f"&api_key={api_key}"

response = requests.get(url)
apod_dict = response.json()

# print(apod_dict)
# for key, value in apod_dict.items():
#     print(f"{key}: {value}")

title = apod_dict["title"]
description = apod_dict["explanation"]

if "hdurl" in apod_dict.keys():
    image_url = apod_dict["hdurl"]  # only for media_type = 'image'
else:
    image_url = apod_dict["url"]    # for media_type 'image' and 'video'

print(title)
print(description)
print(image_url)
