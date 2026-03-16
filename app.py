import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chauffeur & Limousine", page_icon="🚗", layout="wide")

# =========================
# CSS
# =========================

st.markdown("""
<style>

/* ẩn sidebar */
section[data-testid="stSidebar"]{
    display:none;
}

/* menu ngang */
.top-menu{
    position:fixed;
    top:0;
    left:0;
    right:0;
    height:60px;
    background:#6ccf8f;
    display:flex;
    align-items:center;
    padding:0 30px;
    gap:30px;
    z-index:999;
}

/* logo */
.logo{
    height:40px;
}

/* link menu */
.top-menu a{
    color:white;
    text-decoration:none;
    font-size:18px;
    font-weight:600;
}

/* hover */
.top-menu a:hover{
    opacity:0.8;
}

/* đẩy nội dung xuống */
.main{
    margin-top:80px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# MENU + LOGO
# =========================

menu = st.query_params.get("menu", ["Trang chủ"])[0]

st.markdown("""
<div class="top-menu">

<a href="?menu=Trang%20chủ">
<img src="logo.png" class="logo">
</a>

<a href="?menu=Trang%20chủ">Trang chủ</a>
<a href="?menu=Bảng%20giá">Bảng giá</a>
<a href="?menu=Đặt%20xe">Đặt xe</a>
<a href="?menu=Liên%20hệ">Liên hệ</a>

</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.title("Chauffeur & Limousine")
st.write("Đưa đón sân bay • Công tác • Du lịch • Sự kiện")

st.divider()

# =========================
# TRANG CHỦ
# =========================

if menu == "Trang chủ":

    st.header("Các dòng xe của chúng tôi")

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
                st.image(images[0], width=280)

            if st.button(f"Xem ảnh {car}", key=car):

                st.subheader(car)

                for img in images:

                    if os.path.exists(img):
                        st.image(img, width=700)

# =========================
# BẢNG GIÁ
# =========================

elif menu == "Bảng giá":

    st.header("Bảng giá thuê xe")

    if st.button("⚡ Xem bảng giá"):

        try:
            df = pd.read_excel("khung_bao_gia.xlsx")
            st.dataframe(df)

        except:
            st.error("Không tìm thấy file Excel báo giá")

# =========================
# ĐẶT XE
# =========================

elif menu == "Đặt xe":

    st.header("Form đặt xe")

    name = st.text_input("Tên khách hàng")
    phone = st.text_input("Số điện thoại")

    car = st.selectbox(
        "Chọn xe",
        ["Toyota Innova","Toyota Fortuner","Toyota Camry","Toyota Alphard"]
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

elif menu == "Liên hệ":

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

st.markdown("</div>", unsafe_allow_html=True)
