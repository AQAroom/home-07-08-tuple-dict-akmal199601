grades_dict = {}

while True:
    line = input()
    if not line:
        break

    parts = line.split()
    subject = parts[0]
    grade = int(parts[1])
    grades_dict[subject] = grade

if grades_dict:
    average = sum(grades_dict.values()) / len(grades_dict)
    print(f"{average:.2f}")
