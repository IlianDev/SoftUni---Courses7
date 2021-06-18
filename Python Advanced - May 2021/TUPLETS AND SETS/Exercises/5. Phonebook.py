data = input()

phone_book = {}
while not data.isdigit():
    name, phone_number = data.split("-")
    phone_book[name] = phone_number
    data = input()

for _ in range(int(data)):
    name = input()
    # ако директно искаме да достъпим дикт по ключ, който не съществува директно ексепшъна се рейзва
    # вместо да го поискаме phone_book[name]=, phone_book.get(name)
    if phone_book.get(name):  # ако не намери нищо връща None и отива в else
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")
