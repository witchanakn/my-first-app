import streamlit as st
st.title("แอปพิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh_years=st .number_input ("กรอกปี พ.ศ. ที่ต้องการแปลง" ,value=2569)
ce_years=bh_years-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
