import streamlit as st
from datetime import datetime
from db import get_connection

def show_edps():
    st.header("Edinburgh Postnatal Depression Scale (EPDS)")

    questions = [
        {
            "question": "I have been able to laugh and see the funny side of things.",
            "options": ["As much as I always could", "Not quite so much now", "Definitely not so much now", "Not at all"],
            "scores": [0, 1, 2, 3]
        },
        {
            "question": "I have looked forward with enjoyment to things",
            "options": ["As much as I ever did", "Rather less than I used to", "Definitely less than I used to", "Hardly at all"],
            "scores": [0, 1, 2, 3]
        },
        {
            "question": "I have blamed myself unnecessarily when things went wrong",
            "options": ["Yes, most of the time", "Yes, some of the time", "Not very often", "No, never"],
            "scores": [3, 2, 1, 0]
        },
        {
            "question": "I have been anxious or worried for no good reason",
            "options": ["No, not at all", "Hardly ever", "Yes, sometimes", "Yes, very often"],
            "scores": [0, 1, 2, 3]
        },
        {
            "question": "I have felt scared or panicky for no very good reason",
            "options": ["Yes, quite a lot", "Yes, sometimes", "Not very often", "No, not at all"],
            "scores": [3, 2, 1, 0]
        },
        {
            "question": "Things have been getting on top of me",
            "options": ["Yes, most of the time I haven't been able to cope", "Yes, sometimes I haven't been coping", "No, most of the time I have coped quite well", "No, I have been coping as well as ever"],
            "scores": [3, 2, 1, 0]
        },
        {
            "question": "I have been so unhappy that I have had difficulty sleeping",
            "options": ["Yes, most of the time", "Yes, sometimes", "Not very often", "No, not at all"],
            "scores": [3, 2, 1, 0]
        },
        {
            "question": "I have felt sad or miserable",
            "options": ["Yes, most of the time", "Yes, quite often", "Not very often", "No, not at all"],
            "scores": [3, 2, 1, 0]
        },
        {
            "question": "I have been so unhappy that I have been crying",
            "options": ["Yes, most of the time", "Yes, quite often", "Only occasionally", "No, never"],
            "scores": [3, 2, 1, 0]
        },
        {
            "question": "The thought of harming myself has occurred to me",
            "options": ["Yes, quite often", "Sometimes", "Hardly ever", "Never"],
            "scores": [3, 2, 1, 0]
        }
    ]

    responses = []

    # Render each question with its options
    for i, q in enumerate(questions):
        answer = st.radio(q["question"], q["options"], key=f"epds_q{i}")
        responses.append((q, answer))

    if st.button("Submit EPDS"):
        total_score = 0
        q_scores = []
        harmful_thoughts_score = 0

    for i, (q, answer) in enumerate(responses):
        score_index = q["options"].index(answer)
        score = q["scores"][score_index]
        total_score += score
        q_scores.append(score)
        if i == 9:  # Last question
            harmful_thoughts_score = score

    # Create base interpretation based on total score
    if total_score < 8:
        base_interpretation = "Score below 8: Depression not likely. Continue support and self-care."
        alert_type = "success"
    elif total_score <= 11:
        base_interpretation = "Score between 8 - 11: Depression possible. Support is recommended, re-screen in 2–4 weeks."
        alert_type = "warning"
    elif total_score <= 13:
        base_interpretation = "Score between 11 - 13: Fairly high possibility of depression. Monitor and support."
        alert_type = "warning"
    else:
        base_interpretation = "Score above 13: Probable depression. Diagnostic assessment recommended."
        alert_type = "error"

    # Add harmful thoughts warning if present
    if harmful_thoughts_score >= 1:
        interpretation = f"⚠️ CRITICAL: Thoughts of harming yourself are present. Please seek professional help immediately.\n\nAdditional Assessment: {base_interpretation}"
        alert_type = "error"  # Override to error for any harmful thoughts
    else:
        interpretation = base_interpretation

    # Save to database
    email = st.session_state.user_email
    today = datetime.now().date().isoformat()
    
    con = get_connection()
    con.execute("""
        INSERT INTO edps_results (email, date, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, total_score, interpretation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (email, today, *q_scores, total_score, interpretation))
    con.close()

    st.write(f"**Your total score is: {total_score}**")

    # Display appropriate alert
    if alert_type == "error":
        st.error(interpretation + " You can contact any Hospital from the referred list in the references tab.")
    elif alert_type == "warning":
        st.warning(interpretation)
    else:
        st.success(interpretation)
        
    st.success("Results saved successfully!")