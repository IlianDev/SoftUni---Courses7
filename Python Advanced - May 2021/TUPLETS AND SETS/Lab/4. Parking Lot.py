n = int(input())

cars = set()

for x in range(n):
    command, number_car = input().split(", ")
    if command == "IN":
        cars.add(number_car)
    else:
        cars.remove(number_car)

if not cars:
    print("Parking Lot is Empty")

else:
    [print(car) for car in cars]