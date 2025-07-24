import streamlit as st 
import json
import os

from User import user_process

USER_FILE = "users1.json"

# -------- JSON Helpers --------
def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as f:
            json.dump({}, f)

    with open(USER_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Fix for empty or corrupted file
            return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# -------- Authentication --------
def login(username, password):
    users = load_users()
    if username in users and users[username]['password'] == password:
        return True
    return False

def signup(username, password, email):
    users = load_users()
    if username in users:
        return False
    users[username] = {'password': password, 'email': email}
    save_users(users)
    return True

# -------- Main Menu Navigation --------
def mains_menu():
    st.sidebar.title("Navigation")
    st.sidebar.success(f"Logged in as: {st.session_state.username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    user_process()

# -------- App Entry Point --------
def main():
    st.set_page_config(page_title="PLANNING FOR CONSERVATION OF HERITAGE AREAS IN CHITRADURGA CITY", layout="centered")

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""

    if st.session_state.logged_in:
        mains_menu()
        return

    # Login / Signup UI
    st.title("🔐 Login / Sign Up Page")
    choice = st.sidebar.selectbox("Select Option", ["Login", "Sign Up"])

    if choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid username or password.")

    elif choice == "Sign Up":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_email = st.text_input("Email")
        new_pass = st.text_input("Password", type="password")

        def is_valid_email(email):
            import re
            pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            return re.match(pattern, email) is not None  

        if st.button("Sign Up"):
            if not new_user or not new_email or not new_pass:
                st.warning("⚠️ All fields are required.")
            elif not is_valid_email(new_email):
                st.error("❌ Please enter a valid email address.")
            elif signup(new_user, new_pass, new_email):
                st.success("✅ Account created successfully! Please log in.")
            else:
                st.warning("⚠️ Username already taken.")

if __name__ == '__main__':
    main()
