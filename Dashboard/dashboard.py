import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# File uploader for CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Load data if a file is uploaded
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding='utf-8')

# Convert 'mnth' to month names
data['mnth'] = pd.to_datetime(data['mnth'], format='%m').dt.month_name()

# Dashboard Title
st.title("Bike Riding Analysis Dashboard")

# Pertanyaan 1: Bulan mana yang mencatat jumlah pesanan bike riding tertinggi selama 4 musim?
st.header("Bulan dengan Pesanan Tertinggi dalam 4 Musim")

seasonal_orders = data.groupby('season')['cnt'].sum().reset_index()
st.bar_chart(seasonal_orders.set_index('season'))

# Pertanyaan 2: Bulan mana yang mencatat jumlah pesanan bike riding tertinggi dalam 1 tahun?
st.header("Bulan dengan Pesanan Tertinggi dalam Satu Tahun")

monthly_orders = data.groupby('mnth')['cnt'].sum().reset_index()
highest_month = monthly_orders.loc[monthly_orders['cnt'].idxmax()]
st.write(f"Bulan dengan pesanan tertinggi: {highest_month['mnth']} dengan {highest_month['cnt']} pesanan.")

# Plot
fig, ax = plt.subplots()
ax.bar(monthly_orders['mnth'], monthly_orders['cnt'])
plt.xticks(rotation=90)
st.pyplot(fig)

# Pertanyaan 3: Hubungan antara kelembapan dan total pesanan bike riding dalam 1 tahun
st.header("Hubungan antara Kelembapan dan Total Pesanan Bike Riding")

# Scatter plot kelembapan vs total pesanan
fig, ax = plt.subplots()
ax.scatter(data['hum'], data['cnt'], alpha=0.5)
ax.set_xlabel('Kelembapan')
ax.set_ylabel('Jumlah Pesanan')
ax.set_title('Hubungan Kelembapan dan Pesanan')
st.pyplot(fig)
