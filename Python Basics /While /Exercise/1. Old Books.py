searched_book = input()
next_book = input()
book_counter = 0

isFound = False  # Булева променлива, но може да се реши и без булева
# в момента в които булевата се промени от False на True мога да кажа бреик
# означава намерена ли е книгата ами не е вярно значи е фолс
while next_book != "No more books":
    if next_book == searched_book:
        isFound = True
        break
    book_counter += 1  # този брояч е само при неуспешни опити
    next_book = input()
if isFound:  # ако е намерена. Самата булева isFound ни връща  True. Кога ще върне тру. по нагоре сме казали че тя е
    # фосл
    print(f"You checked {book_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")
