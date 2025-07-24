import streamlit as st
from Home_page import home_process
from CTA_Fort import Chitradurga_fort
from Chandravalli import chandravalli_details
from Rangayyana import rangayyana_baagilu
from uchanngi import uchhangellamma_temple
from maramma import maramma_temple
from barageramma import barageramma_temple  # Fixed import
from muruga import murugha_mata
from Study_area import study_area
from proposal import proposal

def user_process():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    page = st.session_state.page
    if page == "home":
        home_process()
    elif page == "Cta_fort":
        Chitradurga_fort()
    elif page == "Chandravalli":
        chandravalli_details()
    elif page == "Rangayyana":
        rangayyana_baagilu()
    elif page == "Uchhangellamma":
        uchhangellamma_temple()
    elif page == "Maramma":
        maramma_temple()
    elif page == "Barageramma":
        barageramma_temple()  # Now correctly mapped
    elif page == "Murugha":
        murugha_mata()
    elif page == "study_area":
        study_area()
    elif page == "proposal":
        proposal()
    else:
        st.warning("Page not found!")
