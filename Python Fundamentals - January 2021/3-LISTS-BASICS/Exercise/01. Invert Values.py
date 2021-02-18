items = input().split()
new_list = []

for i in items:
    i = int(i)

    if i > 0:
        i *= -1
        new_list.append(i)
    elif i < 0:
        i *= -1
        new_list.append(i)
    elif i == 0:
        new_list.append(i)

print(new_list)










