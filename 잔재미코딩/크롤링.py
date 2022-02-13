import requests
from bs4 import BeautifulSoup

res = requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06')
soup = BeautifulSoup(res.content, 'html.parser')
bestlists = soup.select('div.best-list')
bestitems = bestlists[1]
products = bestitems.select('ul > li')

for index, product in enumerate(products):
    title = product.select_one('a.itemname')
    price = product.select_one('div.s-price > strong')
    print (title.get_text(), price.get_text(), title['href'])