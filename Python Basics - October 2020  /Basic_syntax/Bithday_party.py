rent_for_hall = int (input())

ceke_price = rent_for_hall * 0.20
drinks_price = ceke_price - 45/100 * ceke_price
animator = 1/3 * rent_for_hall

full_price = rent_for_hall + ceke_price + drinks_price + animator
print(full_price)




