# не става този код трябжа да се провери

searched_book = input()
next_book = input()
count_book = 0

while next_book != "No More Books":
    if next_book == searched_book:
        break
        count_book += 1
        next_book = input()
if next_book == searched_book:
    print(f'You checked {count_book} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {count_book} books.')
