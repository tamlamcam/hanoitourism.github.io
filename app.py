import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dịch vụ thuê xe",layout="wide")

# ================= CSS =================

st.markdown("""
<style>

/* Thu nhỏ sidebar */
section[data-testid="stSidebar"] {
    width:190px !important;
}

/* Khung menu chung */
div[data-testid="stSidebar"] div[role="radiogroup"]{
    background:#6ccf8f;
    padding:8px;
    border-radius:10px;
}

/* Từng mục menu */
div[data-testid="stSidebar"] label{
    display:flex;
    justify-content:center;
    align-items:center;
    color:white !important;
    padding:8px;
    height:36px;
    border-radius:6px;
    font-weight:600;
}

/* Hover */
div[data-testid="stSidebar"] label:hover{
    background:#57b876;
}

/* Bỏ vòng tròn radio */
div[data-testid="stSidebar"] input[type="radio"]{
    display:none;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================

if "page" not in st.session_state:
    st.session_state.page="Trang chủ"

col1,col2,col3=st.columns([2,6,2])

with col1:
    if os.path.exists("logo.png"):
        st.image("logo.png",width=120)

with col2:

    m1,m2,m3,m4=st.columns(4)

    if m1.button("Trang chủ"):
        st.session_state.page="Trang chủ"

    if m2.button("Các dòng xe"):
        st.session_state.page="Xe"

    if m3.button("Bảng giá"):
        st.session_state.page="Bảng giá"

    if m4.button("Liên hệ đặt xe"):
        st.session_state.page="Liên hệ"

with col3:
    st.markdown("☎ **0948585816**")
    st.caption("Hotline 24/7")

st.divider()

menu=st.session_state.page

# ================= TRANG CHỦ =================

if menu=="Trang chủ":

    st.title("Dịch vụ cho thuê xe")

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.markdown('<div class="service-box">🚗<br>Thuê xe tháng</div>',unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="service-box">✈️<br>Đưa đón sân bay</div>',unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="service-box">🏢<br>Đón khách công tác</div>',unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="service-box">🌏<br>Du lịch</div>',unsafe_allow_html=True)

# ================= CÁC DÒNG XE =================

elif menu=="Xe":

    st.header("Danh mục xe")

    typecar=st.selectbox(
    "Chọn dòng xe",
    ["Sedan","SUV","MPV","Xe nhân viên"]
    )

    cars={

    "Sedan":[
    "Toyota Camry",
    "Toyota Vios"
    ],

    "SUV":[
    "Toyota Fortuner",
    "Ford Everest"
    ],

    "MPV":[
    "Toyota Innova",
    "Kia Carnival"
    ],

    "Xe nhân viên":[
    "Transit",
    "Universe"
    ]
    }

    cols=st.columns(4)

    for i,car in enumerate(cars[typecar]):

        with cols[i%4]:

            img=car.replace(" ","").lower()+".jpg"

            if os.path.exists(img):
                st.image(img,use_container_width=True)

            if st.button(f"Xem {car}",key=car):

                st.session_state.selected_car=car

    # ===== TRANG CHI TIẾT XE =====

    if "selected_car" in st.session_state:

        car=st.session_state.selected_car

        st.divider()
        st.subheader(car)

        # gallery ảnh

        st.write("Gallery ảnh xe")

        gallery=[
        car.replace(" ","").lower()+".jpg",
        car.replace(" ","").lower()+"1.jpg",
        car.replace(" ","").lower()+"2.jpg",
        car.replace(" ","").lower()+"3.jpg"
        ]

        gcols=st.columns(4)

        for i,img in enumerate(gallery):

            if os.path.exists(img):

                with gcols[i%4]:

                    st.image(img,use_container_width=True)

        st.write("Xe phù hợp cho đưa đón sân bay, công tác và du lịch.")

        st.subheader("Thông tin dịch vụ")

        data={
        "Dịch vụ":["Thuê ngày","Thuê tháng","Đưa đón sân bay"],
        "Giá":["1.200.000","18.000.000","450.000"]
        }

        st.table(pd.DataFrame(data))

# ================= BẢNG GIÁ =================

elif menu=="Bảng giá":

    st.header("Bảng giá thuê xe")

    tab1,tab2,tab3=st.tabs([
    "Thuê tháng",
    "Thuê ngày",
    "Sân bay"
    ])

    with tab1:

        if os.path.exists("banggiathang.xlsx"):
            df=pd.read_excel("banggiathang.xlsx")
            st.dataframe(df)

    with tab2:

        if os.path.exists("banggiangay.xlsx"):
            df=pd.read_excel("banggiangay.xlsx")
            st.dataframe(df)

    with tab3:

        if os.path.exists("banggiasanbay.xlsx"):
            df=pd.read_excel("banggiasanbay.xlsx")
            st.dataframe(df)

# ================= FORM ĐẶT XE =================

elif menu=="Liên hệ":

    st.header("Liên hệ đặt xe")

    st.write("Ha Noi Tourist and Trading")
    st.write("📍 829 Bạch Đằng - Hà Nội")
    st.write("☎ Hotline: 0948585816")

    st.markdown("[Chat Zalo](https://zalo.me/0948585816)")

    st.divider()

    st.subheader("Form đăng ký thuê xe")

    with st.form("booking"):

        name=st.text_input("Tên khách hàng")

        phone=st.text_input("Số điện thoại")

        email=st.text_input("Email")

        service=st.selectbox(
        "Loại dịch vụ",
        ["Thuê ngày","Thuê tháng","Đưa đón sân bay","Đi tỉnh"]
        )

        car=st.selectbox(
        "Loại xe",
        ["Sedan","SUV","MPV","Limousine"]
        )

        date=st.date_input("Ngày sử dụng")

        location=st.text_input("Điểm đón")

        destination=st.text_input("Điểm đến")

        note=st.text_area("Yêu cầu thêm")

        submit=st.form_submit_button("Gửi yêu cầu")

        if submit:

            if name and phone:

                st.success("Đã gửi yêu cầu. Chúng tôi sẽ liên hệ lại!")

            else:

                st.warning("Vui lòng nhập tên và số điện thoại")

st.divider()

st.caption("© 2026 Dịch vụ cho thuê xe")
