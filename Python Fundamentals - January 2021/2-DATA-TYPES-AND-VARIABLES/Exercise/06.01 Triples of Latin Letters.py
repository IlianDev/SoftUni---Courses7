num = int(input())

for j in range(97, 97 + num):
    for k in range(97, 97 + num):
        for l in range(97, 97 + num):
            print(f"{(chr(j))}{chr(k)}{chr(l)}")
print()