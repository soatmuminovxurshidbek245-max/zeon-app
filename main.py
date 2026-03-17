import streamlit as st
import random
import time

# Sahifa sozlamalari
st.set_page_config(page_title="ZEON Ekologik AI", page_icon="🌍", layout="centered")

# CSS orqali dizaynni chiroyli qilish
st.markdown("""
    <style>
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border-radius: 20px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 ZEON: Kelajak iqlim texnologiyasi")
st.subheader("Tabiatni asrang va ZEON ballarini to'plang!")

if 'points' not in st.session_state:
    st.session_state.points = 0

st.sidebar.header("Sizning Profilingiz")
st.sidebar.metric("To'plangan ballar", f"{st.session_state.points} ZN")
st.sidebar.info("ZEON ballari kelajakda haqiqiy sovg'alarga almashinadi!")

tab1, tab2 = st.tabs(["📸 Rasm yuklash", "🏆 Reyting"])

with tab1:
    st.write("Daraxt eking yoki tabiatni tozalang va buni rasmga olib yuklang!")
    uploaded_file = st.file_uploader("Ekologik harakat rasmini yuklang", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        with st.spinner('AI rasmni tahlil qilmoqda...'):
            time.sleep(2) 
            st.image(uploaded_file, caption="Sizning hissangiz!", use_container_width=True)
            bonus = random.randint(20, 100)
            st.session_state.points += bonus
            st.success(f"Ajoyib! AI ijobiy harakatni aniqladi. Sizga {bonus} ZEON ball berildi!")
            st.balloons()

with tab2:
    st.header("Global Reyting")
    st.table({"Foydalanuvchi": ["Ali_Eco", "Green_Uz", "Siz (YOU)"], "Ballar": [1450, 980, st.session_state.points]})
    
