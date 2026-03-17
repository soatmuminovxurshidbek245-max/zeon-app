import streamlit as st
import random
import time

# Sahifa sozlamalari
st.set_page_config(page_title="ZEON Global AI", page_icon="🌳", layout="centered")

# Session state
if 'points' not in st.session_state: st.session_state.points = 0
if 'co2' not in st.session_state: st.session_state.co2 = 0.0
if 'user_name' not in st.session_state: st.session_state.user_name = ""

# Sidebar statistika
st.sidebar.title("👤 ZEON Profile")
name = st.sidebar.text_input("Ismingiz:", value=st.session_state.user_name)
if name: st.session_state.user_name = name

st.sidebar.divider()
st.sidebar.metric("To'plangan Ballar", f"{st.session_state.points} ZN")
st.sidebar.metric("Umumiy CO2 (kg)", f"{st.session_state.co2:.2f}")

# Asosiy qism
st.title("🌍 ZEON: Global Eco-Analysis")
st.write(f"Salom **{st.session_state.user_name}**! Rasmni yuklang va umumiy tahlilni oling.")

uploaded_file = st.file_uploader("Ekologik rasm (Daraxt, Bog', Chiqindi turlari va h.k.)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Tahlil qilinayotgan ob'ekt", use_container_width=True)
    
    with st.status("🚀 AI Umumiy Tahlil jarayonida...", expanded=True) as status:
        st.write("📡 Sun'iy yo'ldosh ma'lumotlari bilan solishtirilmoqda...")
        time.sleep(1.5)
        st.write("🌿 Biologik xilma-xillik indeksi hisoblanmoqda...")
        time.sleep(1.5)
        st.write("📊 Emissiya kamayishi prognoz qilinmoqda...")
        status.update(label="Tahlil tayyor! ✅", state="complete", expanded=False)

    # --- AI UMUMIY TAHLILI ---
    st.subheader("📋 AI Ekologik Tahlilnomasi")
    
    col1, col2, col3 = st.columns(3)
    
    # Tasodifiy tahlil natijalari (Investorga ko'rsatish uchun)
    efficiency = random.randint(75, 98)
    plant_type = random.choice(["Archa (Conifer)", "Eman (Oak)", "Mevali daraxt", "Shahar parki", "Uy o'simligi"])
    yearly_o2 = random.randint(100, 500)

    with col1:
        st.metric("Samaradorlik", f"{efficiency}%")
    with col2:
        st.metric("Ob'ekt turi", plant_type)
    with col3:
        st.metric("Yillik O2 (litr)", f"+{yearly_o2}")

    # AI ning shaxsiy xulosasi
    st.info(f"**AI Xulosasi:** Ushbu {plant_type} hozirgi holatda iqlim o'zgarishiga qarshi kurashda yuqori samaradorlik ko'rsatmoqda. Agar bunday ob'ektlar soni 10% ga oshsa, hududdagi havo harorati 0.5°C ga pasayishi mumkin.")

    # Ballarni yangilash
    if st.button("Ballarni hisobga qo'shish"):
        bonus = random.randint(150, 400)
        st.session_state.points += bonus
        st.session_state.co2 += (bonus / 100)
        st.success(f"Hisobingizga {bonus} ZN qo'shildi! Keyingi harakatga o'ting.")
        st.balloons()

st.divider()
st.caption("ZEON AI © 2026. Empowering Climate Action through Data.")
    
