import pandas as pd
from bs4 import BeautifulSoup
import requests

Names = []
Description = []
Price = []
# Reviews = []

url = "https://www.airbnb.co.id/s/Bandung--Indonesia/homes?adults=1&place_id=ChIJf0dSgjnmaC4RshXo05MfahQ&refinement_paths%5B%5D=%2Fhomes"

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "lxml")
for i in range(1, 14):
    np = soup.find('a', class_="l1j9v1wn c1ytbx3a dir dir-ltr").get("href")
    cnp = "https://www.airbnb.co.id"+np
    # print(cnp)

    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    names = soup.find_all('div', class_="t1jojoys dir dir-ltr")
    for i in names:
        n = i.text
        Names.append(n)

    desription = soup.find_all('span', class_="t6mzqp7 dir dir-ltr")
    for i in desription:
        n = i.text
        Description.append(n)

    prices = soup.find_all('div', class_="_1jo4hgw")
    for i in prices:
        n = i.text
        Price.append(n)

    # reviews = soup.find_all('span', class_="r1dxllyb dir dir-ltr")
    # for i in reviews:
    #     n = i.text
    #     Reviews.append(n)

# df = pd.DataFrame({"Names": Names, "Description": Description, "Price": Price})
# df.to_csv("airbnb_bandung.csv")