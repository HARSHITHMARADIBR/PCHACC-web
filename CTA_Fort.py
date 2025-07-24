import base64
import streamlit as st
from PIL import Image

def Chitradurga_fort():
    st.title("🏰 Chitradurga Fort")
    
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.rerun()

    st.write('''Fort Precincts :- 
The Nayak Palegars Built The Fort As An Impregnable Fortification For Defense Purposes With Seven Walls (Yelusuttinakote) 19 Gateways, 38 Posterior Entrances, 35 Secret Entrances, Four Invisible Passages, Water Tanks And 2000 Watch Towers. The Total Length Of The Fort Walls Is About 8 Kilometres (5.0 Mi) And Covers An Area Of About 1,500 Acres (610 Ha). 

Temples In The Fort :- 
18 Temples Were Built In The Upper Fort. The Prominent Ones Are Ekanatheswari, Hidimbeswara, Sampige Siddeshwara, Ekanathamma, Phalguneshwara, Gopala Krishna, Lord Hanuman, Subbaraya And Nandi, And In The Lower Fort Uchchangiamma Temple Is Situated.
Other Structures
•	Rainwater-harvesting Structures Were Built In A Cascade Development
•	'Maddu Bisuva Kallu,’ Constructed During Hyder Ali Rule
•	Chitradurga Fort Visiting Time: Chitradurga Fort Is Open From 6 AM To 6 PM 
•	Tourism: The Fort Is Managed By Archeological Survey Of India. 
	Location Of Fort: Chitradurga, Karnataka. Coordinates : 14.2152°n 76.3953°e
''')

    # ✅ Display Map
    Cta_Map = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0007.jpg"
    with open(Cta_Map, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"<img src='data:image/jpeg;base64,{encoded_image}' width='700'>",
        unsafe_allow_html=True
    )
    st.markdown("***Land Use Map Of Chitradurga Fort***") 

    # ✅ Display Table 1
    Table1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0008.jpg"

    with open(Table1, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"<img src='data:image/jpeg;base64,{encoded_image}' width='700'>",
        unsafe_allow_html=True
    )
    st.markdown("***Land Use Table Of Chitradurga Fort***") 

    # ✅ Display Table 2
    table2 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0021.jpg"
    with open(table2, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"<img src='data:image/jpeg;base64,{encoded_image}' width='700'>",
        unsafe_allow_html=True
    )
    st.markdown("***Factors Affecting Chitradurga Fort***") 

    # ✅ Display Photo Gallery
        # ✅ Display Photo Gallery
    pic1 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0037.jpg"
    pic2 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0024.jpg"
    pic3 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0011.jpg"
    pic4 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0027.jpg"
    pic5 = r"C:\Users\harshith maradi b r\Documents\Downloads\Prohibited\web streamlit\personal finance tracker\personal finance tracker\images\IMG-20250703-WA0042.jpg"

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(Image.open(pic1), caption="Breakage of fort wall near prison", use_container_width=True)
    with col2:
        st.image(Image.open(pic2), caption="Growth of weeds on Fort wall", use_container_width=True)
    with col3:
        st.image(Image.open(pic3), caption="Dumping of solid waste near prison", use_container_width=True)
    with col4:
        st.image(Image.open(pic4), caption="Construction of Obavva Grave using cement", use_container_width=True)
    with col5:
        st.image(Image.open(pic5), caption="Fort front view covered by encroached houses", use_container_width=True)

