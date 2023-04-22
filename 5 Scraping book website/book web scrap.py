from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://books.toscrape.com/catalogue/page-1.html"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "lmxl")
for i in range(1, 10):
    np = soup.find_all('a', class_="next").get("href")
    cnp = "http://books.toscrape.com/catalogue/" + np
    print(cnp)