import streamlit as st
import random
import time

# Sahifa sozlamalari
st.set_page_config(page_title="ZEON Global Eco", page_icon="🌍", layout="centered")

# Dizaynni yanada kuchaytiramiz
st.markdown("""
    <style>
    .main { background-color: #f4f9f4; }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border-radius: 25px;
        height: 3em;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 ZEON: Global Ekologik Harakat")
st.write("Dunyoni asrash uchun kichik harakat qiling va tarixdan joy oling!")

# Foydalanuvchi ma'lumotlarini saqlash
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Sidebar - Profil
st.sidebar.header("👤 Shaxsiy Kabinet")
name_input = st.sidebar.text_input("Ismingizni yozing:", value=st.session_state.user_name)
if name_input:
    st.session_state.user_name = name_input

st.sidebar.metric("Sizning ballaringiz", f"{st.session_state.points} ZN")
st.sidebar.write("---")
st.sidebar.success("Har bir rasm - tabiat uchun hayot!")

# Asosiy qism
tab1, tab2, tab3 = st.tabs(["📸 Harakatni yozib olish", "🏆 Reyting", "💡 Tavsiyalar"])

with tab1:
    if st.session_state.user_name == "":
        st.warning("Iltimos, avval yon menyuda (sidebar) ismingizni kiriting!")
    else:
        st.write(f"Salom, **{st.session_state.user_name}**! Bugun qanday yaxshilik qildingiz?")
        uploaded_file = st.file_uploader("Rasmni yuklang (Daraxt, tozalik va h.k.)", type=["jpg", "png", "jpeg"])

        if uploaded_file:
            with st.spinner('ZEON AI rasmni tahlil qilmoqda...'):
                time.sleep(2)
                st.image(uploaded_file, caption="Sizning hissangiz!", use_container_width=True)
                bonus = random.randint(30, 150)
                st.session_state.points += bonus
                st.success(f"Ajoyib! {st.session_state.user_name}, sizga {bonus} ZEON ball berildi!")
                st.balloons()

with tab2:
    st.header("🏆 Global Leaderboard")
    st.write("Eng faol tabiat himoyachilari:")
    
    current_user = st.session_state.user_name if st.session_state.user_name else "Siz"
    
    leaderboard_data = {
        "O'rin": [1, 2, 3, 4],
        "Foydalanuvchi": ["Botir_Eco", "Green_Queen", "Sarvar_Forest", current_user],
        "Ballar": [2800, 2450, 1900, st.session_state.points]
    }
    st.table(leaderboard_data)

with tab3:
    st.info("Bilardingizmi? Bitta ekilgan daraxt yiliga 22 kg karbonat angidridni yutadi!")
    st.write("1. Plastikdan voz keching.")
    st.write("2. Suvni tejang.")
    st.write("3. Chiqindini saralang.")

st.divider()
st.caption("ZEON AI © 2026. Global Climate Tech Project.")
