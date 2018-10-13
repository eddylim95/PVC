import requests

r = requests.post('http://127.0.0.1:5000/getJson', json = {'url': 'https://shopee.sg/-Bundle-of-4-Dynamo-Laundry-Detergent-Power-Gel-(2.7L-3L)-i.14134779.186143848'})
print('Posted')
