import base64
import streamlit as st
from PIL import Image as PILImage

def barageramma_temple():
    st.title("Barageramma Temple")

    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()

    st.write("""
    Barageramma Temple is a traditional shrine managed by the local authority in Chitradurga.
    It is dedicated to the deity Barageramma and plays a key role during annual festivals.
    """)

    st.write("**Location:** Chitradurga City, Karnataka")
    st.write("**Coordinates:** 14.2230° N, 76.3980° E")

    bara1="images/IMG-20250703-WA0041.jpg"
    with open(bara1, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Landuse Map of Barageramma Temple***")
    
    bara2="images/IMG-20250703-WA0050.jpg"
    with open(bara2, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Landuse Table of Barageramma Temple***")

    bara3="images/IMG-20250703-WA0017.jpg"
    with open(bara3, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Factors affecting in Barageramma Temple***")

    # Display main image


    st.markdown("***Heritage Site Details***")
    st.markdown("""
    - Maintained by local municipal authorities  
    - Hosts annual festivals attended by hundreds of devotees  
    - Known for its traditional Dravidian architecture  
    """)

    st.markdown("***Current Status & Concerns***")
    st.write("""
    While the temple remains active and structurally sound, it requires periodic renovation and proper crowd management during festivals.
    """)

    # Display additional factor images in columns
    p1 = "images/baregeramma temple.jpeg.jpg"
    p2 = "images/IMG-20250703-WA0039.jpg"

    col1, col2 = st.columns(2)
    for img_path, col in zip([p1, p2], [col1, col2]):
        try:
            with col:
                st.image(PILImage.open(img_path), caption=img_path.split("/")[-1], use_container_width=True)
        except FileNotFoundError:
            with col:
                st.warning(f"Missing image: {img_path}")
