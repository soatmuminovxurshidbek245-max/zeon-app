import streamlit as st
import random
import time

# Sahifa sozlamalari
st.set_page_config(page_title="ZEON Global Eco", page_icon="🌍", layout="centered")

# Dizayn
st.markdown("""
    <style>
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border-radius: 20px;
        width: 100%;
    }
    .status-box {
        padding: 10px;
        border-radius: 10px;
        background-color: #e8f5e9;
        border: 1px solid #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 ZEON: Ekologik Kelajak")

# Session state
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Sidebar
st.sidebar.header("👤 Shaxsiy Kabinet")
name_input = st.sidebar.text_input("Ismingizni kiriting:", value=st.session_state.user_name)
if name_input:
    st.session_state.user_name = name_input

st.sidebar.metric("Sizning ballaringiz", f"{st.session_state.points} ZN")

# Status aniqlash
user_status = "Yangi foydalanuvchi"
if st.session_state.points >= 1000:
    user_status = "🌳 Tabiat Qahramoni"
elif st.session_state.points >= 500:
    user_status = "🌱 Eko-Faol"
elif st.session_state.points >= 100:
    user_status = "🍃 Eko-Shogird"

st.sidebar.markdown(f"<div class='status-box'><b>Status:</b> {user_status}</div>", unsafe_allow_html=True)

# TABLAR
tab1, tab2, tab3 = st.tabs(["📸 Rasm yuklash", "🏆 Reyting", "🎁 Eko-Do'kon"])

with tab1:
    if not st.session_state.user_name:
        st.warning("Davom etish uchun sidebar-da ismingizni yozing!")
    else:
        st.write(f"Salom, **{st.session_state.user_name}**! Bugun tabiat uchun nima qildingiz?")
        uploaded_file = st.file_uploader("Rasmni tanlang", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            with st.spinner('Tahlil qilinmoqda...'):
                time.sleep(2)
                st.image(uploaded_file, use_container_width=True)
                bonus = random.randint(30, 150)
                st.session_state.points += bonus
                st.success(f"Ajoyib! +{bonus} ball berildi!")
                st.balloons()

with tab2:
    st.header("🏆 Global Leaderboard")
    current_name = st.session_state.user_name if st.session_state.user_name else "Siz"
    st.table({
        "Foydalanuvchi": ["Botir_Eco", "Green_Queen", current_name],
        "Ballar": [2800, 2450, st.session_state.points],
        "Status": ["🌳 Qahramon", "🌳 Qahramon", user_status]
    })

with tab3:
    st.header("🎁 ZEON Sovg'alar do'koni")
    st.write("To'plangan ballaringizni quyidagi mukofotlarga almashtiring:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Virtual")
        st.info("📜 Eko-Sertifikat (1000 ZN)")
        st.info("🎖 Profil uchun belgi (500 ZN)")
    with col2:
        st.subheader("Haqiqiy (Yaqinda)")
        st.warning("🌳 Daraxt ko'chati (5000 ZN)")
        st.warning("🛍 Eko-sumka (3000 ZN)")
        st.warning("☕️ Qahva uchun chegirma (2000 ZN)")
    
    st.write("---")
    st.caption("Eslatma: Haqiqiy sovg'alar hamkorlarimiz qo'shilgandan so'ng faollashadi.")

st.divider()
st.caption("ZEON AI © 2026. $800B Vision.")
    
