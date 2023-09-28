import json
from time import sleep
import requests
from bs4 import BeautifulSoup


products = {}

for i in range(1, 16):
    url = 'https://zaka-zaka.com/game/new' + f"/page{i}"
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            items = soup.find_all(class_='game-block')
            for item in items:
                if "game-block-more" in item.get("class"):
                    continue
                name = item.find(class_="game-block-name")
                price = item.find(class_="game-block-price")
                products[name.text] = {"price": float(price.text[:-1])}
    sleep(1)


with open("zaka_zaka.json", "w") as f:
    json.dump(products, f,  indent=4)
