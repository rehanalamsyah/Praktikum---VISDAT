import streamlit as st
from PIL import Image


st.title("Praktikum 2: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Padding") # membuat caption


st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112

""", unsafe_allow_html=True) # memungkinkan penggunaan HTML di markdown

# Memuat gambar dari path lokal menggunakan PIL
# CATATAN: Pastikan file "D:/animal2.jpg" tersedia saat aplikasi dijalankan.
try:
    img = Image.open("D:/5.jpeg ")
except FileNotFoundError:
    st.error("Error: File 'D:/5.jpeg' tidak ditemukan. Harap periksa path.")
    img = None


# Menambahkan judul ke aplikasi Streamlit
st.title("Padding")

# Mendefinisikan Padding dengan Kolom
# Membuat tiga kolom dengan rasio lebar (10, 2, 10).
# Kolom kedua ('padding') berfungsi sebagai spasi kosong (padding)
# karena tidak ada konten yang ditempatkan di dalamnya.
col1, padding, col2 = st.columns((10, 2, 10))

# --- Kolom Pertama (col1) ---
with col1:
    # Menggunakan st.image() alih-alih col1.image() untuk konsistensi di dalam blok 'with'
    if img:
        st.image(img, caption="Kolom 1")

# --- Kolom Kedua (padding) ---
# Tidak ada kode di sini, meninggalkan kolom ini kosong sebagai spasi.

# --- Kolom Ketiga (col2) ---
with col2:
    # Menggunakan st.image() alih-alih col2.image() untuk konsistensi di dalam blok 'with'
    if img:
        st.image(img, caption="Kolom 2")