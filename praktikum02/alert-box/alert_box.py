import streamlit as st

st.title("Praktikum 2: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Alert Box") # membuat caption


st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112
""", unsafe_allow_html=True)

# Menampilkan pesan notifikasi dengan warna dan ikon yang berbeda
# Sinyal hijau, biasanya untuk operasi yang berhasil
st.success("Successful")

# Sinyal kuning/oranye, biasanya untuk perhatian atau peringatan
st.warning("Warning")

# Sinyal biru, biasanya untuk informasi umum
st.info("Info")

# Sinyal merah, biasanya untuk pesan kesalahan yang menghalangi
st.error("Error")

# Mirip dengan st.error, tetapi biasanya digunakan untuk menampilkan 
# traceback Python (jika sebuah pengecualian dilewatkan sebagai argumen)
st.exception("It is an exception")