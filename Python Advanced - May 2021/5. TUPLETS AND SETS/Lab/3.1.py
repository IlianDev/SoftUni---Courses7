n = int(input())

names = set()

for x in range(n):
    name = input()
    if name not in names:
        names.add(name)

for y in names:
    print(y)
