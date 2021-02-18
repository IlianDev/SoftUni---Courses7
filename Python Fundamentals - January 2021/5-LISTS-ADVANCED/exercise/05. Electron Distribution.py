number_of_electrons = int(input())
electrons = []
counter = 1

while True:
    if number_of_electrons == 0:
        print(electrons)
        break
    if 2*counter**2 <= number_of_electrons:
        electrons.append(2 * counter ** 2)
        number_of_electrons -= 2 * counter ** 2
    elif number_of_electrons < 2*counter**2:
        electrons.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
    counter += 1
