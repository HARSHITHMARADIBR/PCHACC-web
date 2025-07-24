import base64
import streamlit as st
from PIL import Image as PILImage

def rangayyana_baagilu():
    st.title("Rangayyana Baagilu")
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()
    
    st.write('''Rangayyana Bagilu is a prominent location within Chitradurga Fort, specifically one of the fort's main gates. It's a well-known landmark in the area, even serving as the address for businesses in the Chitradurga HO (Chitradurga Head Office) region. The gate is a significant part of the fort's history and architecture. ''')
    st.write('''Location: 6CC3+99J, Doddapete Main Rd, Chickpet, Chitradurga, Karnataka 577501.''')
    st.write('Coordinates: 14.2152° N, 76.3953° E')
    st.write('''This is part of the outer fortifications. It is named after Nirthadi Ranganatha, the family deity of the Nayakas of Chitradurga. It appears to have been originally built in the last days of Vijayanagara and is ornamented with sculptures of Gandabherunda, Ganesa and other deities. The fort wall on either side (height about7.5 m) is made of large finely dressed blocks of granite and was a formidable obstacle to the enemy. A museum maintained by the Commissionerate of Archaeology and Museums; Govt of Karnataka is located near this gateway
''')
    
    ran1=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0009.jpg"
    with open(ran1, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Landuse Map of Rangayyana Baagilu***")

    ran2=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0019.jpg"
    with open(ran2, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Landuse Table of Rangayyana Baagilu***")

    ran3=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0023.jpg"
    with open(ran3, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Factors affecting in Rangayyana Baagilu***")

    from PIL import Image as PILImage  # Add this at the top if not already present

    p1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\Rangayyana Baagilu.png"
    p2 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0035.jpg"
    p3 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0020.jpg"

    # Create 3 columns
    col1, col2, col3 = st.columns(3)

    # Display images with proper container width (updated parameter)
    with col1:
        st.image(PILImage.open(p1), caption="Rangayyana Baagilu", use_container_width=True)
    with col2:
        st.image(PILImage.open(p2), caption="Road width", use_container_width=True)
    with col3:
        st.image(PILImage.open(p3), caption="Providing oneway", use_container_width=True)


