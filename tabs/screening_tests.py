import streamlit as st
from tabs.edps import show_edps   
from tabs.pbq import show_pbq     

def show_screening_tests():
    st.header("Screening Tests")

    tab1, tab2 = st.tabs(["EPDS test", "PBQ test"])

    with tab1:
        show_edps()

    with tab2:
        show_pbq()