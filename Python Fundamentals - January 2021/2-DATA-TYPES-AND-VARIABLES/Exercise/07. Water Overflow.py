tank_capacity = 255

n = int(input())
current_tank_capacity = 0

for _ in range(n):
    current_litres = int(input())

    if current_tank_capacity + current_litres > tank_capacity:
        print("Insufficient capacity!")
    else:
        current_tank_capacity += current_litres

print(current_tank_capacity)
