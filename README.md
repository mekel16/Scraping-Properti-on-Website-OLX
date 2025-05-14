# Scraping-Properti-on-Website-OLX

# 🏠 Web Scraper Properti OLX Indonesia

Scraper ini digunakan untuk mengumpulkan data listing properti dari [OLX.co.id](https://www.olx.co.id) secara otomatis, termasuk informasi seperti judul iklan, harga, lokasi, luas bangunan, luas tanah, tipe properti, dan tanggal posting. Cocok untuk keperluan analisis pasar properti atau data mining regional.

---

## 🚀 Fitur

- Scrape listing properti dari kota/kabupaten tertentu di OLX
- Klik otomatis tombol **"Load More"** sampai semua data termuat
- Filter berdasarkan **lokasi** yang diambil dari URL
- Ekstraksi detail properti dari masing-masing halaman iklan
- Simpan hasil scraping ke dalam file **CSV**
- Progres scraping ditampilkan di terminal

---

## 🛠️ Requirements

Pastikan Python 3 telah terpasang, lalu install dependencies berikut:

```bash
pip install selenium
pip install webdriver-manager
pip install beautifulsoup4
pip install pandas
