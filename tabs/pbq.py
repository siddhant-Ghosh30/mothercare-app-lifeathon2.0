import streamlit as st
from datetime import datetime
from db import get_connection

def show_pbq():
    st.header("Perinatal Bonding Questionnaire (PBQ)")

    questions = [
        "I feel close to my baby",
        "I wish the old days when I had no baby would come back",
        "I feel distant from my baby",
        "I love to cuddle my baby",
        "I regret having this baby",
        "The baby doesn't seem to be mine",
        "My baby winds me up",
        "I love my baby to bits",
        "I feel happy when my baby smiles or laughs",
        "My baby irritates me",
        "I enjoy playing with my baby",
        "My baby cries too much",
        "I feel trapped as a mother",
        "I feel angry with my baby",
        "I resent my baby",
        "My baby is the most beautiful baby in the world",
        "I wish my baby would somehow go away",
        "I have done harmful things to my baby",
        "My baby makes me feel anxious",
        "I am afraid of my baby",
        "My baby annoys me",
        "I feel confident when caring for my baby",
        "I feel the only solution is for someone else to look after my baby",
        "I feel like hurting my baby",
        "My baby is easily comforted"
    ]

    options = ["Always", "Very often", "Quite often", "Sometimes", "Rarely", "Never"]

    score_mapping = [
        [0, 1, 2, 3, 4, 5],  # Q1 – positive
        [5, 4, 3, 2, 1, 0],  # Q2 – negative
        [5, 4, 3, 2, 1, 0],  # Q3 – negative
        [0, 1, 2, 3, 4, 5],  # Q4 – positive
        [5, 4, 3, 2, 1, 0],  # Q5 – negative
        [5, 4, 3, 2, 1, 0],  # Q6 – negative
        [5, 4, 3, 2, 1, 0],  # Q7 – negative
        [0, 1, 2, 3, 4, 5],  # Q8 – positive
        [0, 1, 2, 3, 4, 5],  # Q9 – positive
        [5, 4, 3, 2, 1, 0],  # Q10 – negative
        [0, 1, 2, 3, 4, 5],  # Q11 – positive
        [5, 4, 3, 2, 1, 0],  # Q12 – negative
        [5, 4, 3, 2, 1, 0],  # Q13 – negative
        [5, 4, 3, 2, 1, 0],  # Q14 – negative
        [5, 4, 3, 2, 1, 0],  # Q15 – negative
        [0, 1, 2, 3, 4, 5],  # Q16 – positive
        [5, 4, 3, 2, 1, 0],  # Q17 – negative
        [5, 4, 3, 2, 1, 0],  # Q18 – negative
        [5, 4, 3, 2, 1, 0],  # Q19 – negative
        [5, 4, 3, 2, 1, 0],  # Q20 – negative
        [5, 4, 3, 2, 1, 0],  # Q21 – negative
        [0, 1, 2, 3, 4, 5],  # Q22 – positive
        [5, 4, 3, 2, 1, 0],  # Q23 – negative
        [5, 4, 3, 2, 1, 0],  # Q24 – negative
        [0, 1, 2, 3, 4, 5]   # Q25 – positive
    ]

    responses = []
    for i, question in enumerate(questions):
        responses.append(st.radio(question, options, key=f"pbq_q{i}"))

    if st.button("Submit PBQ"):
        total_score = 0
        q_scores = []

        # Fixed scoring logic
        for i, answer in enumerate(responses):
            score_index = options.index(answer)
            score = score_mapping[i][score_index]
            total_score += score
            q_scores.append(score)

        # Interpretation
        if total_score >= 26:
            interpretation = "Warning: Your score indicates a higher risk of impaired bonding. Please consult your healthcare provider."
        else:
            interpretation = "Your bonding appears to be within the typical range."

        # Save to database
        email = st.session_state.user_email
        today = datetime.now().date().isoformat()
        
        con = get_connection()
        con.execute("""
            INSERT INTO pbq_results (email, date, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
                                   q11, q12, q13, q14, q15, q16, q17, q18, q19, q20,
                                   q21, q22, q23, q24, q25, total_score, interpretation)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (email, today, *q_scores, total_score, interpretation))
        con.close()

        st.write(f"**Your total score is: {total_score}**")

        if total_score >= 26:
            st.error("⚠️ " + interpretation + " You may call a service provider by contacting any of the referrals from the referrals tab.")
        else:
            st.success(interpretation)
            
        st.success("Results saved successfully!")