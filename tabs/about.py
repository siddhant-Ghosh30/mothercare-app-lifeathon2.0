import streamlit as st

def show_about():
    st.header("About Mother Care")

    st.write("""
    **Mother Care** is a mental health app designed specifically for postpartum women in India.

    ➤ The postpartum period — the first year after childbirth — can be a challenging time, with mental health concerns affecting up to 80% of new mothers. Many of these problems go undiagnosed or are dismissed as normal.

    ➤ This app aims to support mothers by:
    - Tracking mood and sleep patterns
    - Offering coping strategies and stress management techniques
    - Screening for depression, anxiety, and suicidal risk
    - Providing referrals to mental health professionals
    - Convenient & Private Support

    ➤ Why is this important?
    - Poor maternal mental health can affect the emotional development of the child and the stability of the family.
    - Traveling for care can be difficult with an infant; this app provides support from the comfort of home.
    - Many existing apps are designed for Western audiences; this app is tailored to the needs and cultural context of Indian mothers.

    ➤ Our goal is to help ensure the well-being of mothers, infants, and families, contributing to healthier communities and supporting sustainable development.

    """)

    st.info("""
    **Designed & Developed by:**\n
    Siddhant Ghosh, BTech CSE(AI), MIT Bengaluru\n
    **Under the guidance of:**\n
     Dr. Soumyalatha Naveen, Assistant Professor - Senior Scale, SOCE, MIT Bengaluru
""")

# if __name__ == "__main__":
#     show_about()

