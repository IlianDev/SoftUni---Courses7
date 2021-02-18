def calculate_price(pr, q):
    if pr == "coffee":
        return 1.50 * q
    elif pr == "water":
        return q * 1.00
    elif pr == "coke":
        return 1.40 * q
    elif pr == "snacks":
        return 2 * q


product = input()
quantity = int(input())
result = calculate_price(product, quantity)
print(f"{result:.2f}")