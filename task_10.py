profile = {}

n = int(input())
for _ in range(n):
    key, val = input().split()
    profile[key] = val

input()

m = int(input())
for _ in range(m):
    key, val = input().split()
    profile[key] = val

for key in sorted(profile.keys()):
    print(f"{key}: {profile[key]}")
    