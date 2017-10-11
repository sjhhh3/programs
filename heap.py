import heapq

grades = [32, 64, 45, 17, 56, 85, 96]

print(heapq.nlargest(3, grades))

stock = {
    'GOOG' : 520.34,
    'FB' : 83.68,
    'YHOO' : 53.27,
    'APPL' : 77.37,
    'AMZN': 426.23
}
print(heapq.nsmallest(2,zip(stock.values(), stock.keys())))

# print(heapq.nsmallest(2, stocks, key = lambda stock: stock['prince']))     Many key words in dictionary and filter