text = input()
counts = {}

for char in text:
    if char.isalpha() and char.islower():
        counts[char] = counts.get(char, 0) + 1

sorted_keys = sorted(counts.keys())

for key in sorted_keys:
    print(f"{key}: {counts[key]}")
