import streamlit as st
import base64
from PIL import Image as PILImage

def murugha_mata():
    st.title("Murugha Mata")
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()

       
    st.write('''Sri Murugha Mata (Museum, Hindu temple, Park): ''')
    st.write('''Coordinates: 14°14'12.5"N 76°22'37.6"E
69PG+PR9, NH-4, Kavadigarahatti Layout, Chitradurga, Karnataka 577502, India ''')
    st.write('''Area : 17.59 Ha (43.46 acres) ''')
    st.write('''The first Murugha Rajendra Mutha at Chitradurga was built on the Chinmuladri hills by Palegar Bichugatti Bharamanna Nayaka. Later it was shifted to the present muth in 1703 AD which is situated at the left side of Chitradurga-Davanagere road near M.K.Hatti.
Now the 27th Pontiff of the order Sri Shivamurthy Murugha Rajendra Sharanaru prerides over the Muth.
Sri Jagadguru Murugharajendra Vidyapeetha, was established in 1964. It was founded by His Holiness Jagadguru Sri Sri Mallikarjua Murugharajendra Mahaswamiji, the then pontiff of the mutt. The mutt's purpose is to provide education and cultural institutions to the common people in rural and remote areas, particularly those in Chitradurga. 
 ''')
    
    muru1=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0015.jpg"
    with open(muru1, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Landuse Map of Murugha Mata***")

    muru2=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0030.jpg"
    with open(muru2, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Landuse Table of Murugha Mata***")

    muru3=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0033.jpg"
    with open(muru3, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Factors affecting in Murugha Mata***")

    p1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\muruga mutt.jpg"
    p2 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0010.jpg"
    p3 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0034.jpg"

    # Create 3 columns
    col1, col2 , col3 = st.columns(3)

    # Display images with same width in each column
    with col1:
        st.image(PILImage.open(p1), caption="Murugha Mata", use_container_width=True)
    with col2:
        st.image(PILImage.open(p2), caption="Proposed Entry & Exit gate", use_container_width=True)
    with col3:
        st.image(PILImage.open(p3), caption="Growth of aquatic plants", use_container_width=True)
    