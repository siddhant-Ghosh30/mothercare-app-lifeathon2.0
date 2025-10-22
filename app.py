import streamlit as st
import hashlib
from db import get_connection

st.set_page_config(page_title="Mother Care", page_icon="👩‍⚕️", layout="centered", initial_sidebar_state="collapsed")

# initialize session states for login tracking
if 'login_state' not in st.session_state:
    st.session_state.login_state = None # None, 'admin', or 'user'
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'username' not in st.session_state:
    st.session_state.username = "" # for admin
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_age' not in st.session_state:
    st.session_state.user_age = None

st.title("Mother Care")
st.image("mothercare_logo.png")

# if logged in as admin, show admin interface
if st.session_state.login_state == 'admin':
    import admin
    admin.show_admin()

# if logged in as user, show user interface
elif st.session_state.login_state == 'user' and st.session_state.logged_in:
    import user_dashboard
    user_dashboard.show_user_dashboard()

# if not logged in, show login/signup options
else:
    option = st.radio ("Login as:", ["User", "Admin (For Healthcare Providers)"])

    if option == "User":
        st.subheader("User Access")
        user_option = st.radio("Select option:", ["New User", "Existing User"])

        if user_option == "New User":
            st.subheader("User Registration")
            with st.form("new_user_form"):
                name = st.text_input("Name")
                email = st.text_input("Email")
                age = st.number_input("Age", min_value=13, max_value=120, value= 25, step=1)
                # password = st.text_input("Password", type="password") 
                submitted = st.form_submit_button("Create Account")
                
                if submitted:
                    con = get_connection()
                    existing = con.execute("SELECT email FROM users WHERE email = ?", (email,)).fetchone()
                    if existing:
                        st.error("User with this email already exists.")
                    else:
                        # password_hash = hashlib.sha256(password.encode()).hexdigest()
                        con.execute("INSERT INTO users (email, name, age) VALUES (?, ?, ?)", (email, name, age))
                        con.close()
                        st.success("Account created successfully. Please log in.")
                        # st.rerun()

        elif user_option == "Existing User":
            with st.form("existing_user_form"):
                name = st.text_input("Name")
                email = st.text_input("Email")
                # password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Login")
                if submitted:
                    con = get_connection()
                    result = con.execute("SELECT name, age FROM users WHERE email = ?", (email,)).fetchone()
                    con.close()
                    if result != None and result[0] == name:
                        st.session_state.user_age = result[1]
                        st.session_state.logged_in = True
                        st.session_state.login_state = 'user'
                        st.session_state.user_email = email
                        st.session_state.user_name = name
                        st.success("Logged in successfully.")
                        st.rerun()
                    else:
                        st.error("Invalid credentials. Please try again or create a new account if you are not registered.")
                    

    elif option == "Admin (For Healthcare Providers)":
        st.subheader("Admin Login")
        with st.form("admin_login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")

            if submitted:
                con = get_connection()
                result = con.execute("SELECT password_hash FROM admin WHERE username = ?", (username,)).fetchone()
                con.close()
                if result != None and hashlib.sha256(password.encode()).hexdigest() == result[0]:
                    st.session_state.logged_in = True
                    st.session_state.login_state = 'admin'
                    st.session_state.username = username
                    st.success("Logged in successfully as admin.")
                    st.rerun()
                else:
                    st.error("Invalid admin credentials. Please try again.")
        
