import streamlit as st
from db import add_user, login_user, view_all_users

st.set_page_config(page_title="Login System", layout="centered")

st.title("🔐 MySQL-Based Login System")

menu = st.sidebar.selectbox("Choose an option", ["Login", "Register", "View Users"])

if menu == "Register":
    st.subheader("Create Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        add_user(username, password)
        st.success("User registered successfully!")

elif menu == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        result = login_user(username, password)
        if result:
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid credentials.")

elif menu == "View Users":
    st.subheader("👮 Admin Panel")
    admin_user = st.text_input("Admin Username")
    admin_pass = st.text_input("Admin Password", type="password")
    if st.button("Admin Login"):
        if admin_user == "admin" and admin_pass == "admin123":
            users = view_all_users()
            for i, user in enumerate(users, 1):
                st.write(f"{i}. Username: {user[0]} | Password: {user[1]}")
        else:
            st.error("Wrong Admin Credentials")

            
            
            
    
  
  
  
  