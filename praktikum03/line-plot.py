import streamlit as st
import matplotlib.pyplot as plt

# Buat data Sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

# Layout streamlit
st.title("Visualisasi Penjualan Produk") # membuat title halaman
st.sidebar.header("Pengaturan grafik")
options = st.sidebar.selectbox("Pilih tipe Visualisasi:", ("Single Line Plot", "Multiple & Customization", "Jenis garis untuk menunjukan Trend", "Subplot"))

# Identitas Kelompok
st.write("Kelompok : 8 - Matplotlib Line Chart")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112
""", unsafe_allow_html=True)

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A')
    ax.set_title('Product Sales Over Months')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Multiple Line Plot & Customizations
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', marker='o', linestyle='--')
    ax.plot(months, product_B_sales, label='Product B', color='red', marker='x', linestyle='-')

    ax.set_title('Product Sales Over Months')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Jenis garis untuk menunjukan Trend
product_C_sales = [18,22,25,28,32,38,42,45,48,52,56,60]
product_D_sales = [7,9,11,13,16,18,20,23,25,28,30,33]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_C_sales, label='Product C', color='green', linestyle='-.')
    axs.plot(months, product_D_sales, label='Product D', color='purple', linestyle=':')

    axs.set_title('Product Sales Trend Over Months')
    axs.set_xlabel('Month')
    axs.set_ylabel('Sales')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

# Subplot
def subplot_line_plot():
    fig, axs = plt.subplots(2, 1, figsize=(10,8))

    # plot pertama untuk product C
    axs[0].plot(months, product_C_sales, label='Product C', linestyle='-', color='green', marker='d')
    axs[0].set_title('Product Sales C Over Months')
    axs[0].set_xlabel('Month')
    axs[0].set_ylabel('Sales')
    axs[0].legend()
    axs[0].grid(True)

    # plot pertama untuk product D
    axs[1].plot(months, product_D_sales, label='Product D', linestyle='-', color='purple', marker='s')
    axs[1].set_title('Product Sales D Over Months')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Sales')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

# Logika untuk menampilkan visualisasi sesuai menu yang dipilih
if options == "Single Line Plot":
    line_plot()
elif options == "Multiple & Customization":
    customize_line_plot()
elif options == "Jenis garis untuk menunjukan Trend":
    tren_line_plot()
elif options == "Subplot":
    subplot_line_plot()
