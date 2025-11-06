import streamlit as st
import base64
from PIL import Image


st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112

""", unsafe_allow_html=True)

st.write("Munculkan Gambar Tunggal")
# Menampilkan gambar dengan menentukan path
st.image("D:/1.jpeg")
# Keterangan gambar
st.write("ini gambar pinguin")


st.write("Menampilkan Beberapa Gambar")
# Daftar gambar hewan
animal_images = [
    'D:/1.jpeg',
    'D:/2.jpeg',
    'D:/3.jpeg',
    'D:/4.jpeg',
    'D:/5.jpeg'
]

# Menampilkan beberapa gambar dengan lebar 150
st.image(animal_images, width=150)
# Keterangan gambar
st.write("menampilkan background")

# Fungsi untuk menjadikan gambar sebagai background
def add_local_background_image(image):
    with open(image, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read())
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("menampilkan background image")

st.write("Background Image")
# Memanggil fungsi dengan gambar lokal
add_local_background_image('D:/background.jpeg')

# Membuka gambar asli dari folder lokal
original_image = Image.open("D:/5.jpeg")

# Menampilkan gambar asli
st.title("Original Image")
st.image(original_image)

# Mengubah ukuran gambar menjadi 600x400
resized_image = original_image.resize((600, 400))

# Menampilkan gambar yang sudah diubah ukurannya
st.title("Resized Image")
st.image(resized_image)