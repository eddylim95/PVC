from flask import Flask
from flask import request, jsonify
import sys
from GetShopeeProduct import getShopeeProductJson

app = Flask(__name__)

@app.route('/getJson', methods=['POST'])
def getJson():
    json = request.get_json()
    print(json)

    shopeeJson = getShopeeProductJson(json["url"])
    productId = shopeeJson["item"]["itemid"]
    shopId = shopeeJson["item"]["shopid"]
    productName = shopeeJson["item"]["name"]

    imageLink = "https://cf.shopee.sg/file/" + shopeeJson["item"]["image"]
    print(imageLink)

    models = shopeeJson["item"]["models"]

    # Shopee prices are x100000, e.g. $3.80 is 380000
    shopeePriceNormalizeConstant = 100000
    #originalPrice = float(shopeeJson["item"]["price_before_discount"]) / shopeePriceNormalizeConstant
    discountedPrice = float(shopeeJson["item"]["price_min"]) / shopeePriceNormalizeConstant

    modelNamePrice = ""
    if len(models) > 0:
        for i in range(0, len(models)):
            modelNamePrice += models[i]["name"] + "," + str(models[i]["price"] / shopeePriceNormalizeConstant) + "|"
        modelNamePrice = modelNamePrice[:-1]
    else:
        modelNamePrice = [productName + "," + str(discountedPrice)]

    content = {
        "productName": productName,
        "productId": productId,
        "shopId": shopId,
        "imageLink": imageLink,
        "modelNamePrice": modelNamePrice
    }
    print(content)
    return jsonify(content)

app.run()