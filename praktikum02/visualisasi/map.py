import streamlit as st
import pandas as pd
import numpy as np

st.title("Map") # membuat title halaman

st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168
""", unsafe_allow_html=True)
# Membuat DataFrame dengan data koordinat geografis (latitude dan longitude)

df = pd.DataFrame(
    np.random.randn(50, 2) / [10, 10] + [15.4589, 75.0078],
    columns=['latitude', 'longitude']
)

st.map(df)