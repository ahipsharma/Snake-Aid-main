import streamlit as st
import time
import numpy as np
import time

import json
import requests
import time
import requests
import streamlit as st

from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title('Snake Aid')
animation_1 = lottie_url_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_qoo3cyxi.json")
# lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
# lottie_hello = load_lottieurl(lottie_url_hello)
# lottie_download = load_lottieurl(lottie_url_download)
st_lottie(animation_1, speed=1, loop=True, quality="medium", width=200)


# st_lottie(lottie_url_hello, key="hello")

# if st.button("Download"):
#     with st_lottie_spinner(lottie_download, key="download"):
#         time.sleep(5)
#     st.balloons()



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2016/06/02/02/38/mesh-1430108_960_720.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    file = st.file_uploader("Choose your image")


add_bg_from_url() 

