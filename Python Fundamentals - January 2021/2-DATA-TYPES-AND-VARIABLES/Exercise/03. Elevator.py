import math
n = int(input())
p = int(input())

number_of_full_courses = int(n / p)

if n % p == 0:
    print(number_of_full_courses)
elif n % p != 0:
    number_of_full_courses += 1
    print(math.floor(number_of_full_courses))
