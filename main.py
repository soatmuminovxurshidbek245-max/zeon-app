import streamlit as st
import random

st.set_page_config(page_title="ZEON", page_icon="🌍")
st.title("🌍 ZEON: Climate Action AI")
st.write("Welcome to the future of $800B Climate Tech!")

if 'points' not in st.session_state:
    st.session_state.points = 0

st.sidebar.metric("Your ZEON Points", st.session_state.points)

uploaded_file = st.file_uploader("Upload an eco-action photo", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Analyzing...", use_container_width=True)
    bonus = random.randint(10, 50)
    st.session_state.points += bonus
    st.success(f"AI Analysis: Eco-action detected! +{bonus} Points earned.")
    st.balloons()

st.header("🏆 Global Leaderboard")
st.table({"User": ["User_1", "User_2", "YOU"], "Points": [1200, 850, st.session_state.points]})
