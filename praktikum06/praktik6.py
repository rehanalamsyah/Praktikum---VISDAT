# import
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# header
st.title("Praktikum 6: Visualisasi Data")
st.write("kelompok 8")
st.markdown("""
Muhammad Dzaky Dzulfikar Salim - 0110222187<br>
Rehan Alamsyah Putra - 0110222168<br>
Ihwanul Fikri Ramadhan - 0110222112
""", unsafe_allow_html=True)

# dataset
stores = ['Store A', 'Store B', 'Store C']
male = [120, 150, 130]
female = [100, 130, 120]

# dataset transaksi penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a_sales = [200, 250, 300]
product_b_sales = [150, 300, 200]

# data quarter
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]


# 1 Grafik Stacked Vertical Bar Chart
st .subheader("1. Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label='Male', color='blue')
ax.bar(x, female, label='Female', bottom=male, color='pink')

ax.set_title('Population by Genderand Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)


# 2 Grafik Grouped Horizontal Bar Chart
st .subheader("2. Stacked Vertical Bar Chart dengan Matplotlib")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a_sales, label='Product A', color='cyan')
ax.bar(x, product_b_sales, label='Product B', bottom=product_a_sales, color='green')

ax.set_title('Sales by Product and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)


# 3 Grafik Kustomisasi Stacked Vertical Bar Chart
st.subheader("3. Kustomisasi Stacked Vertical Bar Chart")

for i in range(len(stores)):
    plt.text(i, product_a_sales[i]/2, str(product_a_sales[i]), ha='center', color='black')
    plt.text(i, product_a_sales[i] + product_b_sales[i]/2, str(product_b_sales[i]), ha='center', color='white')
st.pyplot(fig)


# 4 Grafik Multiple Stacked Vertical Bar Chart
st.subheader("4. Multiple Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

# first quarter
ax.bar(x - width/2, q1_male, label='Q1 Male', color='lightblue', width=width)
ax.bar(x - width/2, q1_female, bottom=q1_male, label='Q1 Female', color='lightpink', width=width)

# second quarter
ax.bar(x + width/2, q2_male, label='Q2 Male', color='blue', width=width)
ax.bar(x + width/2, q2_female, bottom=q2_male, label='Q2 Female', color='red', width=width)

ax.set_title('Population by Gender, Store, and Quarter')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)