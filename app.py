import streamlit as st
import random
# 🔻 เอาออก: from streamlit_extras.metric_cards import style_metric_cards

...

# -----------------------------
# SIDEBAR
# -----------------------------
st.set_page_config(page_title="CPXTRA Fresh", layout="centered")
st.sidebar.title("🍃 CPXTRA Fresh")
st.sidebar.markdown(f"👤 **ผู้ใช้:** `{user_profile['username']}`")
st.sidebar.markdown(f"💰 **Coins:** `{user_profile['coins']}`")
# 🔻 เอาออก: style_metric_cards()

page = st.sidebar.radio("📌 เมนู", ["หน้าแรก", "ตะกร้า", "คำสั่งซื้อ", "ระบบผู้ขาย", "ระบบแอดมิน"])
