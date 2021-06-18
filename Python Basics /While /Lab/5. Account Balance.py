income = input()
balance = 0

while income != "NoMoreMoney":
    current_amount = float(income)
    if current_amount < 0:
        print("Invalid operation!")
        break
    balance += current_amount
    print(f"Increase: {current_amount:.2f}")
    income = input()
else:
    print(f'Total: {balance:.2f}')

