import base64
import streamlit as st
from PIL import Image as PILImage

def murugha_mata():
    st.title("Murugha Matha, Chitradurga")

    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()

    st.write("""
    Murugha Matha is a prominent religious and spiritual institution in Chitradurga,
    known for its social and educational contributions.
    """)

    st.write("**Location:** Chitradurga, Karnataka")
    st.write("**Coordinates:** 14.2300° N, 76.4000° E")

    # Display main image
    img = "images/IMG-20250703-WA0015.jpg"
    try:
        with open(img, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        st.markdown(
            f'<img src="data:image/jpeg;base64,{encoded}" width="500">',
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning(f"Image not found: {img}")
    img2 = "images/IMG-20250703-WA0030.jpg"
    try:
        with open(img2, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        st.markdown(
            f'<img src="data:image/jpeg;base64,{encoded}" width="500">',
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning(f"Image not found: {img}")

    img3 = "images/IMG-20250703-WA0033.jpg"
    try:
        with open(img3, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        st.markdown(
            f'<img src="data:image/jpeg;base64,{encoded}" width="500">',
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning(f"Image not found: {img}")

    st.markdown("***Key Highlights***")
    st.markdown("""
    - Major center of Lingayat faith in Karnataka  
    - Known for community services, education, and spiritual activities  
    - Historic lineage and significant influence in regional culture  
    """)

    st.markdown("***Recent Status***")
    st.write("""
    The Matha remains active and influential, with ongoing programs in education and rural development.
    """)

    # Optional additional images
    p1 = "images/murugha_event1.jpg"
    p2 = "images/murugha_event2.jpg"
    p3 = "images/murugha_event3.jpg"

    col1, col2, col3 = st.columns(3)
    for img_path, col in zip([p1, p2, p3], [col1, col2, col3]):
        try:
            with col:
                st.image(PILImage.open(img_path), caption=img_path.split("/")[-1], use_container_width=True)
        except FileNotFoundError:
            with col:
                st.warning(f"Missing image: {img_path}")
