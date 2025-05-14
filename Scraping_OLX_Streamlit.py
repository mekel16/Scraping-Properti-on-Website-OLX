import streamlit as st
import csv
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

def scrape_olx(url, log):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/").split("/")
    location_part = path_parts[0]
    location_keyword = location_part.split("_")[0].replace("-", " ").lower()

    log.write(f"Keyword lokasi yang digunakan untuk filter: '{location_keyword}'\n")

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            load_more = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@data-aut-id="btnLoadMore"]'))
            )
            load_more.click()
            WebDriverWait(driver, 5).until_not(
                EC.presence_of_element_located((By.CLASS_NAME, "_1GkRk"))
            )
            log.write("Klik Load More berhasil\n")
        except:
            log.write("Tidak ada tombol Load More lagi. Selesai.\n")
            break

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    listings = soup.find_all("li", {"data-aut-id": "itemBox"})
    log.write(f"Total listing ditemukan: {len(listings)}\n")

    base_url = "https://www.olx.co.id"
    all_links = []

    for item in listings:
        try:
            link_tag = item.find("a", href=True)
            ad_link = base_url + link_tag["href"] if link_tag else None
            ad_title = item.find("span", {"data-aut-id": "itemTitle"}).text.strip()
            ad_price = item.find("span", {"data-aut-id": "itemPrice"}).text.strip()
            ad_location = item.find("span", class_="_2VQu4").text.strip()
            tanggal = item.find("span", class_="_2jcGx").text.strip()

            if ad_link and location_keyword in ad_location.lower():
                all_links.append({
                    "title": ad_title,
                    "price": ad_price,
                    "location": ad_location,
                    "link": ad_link,
                    "tanggal": tanggal
                })
            else:
                log.write(f"Skip karena lokasi tidak cocok: {ad_location}\n")
        except Exception as e:
            log.write(f"Error parsing listing awal: {e}\n")
            continue

    scraped_data = []

    for i, listing in enumerate(all_links):
        try:
            driver.get(listing["link"])
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            detail_html = driver.page_source
            detail_soup = BeautifulSoup(detail_html, "html.parser")

            luas_bangunan = detail_soup.find("span", {"data-aut-id": "value_p_sqr_building"})
            luas_bangunan = luas_bangunan.text.strip() if luas_bangunan else ""

            luas_tanah = detail_soup.find("span", {"data-aut-id": "value_p_sqr_land"})
            luas_tanah = luas_tanah.text.strip() if luas_tanah else ""

            tipe_properti = detail_soup.find("span", {"data-aut-id": "value_type"})
            tipe_properti = tipe_properti.text.strip() if tipe_properti else ""

            scraped_data.append([
                listing["title"],
                tipe_properti,
                luas_bangunan,
                luas_tanah,
                listing["price"],
                listing["location"],
                listing["link"],
                listing["tanggal"]
            ])

            log.write(f"[{i+1}/{len(all_links)}] Scraped: {listing['title']}\n")
        except Exception as e:
            log.write(f"Error scraping detail: {e}\n")
            continue

    driver.quit()
    return scraped_data, location_keyword

st.title("📊 Scraper Properti OLX Indonesia")

url_input = st.text_input("Masukkan URL OLX")

if st.button("🚀 Mulai Scrape"):
    log_placeholder = st.empty()

    class Logger:
        def __init__(self, log_placeholder):
            self.log_text = ""
            self.log_placeholder = log_placeholder

        def write(self, msg):
            self.log_text += msg
            self.log_placeholder.text_area("📋 Log Proses", self.log_text, height=200)

    logger = Logger(log_placeholder)

    with st.spinner("Sedang menjalankan scraper..."):
        data, lokasi = scrape_olx(url_input, logger)

    df = pd.DataFrame(data, columns=[
        "Title", "Tipe Properti", "Luas Bangunan", "Luas Tanah", "Price", "Location", "Link", "Tanggal"
    ])

    st.success(f"✅ Sukses scrape {len(df)} data dari OLX untuk lokasi: {lokasi.title()}")
    st.dataframe(df)
    csv = df.to_csv(index=False).encode("utf-8")
    filename = f"Properti - {lokasi.title()}.csv"
    st.download_button("📥 Download CSV", csv, file_name=filename, mime="text/csv")
