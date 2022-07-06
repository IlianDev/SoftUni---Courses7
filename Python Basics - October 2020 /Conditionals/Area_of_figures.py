figure = input()
import math

if figure == "square":
    a = float(input())
    result = a*a
    print(round(result, 3))
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    result = a*b
    print(round(result, 3))
elif figure == "circle":
    r = float(input())
    result = math.pi * r*r
    print(round(result, 3))
elif figure == "triangle":
    a = float(input())
    h = float(input())
    result = a*h/2
    print(round(result, 3))




