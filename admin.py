import streamlit as st
import pandas as pd
from db import get_connection

def show_admin():
    if "logged_in" not in st.session_state or not st.session_state.logged_in or st.session_state.login_state != "admin":
        st.error("Access denied. Please log in as admin.")
        st.stop()

    st.title("Admin Dashboard")
    st.write("Welcome, you have full access to the database for demonstration purposes.")

    # logout in sidebar
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.login_state = None
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("Logged out successfully.")
        st.rerun()

    # Connect to DuckDB
    con = get_connection()

    # Get list of tables in DuckDB
    tables = con.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='main'").fetchall()
    tables = [t[0] for t in tables]

    st.subheader("Available Tables")
    st.write(f"Found {len(tables)} tables in the database.")

    for table in tables:
        st.markdown(f"### {table}")
        df = pd.read_sql_query(f"SELECT * FROM {table}", con)
        st.dataframe(df)

    con.close()
