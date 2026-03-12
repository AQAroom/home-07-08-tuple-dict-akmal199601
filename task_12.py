visits = {}

while True:
    city = input().strip()
    if not city:
        break
    visits[city] = visits.get(city, 0) + 1

for city in sorted(visits.keys()):
    print(f"{city}: {visits[city]}")
    