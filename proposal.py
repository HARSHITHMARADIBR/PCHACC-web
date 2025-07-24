import base64
import streamlit as st

def proposal():
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()
        
    st.title("PROPOSALS")
    st.write('''GUIDELINES: As and when any unauthorized construction is reported in prohibited or regulated area, ASI initiates action as per provisions of the Ancient Monuments and Archaeological Sites and Remains Act, 1958 (AMASR Act, 1958).''')
    st.write('''As per the existing rule position, [section 20A of the AMASR Act, 1958, stipulates that an area extending to 100 meters from the protected limit is prohibited area] and [section 20B of the AMASR Act, 1958 stipulate that an area extending to 200 meters from the prohibited limit is regulated area].''')
    st.write("""
-  **No construction** (including government or public works) is permitted in the **prohibited area** of centrally protected monuments and areas.

- **Repairs and renovations** of existing buildings/structures within the **prohibited area** (if constructed **before the Amendment**) are **permissible**.

-  **Reconstruction is not allowed** for existing buildings that are **in a dilapidated condition** and located in the **prohibited area**.

-  **Construction, reconstruction, repair, or renovation** is allowed in the **regulated area**, **with permission** from the **Competent Authority**.

-  To undertake **any construction or renovation** (in either **prohibited** or **regulated** areas), an application must be submitted to the **Competent Authority**.

-  The **Competent Authority** will review the application and act based on the **recommendation of the National Monument Authority** — either **granting** or **rejecting** the request.
""")

    st.subheader("VISION")
    st.write("""
    To conserve and develop heritage areas without impacting their integrity, such as the cultural, architectural, and environmental heritage of Chitradurga City.
    """)

    st.subheader("MISSION")
    st.write("""
    - To safeguard historical landmarks such as **Chitradurga Fort**, **Chandravalli**, **Murugha Matta**, and heritage temples through structured conservation efforts.

    - To formulate inclusive policies that integrate heritage conservation with **urban planning**, **infrastructure**, and **tourism development**.

    - To provide **1137 houses free of cost**, including all basic facilities. Each house will be 20x30 sq ft in a total area of **6.33 hectares**, designated for both **residential** and **commercial** use.

    - The land under government possession near **Ingaldalu Village** beside the National Highway (Survey No: 79, **128.91538041 hectares**) will be used to **relocate people** currently living in **prohibited heritage zones** in Chitradurga City.
    """)

    Pro1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0040.jpg"
    with open(Pro1, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="500" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Proposed Rehabilitation Site ***")

    Pro2 =r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0049.jpg"
    with open(Pro2, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="500" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Major locations from Proposed Site***")
    
    Pro3 =r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0012.jpg"
    with open(Pro3, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="400" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Details of Encroachment***")

    st.subheader("SITE ANALYSIS OF LAYOUT")
    st.write("""
    - Total Area: 128.91538041 Hectors
             
    - Coordinates: 14°11'11.5"N 76°27'26.3"E or 5FP4+JW8 Ingaladal, Karnataka 
             
    - Connectivity: Banglore-Mumbai National Highway passes Infront the site area, 8.7Km from Chitradurga govt Bus stand, 12.1Km from Railway Station
             
    - Climatic Condition: Temperature is usually normal, Wind direction is from North-East to South-West, Sun Path follows East to West       
             
    - Vegetation: Vegetation can be seen on the north and south Western and South Western region
    """)

    Pro4 =r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\Ingaldallayoutdesign.jpg"
    with open(Pro4, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="600" height="800" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Layout Design of 79 Survey number***")

    Pro5 =r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\Screenshot 2025-07-22 201450.png"
    with open(Pro5, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="400" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Landuse Analysis***")

    Pro6 =r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\landuse Analysis chart.png"
    with open(Pro6, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="600" height="500" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Landuse Analysis chart***")

    Pro7 =r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\plot analysis table.png"
    with open(Pro7, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="700" height="450" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Plot Analysis***")

    Pro8 =r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\Plot Analysis chart.png"
    with open(Pro8, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <h1 style="display: flex; align-items: center;">
            <img src="data:image/jpeg;base64,{encoded_image}" width="600" height="550" style="margin-right:50px;">
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("***Plot Analysis chart***")