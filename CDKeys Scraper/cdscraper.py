import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.cdkeys.com/pc'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
oldPrices = soup.select('span[data-price-type="oldPrice"] span')
products = soup.select('li.product-item')

# loop through products

for i in range(len(products)):
    # convert the data in the html attributes to json
    prod = json.loads(products[i]['data-impression'])

    # print the product info
    print(f"{prod['name']} - ${prod['price']} - {oldPrices[i].text}")
