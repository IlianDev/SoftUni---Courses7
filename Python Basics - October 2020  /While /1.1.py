searched_book = input()
next_book = input()
book_counter = 0
isFound = False

while next_book != 'No More Books':
    if next_book == searched_book:
        isFound = True
        break
    book_counter += 1
    next_book = input()
if isFound:  # is True
    print(f'You checked {book_counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {book_counter} books.')
