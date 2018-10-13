import requests

def getShopeeProductJson(url):
    shopeeBaseUrl = "https://shopee.sg"
    urlParts = url.split(".")
    shopId = urlParts[-2]
    productId = urlParts[-1]
    getUrl = shopeeBaseUrl + "/api/v2/item/get?itemid=" + productId + "&shopid=" + shopId
    r = requests.get(getUrl)
    print(r)
    return r.json()

    #r = requests.post('http://127.0.0.1:5000/', json = {'data': 'test'})
    #print('Posted')
