import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
import streamlit as st
price = st.number_input("219 (บาท):", value=0.0)
net_price = 219 - 7.0
st.write("นาย วิชญ์ชนกันต์ ทาโน เลขที่ 20  ม.4/17")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
