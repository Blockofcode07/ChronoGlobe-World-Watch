import streamlit as st
from datetime import datetime
import pytz
import time


# Country time zone mapping
timezones = {
    "India 🇮🇳": "Asia/Kolkata",
    "Finland 🇫🇮": "Europe/Helsinki",
    "Estonia 🇪🇪": "Europe/Tallinn",
    "Latvia 🇱🇻": "Europe/Riga",
    "Lithuania 🇱🇹": "Europe/Vilnius"
}


# Streamlit Page Configuration and Title
st.set_page_config(page_title="🌍 ChronoGloabe -Live World Clock", layout="centered")


for country, tz_name in timezones.items():
    tz = pytz.timezone(tz_name)
    current_time = datetime.now(tz).strftime("%A, %d %B %Y | %I:%M:%S %p")
    st.write(f"**{country}**: {current_time}")