import streamlit as st

st.title("Praktikum 2: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Accord") # membuat caption

st.title("Accord") # membuat title halaman

st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112
""", unsafe_allow_html=True)

# Menambahkan judul ke aplikasi Streamlit
st.title('Expanders')

# --- Mendefinisikan Expander ---
# Membuat sebuah expander (seperti kotak yang dapat dibuka/ditutup)
with st.expander("Streamlit with Python"):
    # Konten di dalam blok 'with' ini akan disembunyikan secara default
    # dan hanya akan ditampilkan ketika pengguna mengklik expander.
    st.write("Develop ML Applications in Minutes!!!")