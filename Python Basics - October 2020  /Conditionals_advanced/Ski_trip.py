days = int(input())
room_type = input()
grade = input()

nights = days - 1
final_price = 0

if room_type == "room for one person":
    final_price = nights * 18

if room_type == "apartment":
    final_price = nights * 25
    if days < 10:
        final_price = final_price - 0.30 * final_price
    elif 10 <= days <= 15:
        final_price = final_price - 0.35 * final_price
    elif days > 15:
        final_price = final_price - 0.5 * final_price

elif room_type == "president apartment":
    final_price = nights * 35
    if days < 10:
        final_price = final_price - 0.10 * final_price
    elif 10 <= days <= 15:
        final_price = final_price - 0.15 * final_price
    elif days > 15:
        final_price = final_price - 0.20 * final_price

if grade == "positive":
    final_price = final_price + 0.25 * final_price
elif grade == "negative":
    final_price = final_price - 0.1 * final_price

print(f"{final_price:.2f}")
