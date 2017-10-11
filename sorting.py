
stock = {
    'GOOG' : 520.34,
    'FB' : 83.68,
    'YHOO' : 53.27,
    'APPL' : 77.37,
    'AMZN': 426.23
}


print(sorted(zip(stock.values(), stock.keys()))) # min, max, sorted
'''

from PIL import Image # image process interpreter

img = Image.open("1.jpg")
print(img.size)
print(img.format)

img.show()
'''