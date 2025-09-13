import streamlit as st

def show_references():
    st.header("📞 Medical Professional References")
    st.write("If you need professional help, here are trusted medical professionals and departments you can contact:")
    
    # Add some spacing
    st.markdown("---")
    
    # Department of Psychiatry, KMC Manipal
    with st.container():
        st.subheader("🏥 Department of Psychiatry, KMC Manipal")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.write("**📧 Email:** psychiatry.kmc@manipal.edu")
            st.write("**📞 Phone:** +91-820-2922217")
            st.write("**📍 Location:** KMC Manipal")
        
        with col2:
            st.link_button("🗺️ View on Maps", "https://goo.gl/maps/ayxzEXbjB5SFRE4m7")
    
    st.markdown("---")
    
    # Department of Clinical Psychology - MCHP Manipal
    with st.container():
        st.subheader("🧠 Department of Clinical Psychology - MCHP Manipal")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.write("**📞 Phone:** 0820 292 2415")
            st.write("**📍 Location:** MCHP Manipal")
        
        with col2:
            st.link_button("🗺️ View on Maps", "https://maps.app.goo.gl/U93hFzusszvH3sJS7")
    
    st.markdown("---")
    
    # Perinatal Psychiatry Clinic at TMA Pai Hospital, Udupi
    with st.container():
        st.subheader("🤱 Perinatal Psychiatry Clinic - TMA Pai Hospital, Udupi")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.write("**📧 Email:** office.tmaph@manipal.edu")
            st.write("**📞 Phone:** +91 820 2526501")
            st.write("**📍 Location:** TMA Pai Hospital, Udupi")
            st.write("**🎯 Specialization:** Perinatal and maternal mental health")
        
        with col2:
            st.link_button("🗺️ View on Maps", "https://maps.app.goo.gl/pDDHhe96wC5eNErY8")
    
    st.markdown("---")
    
    # Emergency information
    st.error("🚨 **Emergency:** If you're experiencing a mental health crisis, please contact emergency services immediately or visit the nearest hospital.")
    
    # Additional helpful information
    st.info("💡 **Tip:** Don't hesitate to reach out for help. Mental health professionals are here to support you through your journey.")
    st.success("🌟 Remember, seeking help is a sign of strength. You are not alone!")

# if __name__ == "__main__":
#     show_references()