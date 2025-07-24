import base64
import streamlit as st

def study_area():
    if st.sidebar.button("Home"):
       st.session_state.page = "home"
       st.rerun()
    st.title("STUDY AREA")
    cta_map=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\WhatsApp Image 2025-07-01 at 14.33.51_73550ff3.jpg"
    with open(cta_map, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="500" style="margin-right:100px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("***Key Map of Chitradurga***")    
    demography_details=r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0016.jpg"
    with open(demography_details, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="400" height="250" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Demographic Details***")


    st.write('''Chitradurga is located at 14.23°N 76.4°E. City area is of 62 sq km and rural area is of 1350.76 sq km. It has an average elevation of 732 metres (2401 ft). Chitradurga city is well connected to Bangalore, Mysore, Mangalore, Davanagere, Hubli, Hospet, Bellary, Shimoga, Tumkur, Bijapur, Belgaum by road and through railways it is  200 km (124.3 mi) from Bangalore. Chitradurga railway line is connected to main line at Chikkajajur Bangalore/Mysore – Arasikere broad gauge railway line. in the heart of the Deccan Plateau, Chitradurga is recognized as the land of valour and chivalry. The district headquarters town, Chitradurga owes its name to “Chitrakaladurga,” or “Picturesque castle”. This is a massive fortress on top of granite hills that rises dramatically from the ground. Archaeological remains found in the area, trace its history to the 3rd millennium B.C.''')
    
    Base_Map = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\basemap.jpg"
    with open(Base_Map, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="500" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Base Map***")

    Land_Use_Map = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\landusemap.jpg"
    with open(Land_Use_Map, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="500" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Land Use Map***")

    # LPA Map (FIXED)
    LPA_map = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\lpamap.jpg"
    with open(LPA_map, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="500" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Local Planning Area***")