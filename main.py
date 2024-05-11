import streamlit as st
import requests
from datetime import datetime
from os import path
from website import display_webpage

st.set_page_config(layout='wide')

# See: https://api.nasa.gov/ and https://github.com/nasa/apod-api

api_key = "cahYHylcDQUMEtgApySiOdpiPy7P0gOn4GE8b9M2"

# Query Parameters:
# date=2024-05-11  (omitting this parameter defaults to today's date)
# api_key=

url = "https://api.nasa.gov/planetary/apod" \
      f"?api_key={api_key}"

response = requests.get(url)
apod_dict = response.json()

title = apod_dict["title"]
description = apod_dict["explanation"]

media_type = apod_dict["media_type"]

if "hdurl" in apod_dict.keys():
    image_url = apod_dict["hdurl"]  # only for media_type = 'image'
else:
    image_url = apod_dict["url"]    # for media_type 'image' and 'video'

# Download the image to the "image files" folder.
# Name it yyyy-mm-dd-{url filename} (using current date)
if media_type == "image":
    today = datetime.today().strftime('%Y-%m-%d')
    image_path = f"image files/{today}-{path.basename(image_url)}"
    image_response = requests.get(image_url)
    image = image_response.content
    with open(image_path, 'wb') as file:
        file.write(image)
else:  # "video"
    image_path = image_url

display_webpage(title, description, image_path, media_type)
