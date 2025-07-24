import streamlit as st
from PIL import Image
import base64

from Chandravalli import chandravalli_details 
from CTA_Fort import Chitradurga_fort

def home_process():
    # Sidebar navigation
    page = st.sidebar.selectbox(
        "Select options",
        ["Home", "Study Area", "Proposal"]
    )

    if page == "Study Area":
        st.session_state.page = "study_area"
        st.rerun()
    elif page == "Proposal":
        st.session_state.page = "proposal"

    # ✅ FIXED: Correct image path
    image_path = "images/Logo.jpg"  # Make sure this file exists in your repo

    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.warning("Logo image not found. Please check 'images/Logo.jpg'")
        encoded_image = None

    if encoded_image:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center;">
                <h1 style="display: flex; align-items: center;">
                    <img src="data:image/jpeg;base64,{encoded_image}" width="40" style="margin-right:10px;">
                    PCHACC
                </h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "<div style='text-align:center; font-size:24px; font-weight:bold;'>PLANNING FOR CONSERVATION OF HERITAGE AREAS IN CHITRADURGA CITY</div>",
        unsafe_allow_html=True
    )

    st.subheader("AIM")
    st.write("Aim of the study is to Plan and Conserve the heritage Areas in Chitradurga city.")

    st.subheader("OBJECTIVES")
    st.write("""
    1. To study the chronological growth and development of Chitradurga city.  
    2. To identify and study the characteristics of the heritage places in Chitradurga City.  
    3. To analyse the factors affecting the heritage places in Chitradurga city.  
    4. To propose heritage conservation plan and policy guidelines for Chitradurga city.
    """)

    option1 = st.selectbox("**SELECT HERITAGE SITES**", [
        "-- Select --", 
        "Archaeological Survey Of India", 
        "State Department of Archaeology", 
        "Local Authority",
        "Private Organization"
    ])

    if option1 == "Archaeological Survey Of India":
        option2 = st.selectbox("Select Site", ["-- Select --", "Chitradurga Fort", "Chandravalli"])
        if option2 == "Chitradurga Fort":
            st.session_state.page = "Cta_fort"
            st.rerun()
        elif option2 == "Chandravalli":
            st.session_state.page = "Chandravalli"
            st.rerun()

    elif option1 == "State Department of Archaeology":
        option2 = st.selectbox("Select Site", ["-- Select --", "Rangayyana Baagilu", "Uchhangellamma Temple"])
        if option2 == "Rangayyana Baagilu":
            st.session_state.page = "Rangayyana"
            st.rerun()
        elif option2 == "Uchhangellamma Temple":
            st.session_state.page = "Uchhangellamma"
            st.rerun()

    elif option1 == "Local Authority":
        option2 = st.selectbox("Select site", ["-- Select --", "Maramma Temple", "Barageramma Temple"])
        if option2 == "Maramma Temple":
            st.session_state.page = "Maramma"
            st.rerun()
        elif option2 == "Barageramma Temple":
            st.session_state.page = "Barageramma"
            st.rerun()

    elif option1 == "Private Organization":
        option2 = st.selectbox("Select site", ["-- Select --", "Murugha Mata"])
        if option2 == "Murugha Mata":
            st.session_state.page = "Murugha"
            st.rerun()
