p1 = (float(input()), float(input()))
p2 = (float(input()), float(input()))

dist = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

print(f"{dist:.2f}")