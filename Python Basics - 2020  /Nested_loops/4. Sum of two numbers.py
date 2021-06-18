start = int(input())
end = int(input())
magic_number = int(input())

found_combination = False
counter = 0

for first_number in range(start, end+1):
    for second_number in range(start, end+1):
        counter += 1
        if first_number+second_number == magic_number:
            found_combination = True
            print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
            break

    if found_combination:
        break

if not found_combination:
    print(f"{counter} combinations - neither equals {magic_number}")

