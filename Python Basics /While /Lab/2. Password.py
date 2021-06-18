username = input()
password = input()

# въвеждам си променлива, зашото постоянно ще се чете нова парола
input_password = input()
# спираме да въвеждаме парола ако тази парола която въведа е равна на първата

while input_password != password:
    input_password = input()  # сравнявам новата парола дали е равна с първата и ако е грешна прочитам новата парола.
else:
    print(f"Welcome {username}!")
