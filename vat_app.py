import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price = st.number_input("219 (บาท):", value=219)
import streamlit as st
price = st.number_input("219 (บาท):", value=219)
net_price = price - vat
st.write("นาย วิชญ์ชนกันต์ ทาโน เลขที่ 20  ม.4/17")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

