import streamlit as st
import base64
from PIL import Image as PILImage

def barageramma_temple():
    st.title("Barageramma Temple")
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()

    
    st.write('''Barageramma Temple (Hindu temple), Coordinates: 14°13'07.2"N 76°23'18.6"E 699Q+F99, Davalagiri Bhadavane 1st Phase, Kavadigarahatti Layout, Chitradurga, Karnataka 577501, India
 ''')
    
    bara1=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0041.jpg"
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

    bara2=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0050.jpg"
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

    bara3=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0017.jpg"
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

    p1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\baregeramma temple.jpeg.jpg"
    p2 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0039.jpg"
    # Create 3 columns
    col1, col2 = st.columns(2)

    # Display images with same width in each column
    with col1:
        st.image(PILImage.open(p1), caption="Barageramma Temple", use_container_width=True)
    with col2:
        st.image(PILImage.open(p2), caption="Direction of water flow", use_container_width=True)
    