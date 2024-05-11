import streamlit as st
from datetime import datetime
from os import path


def display_as_webpage(title: str, description: str, image_url: str) -> None:
    """
    Display the passed info on a streamlit webpage

    :param title: title of the image
    :param description: a description of the image
    :param image_url: url of an image or video
    :return:
    """
    st.set_page_config(layout='wide')

    st.header(title)

    # Download the image to the "image files" folder.
    # Name it yyyy-mm-dd-{url filename} (using current date)
    today = datetime.today().strftime('%Y-%m-%d')
    image_path = f"image files/{today}-{path.basename(image_url)}"
    st.image(image_path)

    st.write(description)

    return
