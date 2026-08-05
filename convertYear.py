import streamlit as st
st.title("แอปพิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh_year= st.number_input ("กรอกปี พ.ศ. 2554" ,value=2554)
ce_year= bh_years-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
