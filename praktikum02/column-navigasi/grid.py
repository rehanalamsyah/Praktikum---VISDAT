import streamlit as st
from PIL import Image

st.title("Praktikum 2: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Grid") # membuat caption

st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112

""", unsafe_allow_html=True) # memungkinkan penggunaan HTML di markdown


# Memuat gambar dari path lokal menggunakan PIL
# CATATAN: Pastikan file "D:/animal1.jpg" tersedia saat aplikasi dijalankan.
try:
    img = Image.open("D:/4.jpeg")
except FileNotFoundError:
    st.error("Error: File 'D:/4.jpeg' tidak ditemukan. Harap periksa path.")
    img = None


# Menambahkan judul ke aplikasi Streamlit
st.title("Grid")

# --- Membuat Tata Letak Grid (4x4) ---
# Perulangan ini akan membuat 4 baris
for a in range(4):
    # Mendefinisikan 4 kolom dengan lebar yang sama (rasio 1:1:1:1)
    cols = st.columns((1, 1, 1, 1))

    # Memastikan gambar berhasil dimuat sebelum mencoba menampilkannya
    if img:
        # Menampilkan gambar yang sama di keempat kolom baris saat ini
        # Ini akan membuat 4 elemen per baris
        with cols[0]:
            st.image(img, caption=f"Baris {a+1}, Kolom 1")
        with cols[1]:
            st.image(img, caption=f"Baris {a+1}, Kolom 2")
        with cols[2]:
            st.image(img, caption=f"Baris {a+1}, Kolom 3")
        with cols[3]:
            st.image(img, caption=f"Baris {a+1}, Kolom 4")
    else:
        st.write(f"Baris {a+1}: Gagal menampilkan gambar.")