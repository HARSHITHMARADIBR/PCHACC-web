import streamlit as st

from Home_page import home_process
from CTA_Fort import Chitradurga_fort
from Chandravalli import chandravalli_details
from Rangayyana import rangayyana_baagilu
from uchanngi import uchhangellamma_temple
from maramma import maramma_temple
from barageramma import barageramma_temple
from muruga import murugha_mata
from Study_area import study_area
from proposal import proposal

def user_process():
    # Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Routing
    if st.session_state.page == "home":
        home_process()
    elif st.session_state.page == "Cta_fort":
        Chitradurga_fort()
    elif st.session_state.page == "Chandravalli":
        chandravalli_details()
    elif st.session_state.page == "Rangayyana":
        rangayyana_baagilu()
    elif st.session_state.page == "Uchhangellamma":
        uchhangellamma_temple()
    elif st.session_state.page == "Maramma":
        maramma_temple()
    elif st.session_state.page == "Barageramma":
        barageramma_temple()
    elif st.session_state.page == "Murugha":
        murugha_mata()
    elif st.session_state.page == "study_area":
        study_area()
    elif st.session_state.page == "proposal":
        proposal()
    else:
        st.warning("Page not found!")
