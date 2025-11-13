import streamlit as st
import time

st.title("Praktikum 2: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Empty Container") # membuat caption


st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112
""", unsafe_allow_html=True)

# --- Mendefinisikan Wadah Kosong (Empty Container) ---
# st.empty() membuat sebuah elemen placeholder di aplikasi.
# Elemen ini dimaksudkan untuk diisi dan di-replace (diganti) secara dinamis
# oleh elemen-elemen berikutnya yang ditambahkan ke dalamnya.
placeholder = st.empty()

# Mengganti konten placeholder secara berulang (membuat hitungan mundur)
for seconds in range(5):
    # Mengisi placeholder dengan pesan hitungan mundur
    # Perhatikan bahwa kita tidak menggunakan 'with st.empty():' untuk loop dinamis,
    # tetapi menggunakan variabel placeholder yang sudah didefinisikan di luar loop.
    placeholder.write(f"⏳ {seconds} seconds have passed")
    
    # Menunggu selama 1 detik
    time.sleep(1)

# Setelah loop selesai, mengisi placeholder untuk terakhir kalinya
# (menghapus pesan hitungan mundur sebelumnya dan menggantinya dengan pesan akhir)
placeholder.write("✔️ Times up!")

# Catatan: Dalam kode asli Anda, penggunaan 'with st.empty():' diikuti dengan 'st.write("✓ Times up!")'
# di luar loop tetapi masih dalam blok 'with' memiliki sintaks yang sedikit membingungkan untuk pembaruan dinamis.
# Implementasi di atas (menggunakan variabel untuk placeholder) adalah cara yang paling umum
# dan berfungsi untuk membuat pembaruan yang terus-menerus mengganti konten sebelumnya.