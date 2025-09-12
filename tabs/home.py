import streamlit as st
import pandas as pd
from db import get_connection

def show_home():
    st.header("Home")
    st.write("Here you can see an overview of your mood and sleep patterns.")

    email = st.session_state.user_email #get email of logged in user

    con = get_connection() #connect to db

    # Fetch mood logs
    mood_data = con.execute("SELECT date, mood FROM mood_sleep_logs WHERE email = ? ORDER BY date", (email,)).fetchall()
    mood_df = pd.DataFrame(mood_data, columns = ["Date", "Mood"])

    # Fetch sleep logs
    sleep_data = con.execute("SELECT date, sleep_hours FROM mood_sleep_logs WHERE email = ? ORDER BY date", (email,)).fetchall()
    sleep_df = pd.DataFrame(sleep_data, columns = ["Date", "Sleep Hours"])

    con.close() #close db connection

    # display mood graph and average mood
    if not mood_df.empty:
        st.subheader("Mood Over Time")
        mood_df = mood_df.set_index("Date")
        st.line_chart(mood_df)

        avg_mood = mood_df["Mood"].mean()
        st.metric("Average Mood", f"{avg_mood:.2f}")

    else:
        st.info("No mood logs found. Please add your mood entries.")

    # display sleep graph and average sleep hours
    if not sleep_df.empty:
        st.subheader("Sleep Hours Over Time")
        sleep_df = sleep_df.set_index("Date")
        st.line_chart(sleep_df)

        avg_sleep = sleep_df["Sleep Hours"].mean()
        st.metric("Average Sleep Hours", f"{avg_sleep:.1f}")
    else:
        st.info("No sleep logs found. Please add your sleep entries.")

