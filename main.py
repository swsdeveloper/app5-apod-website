import requests

# See: https://api.nasa.gov/

api_key = "cahYHylcDQUMEtgApySiOdpiPy7P0gOn4GE8b9M2"

# Query Parameters:
# date=2024-05-11  (omitting this parameter defaults to today's date)
# api_key=

url = "https://api.nasa.gov/planetary/apod" \
      f"?api_key={api_key}"

response = requests.get(url)
apod_dict = response.json()

# print(apod_dict)
# for key, value in apod_dict.items():
#     print(f"{key}: {value}")

print(apod_dict["title"])
print(apod_dict["hdurl"])
print(apod_dict["explanation"])
