import requests

r = requests.post('http://127.0.0.1:5000/getShopeeJson', json = {'url': 'https://shopee.sg/Fannai-Men-Hoodie-Casual-Sportswear-Thin-Hoody-Zipper-Long-sleeve-Sweatshirt-i.40981095.650119448'})

print('Posted')

print(r.json())
