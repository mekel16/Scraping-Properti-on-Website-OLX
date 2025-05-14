
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

# Bagaimana code ini bekerja?
 - setelah anda klik mulai scrap atau run code
 - code akan otomatis membuka website OLX yang anda masukkan
 - setelah websitenya benar benar terbuka
 - code akan otomatis melakukan klik pada button(load more)
 - ![image](https://github.com/user-attachments/assets/8897aafd-487c-4f95-a5eb-048ccb724b00)
 - setelah tidak ditemukan lagi tombol load more maka
 - code akan mulai menemukan masing masing box berisi detail dari properti pada website
 - ![image](https://github.com/user-attachments/assets/8b7ba198-5f79-448e-89f0-5c91816aa43a)
 - code akan mengambil harga, tanggal, lokasi, dan judul dari box iklan tersebut
 - nah untuk luas bangunan dan luas tanah didapatkan pada saat code melakukan klik pada box iklan lalu menuju ke detail yang lebih banyak
 - ![image](https://github.com/user-attachments/assets/4315a5ef-5da6-4f0b-b27a-d677097a0c93)
 - hal tersebut dilakukan untuk masing masing box yang tertera di layar/website








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
