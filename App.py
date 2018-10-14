from flask import Flask
from flask import request, jsonify
import sys
from GetShopeeProduct import getShopeeProductJson, getProductShippingCost
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)

logFormatter = logging.Formatter("%(asctime)s [%(filename)s] [%(funcName)s] [%(lineno)d] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

rootLogger.setLevel(logging.INFO)

fileHandler = logging.FileHandler("team.log")
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

@app.route('/getShopeeJson', methods=['POST'])
def getShopeeJson():
    json = request.get_json()
    print(json)

    if json == None:
        return {"Code": 404,
                "Error": "Invalid Post Parameters!" }

    shopeeJson = getShopeeProductJson(json["url"])
    if shopeeJson == None:
        return {"Code": 404,
                "Error": "Unable to retrieve data!" }

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
        modelNamePrice = productName + "," + str(discountedPrice)

    shippingCost = getProductShippingCost(productId, shopId)

    content = {
        "platform": "Shopee",
        "productName": productName,
        "productId": productId,
        "shopId": shopId,
        "imageLink": imageLink,
        "modelNamePrice": modelNamePrice,
        "shippingCost": shippingCost
    }
    #print(content)
    return jsonify(content)

if __name__ == "__main__":
    app.run()
