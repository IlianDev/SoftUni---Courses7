first_e = int(input())
second_e = int(input())
third_e = int(input())
people_count = int(input())

people_per_hour = first_e + second_e + third_e

hours = 0

while people_count > 0:
    hours += 1
    people_count -= people_per_hour

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")
