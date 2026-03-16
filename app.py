import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chauffeur & Limousine", page_icon="🚗", layout="wide")

# =========================
# CSS NAVBAR
# =========================

st.markdown("""
<style>

/* Ẩn sidebar */
section[data-testid="stSidebar"]{
display:none;
}

/* Navbar */
.navbar{
position:fixed;
top:0;
left:0;
right:0;
height:60px;
background:#f4f4f4;
display:flex;
align-items:center;
padding:0 40px;
gap:35px;
border-bottom:1px solid #ddd;
z-index:999;
}

/* Logo */
.logo{
height:38px;
}

/* Menu link */
.navbar a{
text-decoration:none;
color:#333;
font-size:16px;
font-weight:600;
}

/* Hover */
.navbar a:hover{
color:#ff6600;
}

/* Push content xuống */
.block-container{
padding-top:80px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# MENU
# =========================

menu = st.query_params.get("menu", ["Trang chủ"])[0]

st.markdown("""
<div class="navbar">

<a href="?menu=Trang%20chủ">
<img src="logo.png" class="logo">
</a>

<a href="?menu=Trang%20chủ">Trang chủ</a>
<a href="?menu=Các%20loại%20xe">Các loại xe</a>
<a href="?menu=Báo%20giá">Báo giá</a>
<a href="?menu=Liên%20hệ%20đặt%20xe">Liên hệ đặt xe</a>
<a href="?menu=Về%20chúng%20tôi">Về chúng tôi</a>

</div>
""", unsafe_allow_html=True)

# =========================
# TRANG CHỦ
# =========================

if menu == "Trang chủ":

    st.title("Chauffeur & Limousine")
    st.write("Đưa đón sân bay • Công tác • Du lịch • Sự kiện")

    st.header("Dịch vụ của chúng tôi")

    st.write("""
    - Xe sân bay
    - Xe công tác
    - Xe du lịch
    - Xe sự kiện
    """)

# =========================
# CÁC LOẠI XE
# =========================

elif menu == "Các loại xe":

    st.title("Các loại xe")

    cars = {

    "Toyota Innova":[
    "toyotainnova.jpg",
    "toyotainnova1.jpg",
    "toyotainnova2.jpg",
    "toyotainnova3.jpg",
    "toyotainnova4.jpg"
    ],

    "Toyota Fortuner":[
    "toyotafortuner.jpg",
    "toyotafortuner1.jpg",
    "toyotafortuner2.jpg",
    "toyotafortuner3.jpg"
    ],

    "Toyota Camry":[
    "toyotacamry.jpg",
    "toyotacamry1.jpg",
    "toyotacamry2.jpg",
    "toyotacamry3.jpg",
    "toyotacamry4.jpg"
    ],

    "Toyota Alphard":[
    "toyotaalphard.jpg",
    "toyotaalphard1.jpg",
    "toyotaalphard2.jpg",
    "toyotaalphard3.jpg",
    "toyotaalphard4.jpg"
    ]
    }

    cols = st.columns(4)

    for i,(car,images) in enumerate(cars.items()):

        with cols[i]:

            if os.path.exists(images[0]):
                st.image(images[0], width=260)

            if st.button(f"Xem ảnh {car}", key=car):

                st.subheader(car)

                for img in images:

                    if os.path.exists(img):
                        st.image(img, width=700)

# =========================
# BÁO GIÁ
# =========================

elif menu == "Báo giá":

    st.title("Bảng báo giá")

    if st.button("Xem bảng giá"):

        try:
            df = pd.read_excel("khung_bao_gia.xlsx")
            st.dataframe(df)

        except:
            st.error("Không tìm thấy file Excel")

# =========================
# LIÊN HỆ ĐẶT XE
# =========================

elif menu == "Liên hệ đặt xe":

    st.title("Liên hệ đặt xe")

    name = st.text_input("Tên khách hàng")
    phone = st.text_input("Số điện thoại")

    car = st.selectbox(
    "Chọn loại xe",
    ["Toyota Innova","Toyota Fortuner","Toyota Camry","Toyota Alphard"]
    )

    date = st.date_input("Ngày thuê")
    note = st.text_area("Yêu cầu thêm")

    if st.button("Gửi yêu cầu"):

        if name and phone:
            st.success("Chúng tôi sẽ liên hệ lại sớm nhất!")
        else:
            st.warning("Vui lòng nhập đầy đủ thông tin")

# =========================
# VỀ CHÚNG TÔI
# =========================

elif menu == "Về chúng tôi":

    st.title("Về chúng tôi")

    st.write("""
    Công ty chuyên cung cấp dịch vụ:

    - Xe sân bay
    - Xe công tác
    - Xe du lịch
    - Xe sự kiện

    Cam kết:

    - Xe đời mới
    - Lái xe chuyên nghiệp
    - Giá cả cạnh tranh
    """)

    st.subheader("Địa chỉ")

    st.write("829 Bạch Đằng, Hà Nội")

    st.components.v1.iframe(
    "https://maps.google.com/maps?q=829%20bach%20dang%20ha%20noi&t=&z=15&ie=UTF8&iwloc=&output=embed",
    height=450
    )

st.divider()
st.caption("© 2026 Chauffeur & Limousine")
