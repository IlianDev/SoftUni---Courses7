budget_film = float(input())
number_statists = int(input())
price_dress_1_statist = float(input())

sum_dekor = budget_film * 0.1
sum_dress = number_statists * price_dress_1_statist

if number_statists > 150:
    sum_dress = sum_dress - (sum_dress * 0.1)

total_sum_film = sum_dress + sum_dekor
money_waste = abs(total_sum_film - budget_film)

if total_sum_film > budget_film:
    print("Not enough money!")
    print(f"Wingard needs {money_waste:.2f} leva more.")

elif total_sum_film <= budget_film:
    print("Action!")
    print(f"Wingard starts filming with {money_waste:.2f} leva left.")
