import streamlit as st
import pandas as pd
import datetime

st.title("Praktikum 1: Visualisasi Data") # membuat title halaman
st.caption("Bagian 5: Bagian Form") # membuat caption

st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112

""", unsafe_allow_html=True) # memungkinkan penggunaan HTML di markdown

# Creating Text Area
input_text = st.text_area("Enter your Review") # Membuat area teks untuk input ulasan

# Printing entered text
st.write("You entered:\n", input_text) # Menampilkan teks yang dimasukkan


# Create number input
st.number_input("Enter your Number") # Membuat input angka


# Create number input
num = st.number_input("Enter your Number", 0, 10, 5) # Membuat input angka dengan batasan dan nilai default
st.write("Min. Value is 0, Max. Value is 10") # Menampilkan nilai minimum dan maksimum
st.write("Default Value is 5, Step Size value is 2") # Menampilkan nilai default dan langkah
st.write("Total value after adding Number entered with step value is:", num) # Menampilkan hasil penjumlahan

# Time
st.title("Time")  # Membuat judul untuk bagian waktu
# Defining Time Function
st.time_input("Select Your Time") # Membuat input waktu


st.title("Date") # Membuat judul untuk bagian tanggal
# Defining Date Function
st.date_input("Select Date") # Membuat input tanggal


st.title("Date") # Membuat judul untuk bagian tanggal dengan batasan
# Defining Date Function
d = st.date_input("Select Your Date", value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1))
st.write(d) # Menampilkan tanggal yang dipilih

# Membuat judul untuk bagian Text Box
st.title("Text Box") # Membuat judul untuk bagian Text Box
# Creating Text box
name = st.text_input("Enter your Name") # Membuat input teks untuk nama
st.write("Your Name is", name) # Menampilkan nama yang dimasukkan

st.title("Select Color") # Membuat judul untuk bagian pemilihan warna
# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code) # Menampilkan kode warna yang dipilih


st.title("Upload CSV") # Membuat judul untuk bagian unggah CSV

# Upload dataset
data_file = st.file_uploader("Upload CSV", type=["csv"]) # Membuat komponen untuk mengunggah file CSV
details = st.button("Check Details")    # Membuat tombol untuk memeriksa detail file

if data_file is not None:
    file_details = {
        "File Name": data_file.name,
        "File Type": data_file.type,
        "File Size": data_file.size
    }
    st.write(file_details)
    df = pd.read_csv(data_file)
    st.dataframe(df)
else:
    st.write("No CSV file is uploaded") # Menampilkan pesan jika tidak ada file yang diunggah


my_form = st.form(key='form') # Membuat form dengan kunci 'form'
a = my_form.text_input(label='Enter any text') # Menambahkan input teks ke dalam form
submit_button = my_form.form_submit_button(label='Submit') # Menambahkan tombol submit ke dalam form

st.write(a) # Menampilkan teks yang dimasukkan dalam form
