import os
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load dataset
day_df = pd.read_csv(os.path.join(BASE_DIR, "main_day.csv"), parse_dates=["dteday"])
hour_df = pd.read_csv(os.path.join(BASE_DIR, "main_hour.csv"))

# ---- HEADER ----
st.title("Proyek Analisis Data: Bike Sharing Dataset")
st.markdown("""
- **Nama:** Kunti Najma Jalia  
- **Email:** kuntinajma@gmail.com  
- **ID Dicoding:** MC466D5X1782  
""")

# ---- SIDEBAR ----
st.sidebar.title("Pilih Analisis:")
option = st.sidebar.radio(
    "Pilih pertanyaan analisis:",
    [
        "Bagaimana perbedaan pola peminjaman antara pelanggan casual dan registered di Q4 2012?",
        "Pada jam berapa peminjaman sepeda paling tinggi dalam sehari, dan bagaimana perbedaannya antara hari kerja dan akhir pekan?",
        "Analisis Lanjutan Dengan Metode Clustering"
    ]
)

# ---- ANALISIS 1: Perbandingan Casual vs Registered di Q4 2012 ----
if option == "Bagaimana perbedaan pola peminjaman antara pelanggan casual dan registered di Q4 2012?":
    st.subheader("Perbandingan Pola Peminjaman (Casual vs Registered) - Q4 2012")

    # Filter data Q4 2012
    q4_2012 = day_df[(day_df["dteday"].dt.year == 2012) & (day_df["dteday"].dt.month.isin([10, 11, 12]))].copy()

    # Rolling average (7 hari) untuk tren lebih smooth
    q4_2012["casual_avg"] = q4_2012["casual"].rolling(window=7, min_periods=1).mean()
    q4_2012["registered_avg"] = q4_2012["registered"].rolling(window=7, min_periods=1).mean()

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=q4_2012["dteday"], y=q4_2012["casual_avg"], label="Casual", color="red", linewidth=2, ax=ax)
    sns.lineplot(x=q4_2012["dteday"], y=q4_2012["registered_avg"], label="Registered", color="blue", linewidth=2, ax=ax)
    
    ax.set_title("Tren Peminjaman Sepeda Harian (Casual vs Registered) - Q4 2012", fontsize=14, fontweight="bold")
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Peminjaman")
    plt.xticks(rotation=45)
    
    st.pyplot(fig)

# ---- ANALISIS 2: Peminjaman Sepeda Berdasarkan Jam dan Hari ----
elif option == "Pada jam berapa peminjaman sepeda paling tinggi dalam sehari, dan bagaimana perbedaannya antara hari kerja dan akhir pekan?":
    st.subheader("Distribusi Peminjaman Sepeda Berdasarkan Jam dan Hari")

    # Kategorikan hari kerja dan akhir pekan
    hour_df["day_type"] = hour_df["weekday"].apply(lambda x: "Weekday" if x < 5 else "Weekend")

    # Hitung rata-rata peminjaman per jam untuk tiap kategori hari
    hourly_avg = hour_df.groupby(["hr", "day_type"])["cnt"].mean().reset_index()

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="hr", y="cnt", hue="day_type", data=hourly_avg, palette={"Weekday": "blue", "Weekend": "orange"}, ax=ax)
    
    ax.set_title("Peminjaman Sepeda Berdasarkan Jam dan Hari", fontsize=14, fontweight="bold")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Peminjaman")
    
    st.pyplot(fig)

# ---- ANALISIS 3: Clustering (Pengelompokan Berdasarkan Jam Sibuk & Jam Sepi) ----
elif option == "Analisis Lanjutan Dengan Metode Clustering":
    st.subheader("Pengelompokan Berdasarkan Jam Sibuk dan Jam Sepi")

    # Tentukan kategori jam sibuk & jam sepi berdasarkan threshold tertentu
    peak_hours = [7, 8, 17, 18, 19]  # Jam sibuk
    hour_df["hour_category"] = hour_df["hr"].apply(lambda x: "Peak Hours" if x in peak_hours else "Off-Peak Hours")

    # Hitung rata-rata peminjaman per jam
    hourly_avg = hour_df.groupby(["hr", "hour_category"])["cnt"].mean().reset_index()

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="hr", y="cnt", hue="hour_category", data=hourly_avg, palette={"Peak Hours": "red", "Off-Peak Hours": "green"}, ax=ax)
    
    ax.set_title("Distribusi Peminjaman Sepeda Berdasarkan Jam Sibuk dan Jam Sepi", fontsize=14, fontweight="bold")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Peminjaman")
    
    st.pyplot(fig)