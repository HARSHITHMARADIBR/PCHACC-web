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

    # Display main image
    img = "images/barageramma_main.jpg"
    try:
        with open(img, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        st.markdown(
            f'<img src="data:image/jpeg;base64,{encoded}" width="500">',
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning(f"Image not found: {img}")

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
    p1 = "images/barageramma_factor1.jpg"
    p2 = "images/barageramma_factor2.jpg"
    p3 = "images/barageramma_factor3.jpg"

    col1, col2, col3 = st.columns(3)
    for img_path, col in zip([p1, p2, p3], [col1, col2, col3]):
        try:
            with col:
                st.image(PILImage.open(img_path), caption=img_path.split("/")[-1], use_container_width=True)
        except FileNotFoundError:
            with col:
                st.warning(f"Missing image: {img_path}")
