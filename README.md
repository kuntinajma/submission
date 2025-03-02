# Proyek Analisis Data: Bike Sharing Dataset  

## Deskripsi Proyek  
Proyek ini bertujuan untuk menganalisis pola peminjaman sepeda berdasarkan dataset **Bike Sharing**. Analisis mencakup:  
1. **Perbedaan pola peminjaman antara pelanggan casual dan registered di Q4 2012**  
2. **Jam dengan peminjaman tertinggi dalam sehari dan perbedaannya antara hari kerja dan akhir pekan**  
3. **Analisis lanjutan dengan metode Clustering**  

## Instalasi dan Persiapan  
### 1. Clone Repository  
```bash
git clone https://github.com/kuntinajma/submission.git
cd submission
```

### 2. Buat Virtual Environment (Opsional)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

## Menjalankan Dashboard Secara Lokal  
```bash
streamlit run dashboard/dashboard.py
```
Jika berjalan dengan benar, akan muncul tautan **http://localhost:8501/** untuk melihat dashboard interaktif.  

## Link Deploy  
Dashboard dapat diakses secara online melalui Streamlit Cloud:  
🔗 **[Dashboard Bike Sharing](https://kuntinajmajalia.streamlit.app/)**  

Link ini juga tersimpan di dalam file `url.txt` yang berada di folder utama.  

## Struktur Folder  
```
submission/
│── dashboard/
│   ├── dashboard.py        # Kode utama untuk dashboard Streamlit
│── data/
│   ├── day.csv             # Data harian (day dataset)
│   ├── hour.csv            # Data per jam (hour dataset)
│── notebook.ipynb          # Analisis eksploratif di Jupyter Notebook
│── requirements.txt        # Daftar library yang dibutuhkan
│── url.txt                 # Link deploy Streamlit
│── README.md               # Dokumentasi proyek
```

## Fitur Dashboard  
- Analisis perbedaan peminjaman antara pelanggan casual dan registered  
- Analisis waktu peminjaman tertinggi  
- Clustering jam sibuk dan jam sepi  
