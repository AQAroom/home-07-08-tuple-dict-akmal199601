rgb = (int(input()), int(input()), int(input()))

if rgb.count(rgb[0]) == 3:
    print("Да")
else:
    print("Нет")