import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Data Dummy
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],  # Menambahkan kolom 'Suhu' di sini
    'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100],
    'Penjualan_weekdays': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_weekend': [60, 70, 80, 100, 110, 120, 140, 160, 200]
}

# Konversi data ke DataFrame
df = pd.DataFrame(data)

# layout utama
st.title("Praktikum 5: Visualisasi Data")  # membuat title halaman
st.sidebar.header("Bagian 5: Scatter Plot")  # membuat caption

# Menu di sidebar
option = st.sidebar.selectbox(
    'Pilih Jenis Scatter Plot:',
    (
        "Basic Scatter Plot",
        "Kustomisasi scatter plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )
)

# Identitas Kelompok
st.caption("Praktikum 5 - Matplotlib Scatter Plot")
st.markdown("""
Kelompok : 8<br>
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112
""", unsafe_allow_html=True)  # memungkinkan penggunaan HTML di markdown

# 1. Basic Scatter Plot
def basic_scatter_plot():
    st.subheader("Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(df['Suhu'], df['Penjualan_Cokelat'])
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es krim')
    st.pyplot(fig)

# 2. Kustomisasi scatter plot
def custom_scatter_plot():
    st.subheader("Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(df['Suhu'], df['Penjualan_Cokelat'], color='orange', s=100, edgecolors='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es krim')
    ax.grid(True)
    st.pyplot(fig)

# 3. Multiple Scatter Plot
def multiple_scatter_plot():
    st.subheader("Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(df['Suhu'], df['Penjualan_weekdays'], color='brown', label='Cokelat', s=80)
    ax.scatter(df['Suhu'], df['Penjualan_weekend'], color='yellow', label='Vanila', s=80)
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es krim')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# 4. Analisis Scatter Plot
def scatter_3_variables():
    st.subheader("Analisis Scatter Plot dengan 3 Variabel")
    # opsi jenis es krim
    jenis_esskrim = st.selectbox('Pilih Jenis Es krim:', ['Cokelat', 'Vanila', 'Stroberi'])

    # logika untuk opsi jenis eskrim berdasarkan pilihan
    if jenis_esskrim == 'Cokelat':
        penjualan = df['Penjualan_Cokelat']
    elif jenis_esskrim == 'Vanila':
        penjualan = df['Penjualan_Vanila']
    else:
        penjualan = df['Penjualan_Stroberi']

    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    # scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], cmap='coolwarm', s=100, alpha=0.7)

    # styling
    ax.set_title(f'Hubungan Penjualan Es krim {jenis_esskrim} vs dengan Suhu dan Kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es krim ({jenis_esskrim})')
    fig.colorbar(scatter, label='Kelembapan')

    st.pyplot(fig)

    # ringkasan hubungan
    st.subheader("Analisis Hubungan")
    st.write(f'Grafik menunjukan hubungan antara suhu, kelembapan, dan penjualan es krim {jenis_esskrim}.')

# routing berdasarkan pilihan menu sidebar
if option == "Basic Scatter Plot":
    basic_scatter_plot()
elif option == "Kustomisasi scatter plot":
    custom_scatter_plot()
elif option == "Multiple Scatter Plot":
    multiple_scatter_plot()
elif option == "Analisis Scatter Plot":
    scatter_3_variables()

