import streamlit as st
import random
import time
import pandas as pd

# 1. Sahifa sozlamalari
st.set_page_config(page_title="ZEON Global AI", page_icon="🌍", layout="centered")

# 2. Maxsus Stil (CSS)
st.markdown("""
    <style>
    .main { background-color: #f9fbf9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .report-box { padding: 20px; border-radius: 15px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State (Ma'lumotlarni saqlash)
if 'points' not in st.session_state: st.session_state.points = 0
if 'co2' not in st.session_state: st.session_state.co2 = 0.0
if 'history' not in st.session_state: st.session_state.history = []
if 'user_name' not in st.session_state: st.session_state.user_name = ""

# 4. Sidebar (Yon menyu)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/892/892926.png", width=100)
st.sidebar.title("ZEON Dashboard")
name = st.sidebar.text_input("Ismingizni kiriting:", value=st.session_state.user_name)
if name: st.session_state.user_name = name

st.sidebar.divider()
st.sidebar.subheader("Sizning ko'rsatkichlaringiz")
st.sidebar.metric("Umumiy Ballar", f"{st.session_state.points} ZN")
st.sidebar.metric("CO2 Tejaldi (kg)", f"{st.session_state.co2:.2f}")

# 5. Asosiy Sahifa
st.title("🌍 ZEON: AI Climate Solution")
st.write(f"Xush kelibsiz, **{st.session_state.user_name if st.session_state.user_name else 'Ekolog'}**! Sayyorani qutqarishga tayyormisiz?")

tab1, tab2, tab3, tab4 = st.tabs(["📸 AI Scan", "🏆 Ranking", "🎁 Store", "📊 History"])

# --- TAB 1: AI SCAN ---
with tab1:
    st.subheader("Rasm yuklang va AI tahlilini oling")
    uploaded_file = st.file_uploader("Tabiat yoki eko-harakat rasmi", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
        
        with st.status("🔍 ZEON AI tahlil qilmoqda...", expanded=True) as status:
            time.sleep(1)
            st.write("🛰 Geo-lokatsiya aniqlanmoqda...")
            time.sleep(1)
            st.write("🌿 Ob'ekt turi tahlil qilinmoqda...")
            time.sleep(1)
            st.write("📈 CO2 ko'rsatkichlari hisoblanmoqda...")
            status.update(label="Tahlil yakunlandi! ✅", state="complete", expanded=False)

        # AI Analysis Result
        eff = random.randint(80, 99)
        obj = random.choice(["Daraxt (Archa)", "Daraxt (Eman)", "Bog' hududi", "Yashil tom", "Qayta ishlangan plastik"])
        o2_gain = random.randint(50, 200)
        
        st.markdown(f"""
        <div class="report-box">
            <h3>📋 AI Ekologik Hisoboti</h3>
            <p><b>Ob'ekt:</b> {obj}</p>
            <p><b>Ekologik samaradorlik:</b> {eff}%</p>
            <p><b>Yillik O2 prognozi:</b> +{o2_gain} litr</p>
            <p><i>AI Xulosasi: Ushbu harakat iqlim barqarorligiga sezilarli hissa qo'shadi.</i></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Tasdiqlash va Ballarni olish"):
            bonus = random.randint(100, 500)
            st.session_state.points += bonus
            st.session_state.co2 += (bonus / 150)
            st.session_state.history.append({"Action": obj, "Points": bonus, "CO2": bonus/150})
            st.success(f"Hisobingizga {bonus} ZN qo'shildi!")
            st.balloons()

# --- TAB 2: RANKING ---
with tab2:
    st.subheader("🏆 Global Leaderboard")
    df = pd.DataFrame({
        "User": ["Botir_Eco", "Green_Queen", "Sardor_AI", st.session_state.user_name if st.session_state.user_name else "Siz"],
        "Points (ZN)": [5400, 4200, 3900, st.session_state.points],
        "Impact (CO2 kg)": [36.0, 28.0, 26.0, st.session_state.co2]
    }).sort_values(by="Points (ZN)", ascending=False)
    st.table(df)

# --- TAB 3: STORE ---
with tab3:
    st.subheader("🎁 Sovg'alar va Imtiyozlar")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("**Eko-Sertifikat** \n\n 1,000 ZN")
        if st.button("Sotib olish 1"):
            if st.session_state.points >= 1000: st.success("Sertifikat yuborildi!")
            else: st.error("Ball yetarli emas")
            
    with col_b:
        st.info("**Haqiqiy Daraxt Ekish** \n\n 5,000 ZN")
        if st.button("Sotib olish 2"):
            if st.session_state.points >= 5000: st.success("Daraxt ekish uchun buyurtma berildi!")
            else: st.error("Ball yetarli emas")

# --- TAB 4: HISTORY ---
with tab4:
    st.subheader("📜 Sizning harakatlaringiz tarixi")
    if st.session_state.history:
        st.write(pd.DataFrame(st.session_state.history))
    else:
        st.write("Hozircha harakatlar mavjud emas.")

st.divider()
st.caption("ZEON AI © 2026 - Digitalizing the Green Future.")
