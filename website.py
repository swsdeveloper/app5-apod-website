import streamlit as st
from datetime import datetime


def display_webpage(title: str, description: str, image_path: str, media_type: str) -> None:
    """
    Display the passed info on a streamlit webpage

    :param title: title of the image
    :param description: a description of the image
    :param image_path: path to a downloaded image or url of a video
    :param media_type: either 'image' or 'video'
    :return:
    """
    page_date = ":blue[" + datetime.today().strftime('%b %d, %Y') + "]"
    st.header(page_date)

    page_title = "NASA's Astronomy Image of the Day"
    st.title(page_title)

    st.header(title)

    if media_type == "image":
        st.image(image_path)  # should point to a file
    else:
        st.video(image_path)  # should be a url

    st.write(description)

    return
