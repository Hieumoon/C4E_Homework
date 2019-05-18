prices = {
    "banana": 4, 
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for k, v in prices.items():
    print(k)
    print("price:", prices[k])
    print("price:", stock[k])

total = 0
for k in prices:
    total = total + prices[k]*stock[k]
print()
print("If selling all of your food, you would make total money:", total, "$")
