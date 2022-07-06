square_metres = float (input())
price_square_metres = square_metres * 7.61
discount = price_square_metres * 0.18
the_final_price = price_square_metres - discount
print(f"The final price is: {the_final_price} lv.")
print(f"Discount is: {discount} lv.")

