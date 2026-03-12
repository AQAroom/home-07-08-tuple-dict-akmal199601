password = input()
n = int(input())
requirements = {}

for _ in range(n):
    req, val = input().split()
    requirements[req] = val

is_valid = True

if "мин_длина" in requirements:
    if len(password) < int(requirements["мин_длина"]):
        is_valid = False

if is_valid and requirements.get("цифры") == "да":
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        is_valid = False

if is_valid and requirements.get("заглавные") == "да":
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        is_valid = False

print("Да" if is_valid else "Нет")
