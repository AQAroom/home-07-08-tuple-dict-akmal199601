prices = {}

while True:
    line = input()
    if not line:
        break

    parts = line.split()
    name = parts[0]
    price = int(parts[1])
    prices[name] = price

if prices:
    most_expensive = max(prices, key=prices.get)
    print(most_expensive)
