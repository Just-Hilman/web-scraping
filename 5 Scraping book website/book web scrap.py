from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://books.toscrape.com/catalogue/page-1.html"
r = requests.get(url)
print(r)