# import library yang dibutuhkan
import streamlit as st

# text element
# header - untuk membuat tulisan header
st.header("Ini adalah Header") # membuat header besar
st.subheader("Ini adalah Subheader") # membuat subheader
st.text("Ini adalah Text biasa tanpa format") # membuat text biasa
st.markdown("**ini teks bold** dan *ini teks italic*") # membuat text dengan format markdown
st.caption("Ini adalah caption") # membuat caption
st.title("Ini adalah Title") # membuat title halaman

st.write("Kelompok : 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112

""", unsafe_allow_html=True)
#coba mandiri 
#tuliskan:
# 1. judul praktikum pakai title() = praktikum 1 Visualisasi Data
# 2. Bagian praktikum pakai subheader() = Bagian 1: Text Elements
# 3. Nama lengkap anggota - nim pakai markdown multibaris """"

# Bagian 2: Menampilkan Rumus (letex)
st.header("Displaying LaTeX")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''')
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''')


st.header("Displaying Code")
st.subheader("Python Code")

code = '''
def hello():
    print("Hello, Streamlit!")
'''

st.code(code, language='python')

st.subheader("JavaScript Code")
st.code("""
public class GFG {
        public static void main(String args[]) {
            System.out.println("Hello, Streamlit!");
        }
}
""", language='java')
# Fungsi st.code() digunakan untuk menampilkan kode program dengan format yang rapi dan mudah dibaca.

st.subheader("Javascript Code")
st.code("""
<p id="demo"></p>
<script>
try {
        addalert("Welcome guest!"); // kesalahan ketik (addalert)
        sengaja dibuat untuk menimbulkan error
}
catch(err) {
        document.getElementById("demo").innerHTML = err.message; //
        menampilkan pesan error di elemen HTML dengan id="demo"
}
</script>
""", language='javascript')