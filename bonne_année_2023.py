import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
import emoji

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.write(emoji.emojize("""# Bonne et heureuse année 2023"""))
st.header("A toute la famille PEM")
st.write("by Tony Porsché")

lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_cwJmjdcvDK.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",

    height=None,
    width=None,
    key=None,
)
st.balloons()



