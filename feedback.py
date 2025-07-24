import streamlit as st


def feedback():
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
        st.experimental_rerun()
    st.title("Feedback")