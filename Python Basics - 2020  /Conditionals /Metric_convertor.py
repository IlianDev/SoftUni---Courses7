number = float(input())
in_currency = input()
out_currency = input()
result = 0

if in_currency == "mm":
    if out_currency == "cm":
        result = number / 10
    elif out_currency == "m":
        result = number / 1000

elif in_currency == "cm":
    if out_currency == "mm":
        result = number * 10
    elif out_currency == "m":
        result = number/100

elif in_currency == "m":
    if out_currency == "cm":
        result = number * 100
    elif out_currency == "mm":
        result = number * 1000

print(f"{result:.3f}")
