import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chauffeur & Limousine", page_icon="🚗", layout="wide")

# =========================
# CSS GIAO DIỆN
# =========================

st.markdown("""
<style>

/* sidebar nhỏ gọn */
section[data-testid="stSidebar"]{
    width:210px !important;
}

/* khung menu */
div[role="radiogroup"]{
    background:#6ccf8f;
    padding:8px;
    border-radius:10px;
}

/* từng mục menu */
div[role="radiogroup"] label{
    display:flex;
    justify-content:center;
    align-items:center;
    color:white !important;
    padding:8px;
    height:36px;
    margin:3px 0;
    font-weight:600;
}

/* hover */
div[role="radiogroup"] label:hover{
    background:#57b876;
    border-radius:6px;
}

/* ẩn vòng tròn radio */
input[type="radio"]{
    display:none;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

col1, col2 = st.columns([1,4])

with col1:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)

with col2:
    st.title("Chauffeur & Limousine")
    st.write("Đưa đón sân bay • Công tác • Du lịch • Sự kiện")

st.divider()

# =========================
# MENU
# =========================

menu = st.sidebar.radio(
    "MENU",
    ["🏠 Trang chủ","💰 Bảng giá","📅 Đặt xe","📞 Liên hệ"]
)

# =========================
# TRANG CHỦ
# =========================

if menu == "🏠 Trang chủ":

    st.header("Các dòng xe của chúng tôi")

    cars = {
        "Toyota Innova":[
        "Toyota Innova.jpg",
        "Toyota Innova3.jpg",
        "Toyota Innova4.jpg"
        ],

        "Toyota Fortuner":[
        "Toyota Fortuner.jpg",
        "Toyota Fortuner3.jpg",
        "Toyota Fortuner4.jpg"
        ],

        "Toyota Camry":[
        "Toyota Camry.jpg",
        "Toyota Camry3.jpg",
        "Toyota Camry4.jpg"
        ],

        "Kia Carnival":[
        "Kia Carnival.jpg",
        "Kia Carnival3.jpg",
        "Kia Carnival4.jpg"
        ]
    }

    cols = st.columns(4)

    for i,(car,images) in enumerate(cars.items()):

        with cols[i]:

            if os.path.exists(images[0]):
                st.image(images[0], width=300)

            if st.button(f"Xem ảnh {car}", key=car):

                st.subheader(car)

                for img in images:

                    if os.path.exists(img):
                        st.image(img, use_container_width=True)

# =========================
# BẢNG GIÁ
# =========================

elif menu == "💰 Bảng giá":

    st.header("Bảng giá thuê xe")

    if st.button("⚡ Xem bảng giá"):

        try:
            df = pd.read_excel("khung_bao_gia.xlsx")
            st.dataframe(df,use_container_width=True)

        except:
            st.error("Không tìm thấy file Excel báo giá")

# =========================
# ĐẶT XE
# =========================

elif menu == "📅 Đặt xe":

    st.header("Form đặt xe")

    name = st.text_input("Tên khách hàng")

    phone = st.text_input("Số điện thoại")

    car = st.selectbox(
        "Chọn xe",
        ["Toyota Innova","Toyota Fortuner","Toyota Camry","Kia Carnival"]
    )

    date = st.date_input("Ngày thuê")

    note = st.text_area("Yêu cầu thêm")

    if st.button("Gửi yêu cầu"):

        if name and phone:

            st.success("Đã gửi yêu cầu. Chúng tôi sẽ liên hệ lại!")

        else:

            st.warning("Vui lòng nhập tên và số điện thoại")

# =========================
# LIÊN HỆ
# =========================

elif menu == "📞 Liên hệ":

    st.header("Thông tin liên hệ")

    st.write("Ha Noi Tourist and Trading")

    st.write("📍 Head office: 49 Hai Ba Trung, Hoan Kiem, Hanoi")

    st.write("📍 Executive office: 829 Bạch Đằng, Hà Nội")

    st.write("📞 Hotline: +84 4 39361030")

    st.write("📞 Hotline: +84 439367602")

    st.subheader("Bản đồ")

    st.components.v1.iframe(
        "https://maps.google.com/maps?q=829%20bach%20dang%20ha%20noi&t=&z=15&ie=UTF8&iwloc=&output=embed",
        height=450
    )

st.divider()
st.caption("© 2026 Dịch vụ cho thuê xe")
