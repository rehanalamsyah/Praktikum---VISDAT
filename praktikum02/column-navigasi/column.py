import streamlit as st
import pandas as pd
import numpy as np

st.title("Column") # membuat title halaman

st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama.")
col2.image("praktikum01/assets/5.jpeg")
col2.write("Ini adalah kolom kedua dengan gambar Streamlit.")