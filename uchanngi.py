import streamlit as st
import base64
from PIL import Image as PILImage

def uchhangellamma_temple():
    st.title("Ucchangellamma Temple")
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()

    st.write('''Shri Ucchangi Devi Devasthana (Hindu temple) ''')
    st.write('''Coordinates: 14°13'13.2"N 76°23'57.3"E''')
    st.write('Address : 69CX+4MQ, Doddapete Main Rd, Chickpet, Chitradurga, Karnataka 577501, India The Uchangi Yellamma temple is located in Chitra city, Chitradurga district.')
    st.write('''It is located on the way to Fort in Chikkapete. Yellamma popularly known as Renuka Yellamma is powerful deity in the town and this temple is facing east direction which has various mandapams. This temple was constructed in Vijayanagar style of architecture. This temple was constructed by Madakari Nayaka dynasty and believed to be their goddess.
''')
    
    uchn1=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0044.jpg"
    with open(uchn1, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Landuse Map of Ucchangellamma Temple***")

    uchn2=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0022.jpg"
    with open(uchn2, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Landuse Table of Ucchangellamma Temple***")

    uchn3=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0048.jpg"
    with open(uchn3, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Factors affecting in Ucchangellamma Temple***")

    p1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\uchhangellamma temple.png"
    p2 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0029.jpg"

    # Create 3 columns
    col1, col2 = st.columns(2)

    # Display images with same width in each column
    with col1:
        st.image(PILImage.open(p1), caption="Ucchangellamma Temple", use_container_width=True)
    with col2:
        st.image(PILImage.open(p2), caption="Providing Traffic signal", use_container_width=True)
    