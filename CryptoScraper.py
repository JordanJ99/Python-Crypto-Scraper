from urllib.request import urlopen as req
from bs4 import BeautifulSoup

rawurl = 'https://coinmarketcap.com/'
page = req(rawurl)
page_html = page.read()
page.close()
page_soup = BeautifulSoup(page_html, "html.parser")
table = page_soup.find(id="currencies")
table2 = table.tbody
crypto_containers = table2.find_all('tr')

name_Array = []
price_array = []
#print("Printing all Cryptocurrency names:")
for container in crypto_containers:
    #names = container.find_all("td", {"class": "no-wrap currency-name"})
    cryptoNames = container.findAll("a", {"class": "currency-name-container link-secondary night-mode-bold"})
    name = cryptoNames[0].string
    name_Array.append(name)

for container in crypto_containers:
    cryptoPrices = container.findAll("a", {"class": "price"})
    price = cryptoPrices[0].string
    price_array.append(price)

print("Printing all Cryptocurrency name and prices:")

for i in range(len(price_array)):
    print(name_Array[i], "  ",price_array[i])