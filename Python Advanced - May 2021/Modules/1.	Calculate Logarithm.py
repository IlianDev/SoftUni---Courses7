from math import log

num = int(input())
base = input()

if base == "natural":
    print(log(num))
else:
    print(log(num, int(base)))