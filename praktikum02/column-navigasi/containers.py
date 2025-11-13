import streamlit as st
import numpy as np

st.title("Praktikum 2: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Container") # membuat caption


st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112
""", unsafe_allow_html=True)


# Menambahkan judul ke aplikasi Streamlit
st.title("Container")

# --- Konten di Dalam Container ---
# Membuat sebuah container yang dapat menampung elemen secara independen.
# Konten di dalam 'with st.container():' akan dibungkus bersama.
with st.container():
    st.write("Element Inside Container")
    
    # Mendefinisikan Elemen Grafik (Chart)
    # Membuat data acak 40x4 menggunakan numpy untuk grafik garis
    chart_data = np.random.randn(40, 4)
    st.line_chart(chart_data)

# --- Konten di Luar Container ---
# Elemen ini akan muncul di bawah container, di bagian utama aplikasi.
st.write("Element Outside Container")


# Menambahkan judul ke aplikasi Streamlit
st.title("Out of Order Container")

# --- Mendefinisikan Container ---
# Membuat sebuah container yang disimpan dalam variabel
container_one = st.container()

# Menulis elemen pertama ke dalam container_one
container_one.write("Element One Inside Container")

# Menulis elemen di luar container (langsung ke aplikasi utama)
st.write("Element Outside Container")

# --- Memasukkan Lebih Banyak Elemen ke Container ---
# Streamlit memungkinkan Anda menambahkan elemen ke container yang sudah didefinisikan
# meskipun elemen lain (seperti "Element Outside Container") sudah ditambahkan setelahnya.
# Elemen-elemen ini akan ditambahkan di bagian bawah container_one, sebelum "Element Outside Container".
container_one.write("Element Two Inside Container")

# Menambahkan grafik garis acak ke dalam container
chart_data = np.random.randn(40, 4)
container_one.line_chart(chart_data)