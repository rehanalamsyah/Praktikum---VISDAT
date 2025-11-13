import streamlit as st
from PIL import Image


st.title("Praktikum 2: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: spaced-out") # membuat caption

st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112

""", unsafe_allow_html=True) # memungkinkan penggunaan HTML di markdown

# Memuat gambar dari path lokal menggunakan PIL
# CATATAN: Pastikan file "D:/5.jpeg" tersedia saat aplikasi dijalankan.
try:
    img = Image.open("D:/5.jpeg")
except FileNotFoundError:
    st.error("Error: File 'D:/5.jpeg' tidak ditemukan. Harap periksa path.")
    # Gunakan gambar placeholder jika file tidak ditemukan
    # Anda mungkin ingin menggantinya dengan penanganan yang lebih baik
    img = None


# Menambahkan judul ke aplikasi Streamlit
st.title("Spaced-Out Columns")

# --- Membuat Dua Baris Konten ---
# Perulangan ini akan mengulangi blok kolom sebanyak 2 kali,
# secara efektif membuat dua baris yang identik.
for i in range(2):
    # Membuat 4 kolom dengan lebar yang tidak sama (rasio 3:1:2:1)
    # Ini akan menghasilkan 4 kolom dengan jarak di antaranya (spaced-out appearance)
    cols = st.columns((3, 1, 2, 1))

    # Memastikan gambar berhasil dimuat sebelum mencoba menampilkannya
    if img:
        # Menampilkan gambar yang sama di keempat kolom
        # Perhatikan bahwa kolom 1 dan 3 akan lebih lebar daripada kolom 2 dan 4.
        cols[0].image(img, caption=f"Baris {i+1}, Kolom 1 (Lebar 3)")
        cols[1].image(img, caption=f"Baris {i+1}, Kolom 2 (Lebar 1)")
        cols[2].image(img, caption=f"Baris {i+1}, Kolom 3 (Lebar 2)")
        cols[3].image(img, caption=f"Baris {i+1}, Kolom 4 (Lebar 1)")
    else:
         st.write(f"Baris {i+1}: Kolom tidak menampilkan gambar karena gagal dimuat.")