import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#judul
st.title("Praktikum 7: Horizontal Bar Chart")
st.subheader("Horizontal Bar Chart dan Stacked Horizontal Bar Chart")

# identitas kelompok
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112
""", unsafe_allow_html=True)

# dataset
brand = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [350, 420, 300, 200]
sales_2024 = [380, 450, 320, 300]

# atur posisi y
y=np.arange(len(brand))
bar_width=0.4

# filter kategori
kategori = st.selectbox(
    "Pilih Kategori Penjualan:",
    [' Basic Chart', 'Kustomisasi Grafik', 'Multiple Chart']
)

# bacis bar chart
if kategori == ' Basic Chart':
    st.subheader("1. Horizontal Bar Chart Sederhana")
    fig1, ax1 = plt.subplots()

# grafik batang horizontal
    ax1.set_yticks(y)
    ax1.set_yticklabels(brand)
    ax1.set_title('Horizontal Bar Chart - 2023')
    ax1.set_xlabel('Jumlah Penjualan')
    ax1.set_ylabel('Merk')
    ax1.barh(y, sales_2023, color='skyblue')
    st.pyplot(fig1)

# Stacked bar chart
    st.subheader("2. Stacked Horizontal Bar Chart")
    fig2, ax2 = plt.subplots()
    ax2.set_yticks(y)
    ax2.set_yticklabels(brand)
    ax2.set_title('Stacked Horizontal Bar Chart - 2023 vs 2024')
    ax2.set_xlabel('Jumlah Penjualan')
    ax2.set_ylabel('Merk')
    ax2.barh(y, sales_2023, label='2023', color='lightblue')
    ax2.barh(y, sales_2024, left=sales_2023, label='2024', color='lightcoral')
    ax2.legend()
    st.pyplot(fig2)

# kustomisasi bar chart
elif kategori == 'Kustomisasi Grafik':
    st.subheader("3. Horizontal Bar Chart dengan Kustomisasi")
    fig3, ax3 = plt.subplots()

    # grafik batang horizontal dengan kustomisasi
    ax3.set_yticks(y)
    ax3.set_yticklabels(brand)
    ax3.set_title('Horizontal Bar Chart - 2023 dengan Kustomisasi')
    ax3.set_xlabel('Jumlah Penjualan')
    ax3.set_ylabel('Merk')
    ax3.barh(y, sales_2023, color='lightgreen', edgecolor='black')
    ax3.grid(axis='x', linestyle='--', alpha=0.6)
     # label nilai
    for i, v in enumerate(sales_2023):
       ax3.text(v + 5, i, str(v), va='center')

    st.pyplot(fig3)

    # Stacked
    st.subheader("3. Stacked Horizontal Bar Chart dengan Kustomisasi")
    fig4, ax4 = plt.subplots()

    # grafik batang horizontal dengan kustomisasi
    ax4.set_yticks(y)
    ax4.set_yticklabels(brand)
    ax4.set_title('Horizontal Bar Chart - 2023 dengan Kustomisasi')
    ax4.set_xlabel('Jumlah Penjualan')
    ax4.set_ylabel('Merk')
    ax4.barh(y, sales_2023, label='2023', color='lightgreen', edgecolor='black')
    ax4.barh(y, sales_2024, label='2024', left=sales_2023, color='salmon', edgecolor='black')
    ax4.grid(axis='x', linestyle='--', alpha=0.6)
    ax4.legend()
    st.pyplot(fig4)

# multiple bar chart
else:
    st.subheader("Horizontal Bar Chart Sederhana")
    fig5, ax5 = plt.subplots()
    ax5.set_yticks(y)
    ax5.set_yticklabels(brand)
    ax5.set_title('Multiple Horizontal Bar Chart - 2023')
    ax5.set_xlabel('Jumlah Penjualan')
    ax5.set_ylabel('Merk')
    ax5.barh(y - bar_width/2, sales_2023, height=bar_width, label='2023', color='skyblue')
    ax5.barh(y + bar_width/2, sales_2024, height=bar_width, label='2024', color='lightcoral')
    ax5.grid(axis='x', linestyle='--', alpha=0.6)
    ax5.legend()
    st.pyplot(fig5)

# Stacked bar chart

    st.subheader(" Multiple Stacked Horizontal Bar Chart")
    fig6, ax6 = plt.subplots()
    ax6.set_yticks(y)
    ax6.set_yticklabels(brand)
    ax6.set_title('Stacked Horizontal Bar Chart')
    ax6.set_xlabel('Jumlah Penjualan')
    ax6.set_ylabel('Merk')
    ax6.barh(y, sales_2023, label='2023')
    ax6.barh(y, sales_2024, left=sales_2023, label='2024')
    ax6.legend()
    st.pyplot(fig6)

# kustomisasi bar chart

    st.subheader("2. Horizontal Bar Chart dengan Kustomisasi")
    fig7, ax7 = plt.subplots()

    # grafik batang horizontal dengan kustomisasi
    ax7.set_yticks(y)
    ax7.set_yticklabels(brand)
    ax7.set_title('Horizontal Bar Chart - 2023 dengan Kustomisasi')
    ax7.set_xlabel('Jumlah Penjualan')
    ax7.set_ylabel('Merk')
    ax7.barh(y, sales_2023, color='lightgreen', edgecolor='black')
    ax7.grid(axis='x', linestyle='--', alpha=0.6)
     # label nilai
    for i, v in enumerate(sales_2023):
       ax7.text(v + 5, i, str(v), va='center')

    st.pyplot(fig7)

    # Stacked
    st.subheader("3. Stacked Horizontal Bar Chart dengan Kustomisasi")
    fig4, ax4 = plt.subplots()

    # grafik batang horizontal dengan kustomisasi
    ax4.set_yticks(y)
    ax4.set_yticklabels(brand)
    ax4.set_title('Horizontal Bar Chart - 2023 dengan Kustomisasi')
    ax4.set_xlabel('Jumlah Penjualan')
    ax4.set_ylabel('Merk')
    ax4.barh(y, sales_2023, label='2023', color='lightgreen', edgecolor='black')
    ax4.barh(y, sales_2024, label='2024', left=sales_2023, color='salmon', edgecolor='black')
    ax4.grid(axis='x', linestyle='--', alpha=0.6)
    ax4.legend()
    st.pyplot(fig4)