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


# Title with HTML + CSS styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: #2c3e50;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        .footer {
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            bottom: 0;
            width: 100vw;
            padding: 10px 0;
            background-color: #f0f2f6;
            text-align: center;
            font-size: 0.85em;
            color: #6c757d;
        }
    </style>
    <div class="title">🕒 Live World Clock</div>
    <div class="subtitle">Get current date and time for India, Finland, Estonia, Latvia, and Lithuania</div>
""", unsafe_allow_html=True)

# Placeholder for clock updates
placeholder = st.empty()


# Main clock loop
while True:
    with placeholder.container():
        st.markdown("### 📅 Date and Time by Country")
        for country, tz_name in timezones.items():
            tz = pytz.timezone(tz_name)
            current_time = datetime.now(tz).strftime("%A, %d %B %Y | %I:%M:%S %p")
            st.write(f"**{country}**: {current_time}")
    
        # Footer
        st.markdown("""
            <div class="footer">
                 Created by <strong>Aditya Jawanjal</strong> | Version <strong>0.1.0</strong>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(1)
