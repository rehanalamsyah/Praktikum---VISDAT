#import library yang dibutuhkan
from turtle import pd
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Praktikum 1: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Data Elements") # membuat caption


st.markdown("""
Kelompok 1:<br>
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168
""", unsafe_allow_html=True)
# DataFrame: komponen untuk menampilkan data dalam bentuk tabel interaktif

st.subheader("DataFrame") # membuat subheader

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)

#menampilkan dataframe
st.dataframe(df)

# Highlight nilai minumum
st.subheader("Highlight Minimum Value di DataFrame") # membuat subheader

# highlight nilai terkecil disetiap kolom dataframe
# axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

#Tabel Statis
st.subheader("Tabel Statis") # membuat subheader

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col %d' % i for i in range(10))
)

#menampilkan tabel statis
st.table(df)

# Metrics: komponen untuk menampilkan nilai metrik
st.subheader("Metrics") # membuat subheader
# Menampilkan metrik tunggal (nilai utama + perubahan nilai)

st.metric(label="Temperature", value="31 °C", delta="1.2 °C")
# kenaikan suhu sebesar 1.2 derajat celcius

# metrics sesuai delta_color
# delta_color digunakan untuk mengatur warna perubahan nilai
# - "normal": warna default (hijau untuk positif, merah untuk negatif)
# - "inverse": warna terbalik (merah untuk positif, hijau untuk negatif
# - "off": tanpa warna

# definisikan variabel metrics
col1, col2, col3 = st.columns(3)

# menampilkan indikator data
col1.metric(label="Curah Hujan", value="100 cm", delta="10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") # naik tapi oburuk
col3.metric(label="Pelanggan", value="100", delta="10", delta_color="off") # netral (tidak baik atau buruk)

# Menampilkan metrik tambahan dengan nilai kosong atau Nol
st.metric(label="Speed", value="none", delta="0") # kosong # naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") # turun buruk karena di setting default