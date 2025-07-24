import streamlit as st
import base64
from PIL import Image as PILImage

def maramma_temple():
    st.title("Maramma Temple")
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()
    
    st.write('''Maramma Temple (Hindu temple), Coordinates: 14°13'18.3"N 76°23'04.5"E
69CM+PR4, Nehru Nagar, Chitradurga, Karnataka 577501, India
 ''')
    
    mara1=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0018.jpg"
    with open(mara1, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Landuse Map of Maramma Temple***")

    mara2=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0028.jpg"
    with open(mara2, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Landuse Table of Maramma Temple***")

    mafra3=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0038.jpg"
    with open(mafra3, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Factors affecting in Maramma Temple***")

    p1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0036.jpg"
    p2 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0025.jpg"

    # Create 3 columns
    col1, col2 = st.columns(2)

    # Display images with same width in each column
    with col1:
        st.image(PILImage.open(p1), caption="Reduced Road Width", use_container_width=True)
    with col2:
        st.image(PILImage.open(p2), caption="Proposed Flyover", use_container_width=True)
    