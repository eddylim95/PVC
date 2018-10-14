import requests

r = requests.post('https://pvc2018.herokuapp.com/getShopeeJson', json = {'url': 'https://shopee.sg/-Bundle-of-4-Dynamo-Laundry-Detergent-Power-Gel-(2.7L-3L)-i.14134779.186143848'})

print('Posted')

print(r.json())
