total_budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_1l_price = flour_price * 1.25
milk_250_price = milk_1l_price * 0.25

colored_eggs_count = 0
cozonacs_made = 0

total_cozonac_price = flour_price + eggs_price + milk_250_price

while total_budget >= total_cozonac_price:
    colored_eggs_count += 3
    cozonacs_made += 1
    if cozonacs_made % 3 == 0:
        colored_eggs_count = colored_eggs_count - cozonacs_made + 2

    total_budget -= total_cozonac_price

print(f'You made {cozonacs_made} cozonacs! Now you have {colored_eggs_count} eggs and {total_budget:.2f}BGN left.')
