import base64
import streamlit as st
from PIL import Image as PILImage  # ✅ Correct import

def chandravalli_details():
    st.title("Chandravalli Area")

    # Navigation button
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()

    # --- History and Location ---
    st.markdown("""
    ### 🏛️ **History of Chandravalli**

    1. Settlements that are around 3000 years old. Lead coins of the Satavahanas, Roman silver coins and ornaments of gold, silver and copper were discovered here.  
    2. Dams were built as early as 4th century AD by Kadamba ruler Mayura Sharma.  
    3. 1284 AD: Panchalinga (Five Lingas) cave in the Ankhi Matha area.  
    4. Bhairaveshvara Temple and Paradeshappa Caves: Seven caves formed centuries ago, inside the hill.  

    ### 📍 **Location of Chandravalli**

    - Chitradurga, Karnataka, India  
    - **Coordinates**: 14°12′32″N 76°23′10″E  
    - **Area**: 53.3 Ha (132 Acres)  
    - **Size**: 730m × 730m (2,400 ft × 2,400 ft)
    """)

    # --- Image 1: Landuse Map ---
    cndrv_map = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0047.jpg"
    with open(cndrv_map, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="700">
    """, unsafe_allow_html=True)
    st.markdown("***Landuse Map of Chandravalli***")

    # --- Image 2: Landuse Table ---
    tablec1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0013.jpg"
    with open(tablec1, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="250">
    """, unsafe_allow_html=True)
    st.markdown("***Landuse Table of Chandravalli***")

    # --- Image 3: Factors Affecting ---
    tablec2 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0026.jpg"
    with open(tablec2, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="250">
    """, unsafe_allow_html=True)
    st.markdown("***Factors Affecting in Chandravalli***")

    # --- Grid of 4 Images ---
    p1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\chandravalli.jpeg.jpg"
    p2 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0032.jpg"
    p3 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0014.jpg"
    p4 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0031.jpg"

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(PILImage.open(p1), caption="Chandravalli Lake", use_container_width=True)
    with col2:
        st.image(PILImage.open(p2), caption="Broken Shivalinga", use_container_width=True)
    with col3:
        st.image(PILImage.open(p3), caption="Cave Markings", use_container_width=True)
    with col4:
        st.image(PILImage.open(p4), caption="Bear Incident", use_container_width=True)
