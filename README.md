
# Web Scraper Properti OLX Indonesia

Scraper ini digunakan untuk mengumpulkan data listing properti dari OLX.co.id secara otomatis, termasuk informasi seperti judul iklan, harga, lokasi, luas bangunan, luas tanah, tipe properti, dan tanggal posting. Cocok untuk keperluan analisis pasar properti atau data mining regional.

--- 
# Cara Menggunakan
silahan pilih kolasi dan kategori pada website:
 - ![image](https://github.com/user-attachments/assets/a0c8191e-6ba8-46d9-88e9-42e00cf93692)

Setelah itu, copy linknya dan masukkan ke input pada kolom input
 - ![image](https://github.com/user-attachments/assets/b0274a1c-6195-42d5-ad77-e0482e9600fb)
 - ![image](https://github.com/user-attachments/assets/0bb9049c-5f58-4e2e-b547-672b479080ef)
   Jika anda menggunakan streamlit. jika tidak menggunakan streamlit maka cukup copy di terminal






# Fitur

- Scrape listing properti dari kota/kabupaten tertentu di OLX
- Klik otomatis tombol "Load More" sampai semua data termuat
- Filter berdasarkan lokasi yang diambil dari URL
- Ekstraksi detail properti dari masing-masing halaman iklan
- Simpan hasil scraping ke dalam file CSV
- Progres scraping ditampilkan di terminal
- tidak ada duplikad pada saat scrap karena - sudah terfilter pada saat proses scraping

---



## 🛠️ Requirements

Pastikan Python 3 telah terpasang, lalu install dependencies berikut:

```bash
pip install selenium
pip install webdriver-manager
pip install beautifulsoup4
pip install pandas
