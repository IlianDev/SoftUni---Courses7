while True:
    line = input()
    if line == "End":
        break

    destination = line
    needed_money = float(input())
    saved_money = 0
    while saved_money < needed_money:
        current_saved_money = float(input())
        saved_money += current_saved_money
    print(f"Going to {destination}!")

