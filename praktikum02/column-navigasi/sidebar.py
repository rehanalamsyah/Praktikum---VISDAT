import streamlit as st

st.title("Praktikum 2: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Sidebar") # membuat caption


st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112

""", unsafe_allow_html=True) # memungkinkan penggunaan HTML di markdown

# --- Sidebar ---
# Semua elemen yang diawali dengan st.sidebar. akan ditempatkan di sidebar aplikasi.

# Menambahkan judul ke sidebar
st.sidebar.title("Sidebar")

# Menambahkan widget radio button ke sidebar
st.sidebar.radio("Are you a New User", ["Yes", "No"])

# Menambahkan widget slider ke sidebar
# Slider memiliki rentang dari 0 hingga 10 (nilai minimum dan maksimum)
st.sidebar.slider("Select a Number", 0, 10)

# Catatan: Anda dapat menambahkan elemen ke body utama aplikasi di sini.
# st.write("Konten utama aplikasi di sini.")