number = float(input())
in_currency = input()
out_currency = input()

#izbiram si mernata edinica na e "mm"
if in_currency == "cm":
    number *= 10
elif in_currency == "m":
    number *= 1000
# do tu kakvoto i da mi e podadeno shte rabotim samo v mm
if out_currency == "cm":
    number /= 10
elif out_currency == "m":
    number /= 1000
#elif out_currency == "mm": tova ne ni trqbva zashtoto rabotim v mm

print(f"{number:.3f}")

