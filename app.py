import streamlit as st
import pandas as pd
import os

# ===== CSS GIAO DIỆN =====
st.markdown("""
<style>

/* Thu nhỏ sidebar */
section[data-testid="stSidebar"] {
    width:220px !important;
}

/* Khoảng cách menu */
section[data-testid="stSidebar"] .stRadio > div{
    gap:12px;
}

/* Khung menu */
section[data-testid="stSidebar"] .stRadio label{
    background-color:#6ccf8f;
    color:white;
    padding:14px;
    border-radius:6px;
    border:1px solid #5bb97a;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    font-weight:bold;
    height:50px;
}

/* Hover */
section[data-testid="stSidebar"] .stRadio label:hover{
    background-color:#57b876;
}

/* Khung ảnh xe */
.car-card{
    width:100%;
    height:250px;
    overflow:hidden;
    border-radius:8px;
}

/* Ảnh luôn vừa khung */
.car-card img{
    width:100%;
    height:100%;
    object-fit:cover;
}

</style>
""", unsafe_allow_html=True)

# ===== CẤU HÌNH TRANG =====
st.set_page_config(page_title="Dịch vụ thuê xe", page_icon="🚗", layout="wide")

# ===== HEADER =====
col1, col2 = st.columns([1,4])

with col1:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)

with col2:
    st.title("Chauffeur & Limousine")
    st.write("Đưa đón sân bay • Công tác • Du lịch • Sự kiện")

st.divider()

# ===== MENU =====
menu = st.sidebar.radio(
    "MENU",
    ["Trang chủ","Bảng giá","Đặt xe","Liên hệ"]
)

# ===============================
# TRANG CHỦ
# ===============================

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
            "toyotacamry4.jpg",
        ],

        "Kia Carnival":[
            "toyotaalphard.jpg",
            "toyotaalphard1.jpg",
            "toyotaalphard2.jpg",
            "toyotaalphard3.jpg",
            "toyotaalphard4.jpg",
        ]
    }

    cols = st.columns(4)

    for i,(car,images) in enumerate(cars.items()):

        with cols[i]:

            # khung ảnh cố định
            st.markdown('<div class="car-card">', unsafe_allow_html=True)

            if os.path.exists(images[0]):
                st.image(images[0], use_container_width=True)
            else:
                st.warning(f"Không tìm thấy ảnh: {images[0]}")

            st.markdown('</div>', unsafe_allow_html=True)

            # nút xem ảnh
            if st.button(f" {car}", key=car):

                st.subheader(car)

                for img in images:

                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                    else:
                        st.warning(f"Thiếu ảnh: {img}")

# ===============================
# BẢNG GIÁ
# ===============================

elif menu == "Bảng giá":

    st.header("Bảng giá thuê xe")

    if st.button("⚡ Báo giá xe đi tỉnh"):

        try:
            df = pd.read_excel("baogiaxeditinh.xlsx")
            st.dataframe(df)

        except:
            st.error("Không tìm thấy file Excel báo giá")

# ===============================
# FORM ĐẶT XE
# ===============================

elif menu == "Đặt xe":

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

# ===============================
# LIÊN HỆ
# ===============================

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
