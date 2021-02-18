n = int(input())

evens_list = []
odds_list = []
positives_list = []
negatives_list = []

for _ in range(n):
    current_number = int(input())

    if current_number % 2 == 0:
        evens_list.append(current_number)

    if current_number % 2 == 1:
        odds_list.append(current_number)

    if current_number < 0:
        negatives_list.append(current_number)

    if current_number >= 0:
        positives_list.append(current_number)

command = input()

if command == "even":
    print(evens_list)
elif command == "odd":
    print(odds_list)
elif command == "positive":
    print(positives_list)
else:
    print(negatives_list)