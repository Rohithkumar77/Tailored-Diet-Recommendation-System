import streamlit as st
import sqlite3
import hashlib

# Create a SQLite database to store user information
def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                  (username TEXT PRIMARY KEY, password TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Hash a password for secure storage
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Check if a user exists in the database
def user_exists(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result is not None

# Check if a user's password matches in the database
def check_password(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    conn.commit()
    stored_password = c.fetchone()
    conn.close()
    if stored_password:
        return stored_password[0] == hash_password(password)
    return False

# Add a new user to the database
def add_user(username, password, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                (username, hash_password(password), email))
    conn.commit()
    conn.close()

# Create a session state variable to track logged-in users
if "user" not in st.session_state:
    st.session_state["user"] = None

create_database()

st.title("User Authentication")

# Display login and signup tabs
tab_names = ["Login", "Sign Up"]
selected_tab = st.radio("Select an action:", tab_names)

if selected_tab == "Sign Up":
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if username and email and password and confirm_password:  # Check if all fields are filled out
            if password == confirm_password:
                if not user_exists(username):
                    add_user(username, password, email)
                    st.success("User created successfully!")
                else:
                    st.warning("Username already exists!")
            else:
                st.warning("Passwords do not match!")
        else:
            st.warning("All fields are required!")  # Warn the user if any field is empty

if selected_tab == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if username and password:  # Check if both fields are filled out
            if user_exists(username) and check_password(username, password):
                st.success("Logged in as {}".format(username))
                st.session_state["user"] = username
            else:
                st.warning("Invalid username or password!")
        else:
            st.warning("Both fields are required!")  # Warn the user if any field is empty
