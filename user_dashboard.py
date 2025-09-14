import streamlit as st
from tabs.home import show_home
from tabs.mood_sleep import show_mood_sleep_logs
from tabs.screening_tests import show_screening_tests
from tabs.coping_cards import show_coping_cards
from tabs.references import show_references
from tabs.about import show_about

def show_user_dashboard():
    if "logged_in" not in st.session_state or not st.session_state.logged_in or st.session_state.login_state != "user":
        st.error("Access denied. Please log in as a user.")
        st.stop()

    st.title(f"Hey {st.session_state.user_name}, welcome to your dashboard!")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "Mood & Sleep Logs", "Screening Tests", "Coping Cards", "References", "About"])

    with tab1:
        show_home()

    with tab2:
        show_mood_sleep_logs()

    with tab3:
        show_screening_tests()

    with tab4:
        show_coping_cards()

    with tab5:
        show_references()
    
    with tab6:
        show_about()



