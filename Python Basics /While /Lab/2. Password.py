username = input()
password = input()


input_password = input()


while input_password != password:
    input_password = input()
else:
    print(f"Welcome {username}!")
