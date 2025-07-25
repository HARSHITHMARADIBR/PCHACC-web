import base64
import streamlit as st
from PIL import Image as PILImage

def uchhangellamma_temple():
    st.title("Uchhangellamma Temple")

    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()

    st.write('''Uchchangellamma Temple is an important religious site located in the Chitradurga Fort complex. The temple is dedicated to Uchchangellamma, the family deity of the Nayakas of Chitradurga, who ruled the region during the post-Vijayanagar period.''')
    st.write('''Location: Chitradurga Fort Complex, Chitradurga, Karnataka 577501''')
    st.write('Coordinates: 14.2220° N, 76.3999° E')
    st.write('''The temple stands as a testimony to the cultural and spiritual heritage of the region. Its traditional architecture and religious significance attract both tourists and devotees alike.''')

    # Image 1
    img1 = "images/IMG-20250703-WA0044.jpg"
    try:
        with open(img1, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <h1 style="display: flex; align-items: center;">
                <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
            </h1>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning(f"Image not found: {img1}")

    st.markdown("***Landuse Map of Uchhangellamma Temple***")

    # Image 2
    img2 = "images/IMG-20250703-WA0022.jpg"
    try:
        with open(img2, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <h1 style="display: flex; align-items: center;">
                <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
            </h1>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning(f"Image not found: {img2}")

    st.markdown("***Landuse Table of Uchhangellamma Temple***")

    # Image 3
    img3 = "images/IMG-20250703-WA0017.jpg"
    try:
        with open(img3, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <h1 style="display: flex; align-items: center;">
                <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
            </h1>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning(f"Image not found: {img3}")

    st.markdown("***Factors affecting Uchhangellamma Temple Area***")

    # Grid Images
    p1 = "images/Uchhangellamma_Temple.png"
    p2 = "images/IMG-20250703-WA0039.jpg"

    col1, col2 = st.columns(2)

    try:
    st.image(PILImage.open(p1), caption="Barageramma Temple", use_container_width=True)
except FileNotFoundError:
    st.warning(f"Missing image file: {p1}")

    try:
        with col2:
            st.image(PILImage.open(p2), caption="Pedestrian Movement", use_container_width=True)
    except FileNotFoundError:
        with col2:
            st.warning(f"Missing: {p2}")
