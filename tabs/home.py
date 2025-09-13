import streamlit as st
import pandas as pd
from db import get_connection

def show_home():
    st.header("Home")
    st.write("Here you can see an overview of your mood and sleep patterns.")

    email = st.session_state.user_email #get email of logged in user

    con = get_connection() #connect to DB
    rows = con.execute("SELECT date, mood_score, sleep_hours FROM mood_sleep_logs WHERE email = ? ORDER BY date ASC LIMIT 7", (email,)).fetchall()
    con.close()
    
    if rows:
        df = pd.DataFrame(rows, columns=["Date", "Mood Score", "Sleep Hours"])
        df["Date"] = pd.to_datetime(df["Date"]) # convert date column to datetime

        # mood over time graph
        st.subheader("Mood over the past week")
        mood_chart = df.set_index("Date")["Mood Score"]
        st.line_chart(mood_chart)

        # sleep over time graph
        st.subheader("Sleep Hours over the past week")
        sleep_chart = df.set_index("Date")["Sleep Hours"]
        st.line_chart(sleep_chart)

        # Averages 
        avg_mood = df["Mood Score"].mean()
        avg_sleep = df["Sleep Hours"].mean()

        col1, col2 = st.columns(2)
        col1.metric(f"Average Mood" , f"{avg_mood:.2f} / 10")
        col2.metric(f"Average Sleep", f"{avg_sleep:.2f} hours")

    else:
        st.info("It looks like you haven't logged any mood or sleep data yet. Start tracking today in the 'Mood & Sleep Logs' tab!")


    