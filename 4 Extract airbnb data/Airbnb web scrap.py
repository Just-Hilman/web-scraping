import pandas as pd
from bs4 import BeautifulSoup
import requests

Names = []
Description = []
Price = []
Reviews = []

url = "https://www.airbnb.co.id/s/Bandung--Indonesia/homes?adults=1&place_id=ChIJf0dSgjnmaC4RshXo05MfahQ&refinement_paths%5B%5D=%2Fhomes"

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "lxml")

np = soup.find('a', class_="l1j9v1wn c1ytbx3a dir dir-ltr").get("href")
cnp = "https://www.airbnb.co.id"+np
# print(cnp)

url = cnp
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

names = soup.find_all("div", class_="t1jojoys dir dir-ltr")
print(names)