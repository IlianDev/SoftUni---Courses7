text = input()
sum_total = 0

for symbol in text:
    if symbol == "a":
        sum_total += 1
    elif symbol == "e":
        sum_total += 2
    elif symbol == "i":
        sum_total += 3
    elif symbol == "o":
        sum_total += 4
    elif symbol == "u":
        sum_total += 5

print(sum_total)