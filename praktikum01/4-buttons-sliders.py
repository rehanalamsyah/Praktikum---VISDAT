import streamlit as st
import time


st.title("Praktikum 1: Visualisasi Data") # membuat title halaman
st.caption("Bagian 2: Button dan Slider") # membuat caption

st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112

""", unsafe_allow_html=True)

st.title("Creating a Button") # Membuat Tombol

# Defining a Button
button = st.button('Click Here') # Membuat tombol dengan label 'Click Here'

if button:
    st.write('You have clicked the Button') # Menampilkan teks jika tombol diklik
else:
    st.write('You have not clicked the Button') # Menampilkan teks jika tombol tidak diklik

st.title("Creating Radio Buttons") # Membuat Radio Button

# Defining Radio Button
gender = st.radio(
    "Select your gender:",
    ('Male', 'Female', 'Others')
) # Membuat radio

# Defining Radio Button dengan opsi
if gender == 'Male':
    st.write("You have selected Male.") # Menampilkan teks jika opsi Male dipilih
elif gender == 'Female':
    st.write("You have selected Female.") # Menampilkan teks jika opsi Female dipilih
else:
    st.write("You have selected Others.") # Menampilkan teks jika opsi Others dipilih

st.title("Creating Checkboxes") # Membuat Checkbox

st.write("Select your Hobbies:") # Menampilkan teks

# Defining Checkboxes
check_1 = st.checkbox('Books') # Membuat checkbox dengan label 'Books'
check_2 = st.checkbox('Movies') # Membuat checkbox dengan label 'Movies'
check_3 = st.checkbox('Sports') # Membuat checkbox dengan label 'Sports'

st.title("Creating Dropdown") # Membuat Dropdown

# Defining Dropdown
hobby = st.selectbox(
    'Choose your hobby:',
    ('Books', 'Movies', 'Sports')
) # Membuat dropdown dengan opsi

st.title("Creating Multi-Select with Pre-Selection") # Membuat Multi-Select dengan Pre-Selection

# Defining Multi-Select
selected = st.multiselect(
    "Select your Hobbies:",
    ['Cooking', 'Watching Movies/TV Series', 'Playing', 'Reading', 'Hiking'],
    ['Reading', 'Playing']
) # Membuat multi-select dengan opsi dan pre-seleksi

st.write("You selected:", selected) # Menampilkan opsi yang dipilih

st.title("Download Button") # Membuat Tombol Download

# Download Button for image
download_btn = st.download_button(
    label="Download Image",
    data=open("D:/1.jpeg", "rb"),
    file_name="my_image.jpeg",
    mime="image/jpeg"
) # Membuat tombol download untuk gambar


st.title("Progress Bar") # Membuat Progress Bar

# Defining Progress Bar
download = st.progress(0)

for percent in range(100):
    time.sleep(0.1)
    download.progress(percent + 1)

st.write("Download Complete!") # Menampilkan teks setelah progress bar selesai


st.title("Spinner") # Membuat Spinner

# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5) # Simulasi proses yang memakan waktu

st.write("Hello Data Scientists!") # Menampilkan teks setelah spinner selesai
