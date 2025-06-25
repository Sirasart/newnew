import streamlit as st
import random
from streamlit_extras.metric_cards import style_metric_cards

# -----------------------------
# MOCK DATABASE
# -----------------------------
products = [
    {
        "id": "prod_001",
        "name": "ข้าวกล้องอินทรีย์",
        "category": "ข้าว",
        "region": "อุบลราชธานี",
        "price": 45,
        "seller": "กลุ่มแม่บ้านบ้านนา",
        "trace": "ปลูกที่ อุบลฯ | เก็บเกี่ยว 1 พ.ค. 2025 | รับรอง Organic"
    },
    {
        "id": "prod_002",
        "name": "กล้วยตากพลังงานแสงอาทิตย์",
        "category": "ผลไม้แปรรูป",
        "region": "พิษณุโลก",
        "price": 35,
        "seller": "กลุ่มเกษตรบ้านคลอง",
        "trace": "ปลูกที่ พิษณุโลก | ตาก 15 มิ.ย. 2025 | ปลอดสาร"
    }
]

cart = []
user_profile = {
    "username": "demo_user",
    "coins": 100,
    "order_history": [],
    "role": "Customer"
}

# -----------------------------
# FUNCTION DEFINITIONS
# -----------------------------
def add_to_cart(product):
    cart.append(product)
    st.success(f"✅ เพิ่ม '{product['name']}' ลงในตะกร้าแล้ว")

def place_order():
    if not cart:
        st.warning("🛒 ตะกร้ายังว่างอยู่ ลองเลือกสินค้าเพิ่มเติม")
        return
    st.success("🎉 สั่งซื้อสำเร็จ! คุณได้รับ 10 Coins")
    user_profile["coins"] += 10
    user_profile["order_history"].extend(cart)
    cart.clear()

def recommend_products():
    if not user_profile["order_history"]:
        return products
    keywords = [item["category"] for item in user_profile["order_history"]]
    return [p for p in products if p["category"] in keywords]

# -----------------------------
# SIDEBAR
# -----------------------------
st.set_page_config(page_title="Local Hub", layout="centered")
st.sidebar.title("🍃 Local Hub")
st.sidebar.write(f"👤 ผู้ใช้: `{user_profile['username']}`")
st.sidebar.metric(label="💰 Coins", value=user_profile['coins'])
style_metric_cards()

page = st.sidebar.radio("📌 เมนู", ["หน้าแรก", "ตะกร้า", "คำสั่งซื้อ", "ระบบผู้ขาย", "ระบบแอดมิน"])

# -----------------------------
# PAGE: หน้าแรก
# -----------------------------
if page == "หน้าแรก":
    st.title("🛍️ สินค้าแนะนำจากชุมชน")
    st.markdown("---")
    for product in recommend_products():
        with st.container():
            st.subheader(f"📦 {product['name']}")
            st.caption(f"หมวด: {product['category']} | พื้นที่: {product['region']}")
            st.write(f"💸 ราคา: **{product['price']} บาท**")
            st.write(f"👩‍🌾 ผู้ผลิต: _{product['seller']}_")
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"🔍 ดู QR ต้นทาง - {product['id']}"):
                    st.info(f"🔗 {product['trace']}")
            with col2:
                if st.button(f"🛒 เพิ่มลงตะกร้า - {product['id']}"):
                    add_to_cart(product)
            st.markdown("---")

# -----------------------------
# PAGE: ตะกร้า
# -----------------------------
elif page == "ตะกร้า":
    st.title("🧺 ตะกร้าสินค้าของคุณ")
    st.markdown("---")
    if not cart:
        st.info("🔸 ยังไม่มีสินค้าในตะกร้า")
    else:
        total = sum([item["price"] for item in cart])
        for item in cart:
            st.write(f"- 🛍️ {item['name']} ({item['price']} บาท)")
        st.markdown(f"**รวมทั้งหมด: {total} บาท**")
        if st.button("✅ ยืนยันการสั่งซื้อ"):
            place_order()

# -----------------------------
# PAGE: คำสั่งซื้อ
# -----------------------------
elif page == "คำสั่งซื้อ":
    st.title("📦 คำสั่งซื้อที่ผ่านมา")
    st.markdown("---")
    if not user_profile["order_history"]:
        st.info("📭 ยังไม่มีประวัติการสั่งซื้อ")
    else:
        for item in user_profile["order_history"]:
            st.write(f"✅ {item['name']} ({item['price']} บาท)")

# -----------------------------
# PAGE: ระบบผู้ขาย (Mock)
# -----------------------------
elif page == "ระบบผู้ขาย":
    st.title("👩‍🌾 ระบบสำหรับผู้ขาย (จำลอง)")
    st.markdown("---")
    st.info("🔧 ฟังก์ชันนี้สำหรับผู้ขาย เพิ่ม/จัดการสินค้า (เวอร์ชันสมบูรณ์กำลังพัฒนา)")
    st.text_input("📌 ชื่อสินค้าใหม่")
    st.text_input("💸 ราคา")
    st.button("➕ เพิ่มสินค้า (จำลอง)")

# -----------------------------
# PAGE: ระบบแอดมิน (Mock)
# -----------------------------
elif page == "ระบบแอดมิน":
    st.title("🛡️ ระบบแอดมิน (จำลอง)")
    st.markdown("---")
    st.info("🧰 จัดการร้านค้า ตรวจสอบสินค้า รับเรื่องแจ้งปัญหา (เวอร์ชันสมบูรณ์กำลังพัฒนา)")
    st.button("📥 ดูร้านค้ารออนุมัติ")
    st.button("🚨 ดูรายการแจ้งปัญหา")
