import streamlit as st
import pandas as pd
from datetime import datetime
from db import get_connection

def show_mood_sleep_logs():
    st.header("Mood & Sleep Logs")
    
    email = st.session_state.user_email #get email of logged in user

    # form to log today's mood and sleep
    with st.form("mood_sleep_form"):
        st.write("Log your mood and sleep for today:")
        mood = st.slider(
            "Rate your mood today (1 = Very Low, 10 = Excellent):", 
            min_value=1, 
            max_value=10, 
            value=5,  # Default to middle
            step=1
        )
        sleep_hours = st.number_input(
            "Hours of sleep:", 
            min_value=0.0, 
            max_value=24.0, 
            value=8.0, 
            step=0.5
        )

        submitted = st.form_submit_button("Submit Log")

        if submitted:
            con = get_connection()
            today = datetime.now().date().isoformat()
            # Check if entry for today already exists
            existing = con.execute("SELECT * FROM mood_sleep_logs WHERE email = ? AND date = ?", (email, today)).fetchone()
            if existing:
                # Update existing entry
                con.execute("""
                    UPDATE mood_sleep_logs 
                    SET mood_score = ?, sleep_hours = ? 
                    WHERE email = ? AND date = ?
                """, (mood, sleep_hours, email, today))
                st.success("Today's log updated successfully!")
            else:
                # Insert new entry
                con.execute("""
                    INSERT INTO mood_sleep_logs (email, date, mood_score, sleep_hours) 
                    VALUES (?, ?, ?, ?)
                """, (email, today, mood, sleep_hours))
                st.success("Log submitted successfully!")
            con.close()
            st.rerun()

    # Display past logs
    # Button to view past entries
    if st.button("View Past Entries"):
        st.subheader("Your Past Logs")
        con = get_connection()
        rows = con.execute("SELECT date, mood_score, sleep_hours FROM mood_sleep_logs WHERE email = ? ORDER BY date DESC", (email,)).fetchall()
        con.close()
        if rows:
            df = pd.DataFrame(rows, columns=["Date", "Mood Score", "Sleep Hours"])
            st.dataframe(df)
        else:
            st.info("You have not logged any entries yet.")


