import streamlit as st
import pandas as pd
import numpy as np

st.title("Area Chart") # membuat title halaman

st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168
""", unsafe_allow_html=True)

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=['C1', 'C2', 'C3', 'C4']
)

st.area_chart(df)