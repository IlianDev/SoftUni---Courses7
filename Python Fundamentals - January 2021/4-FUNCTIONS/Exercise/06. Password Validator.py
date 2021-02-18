def check_password_is_valid(pwrd):
    is_valid = True
    consist_only_letters_and_digits = True
    count_digits = 0

    if len(pwrd) < 6 or len(pwrd) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    for el in pwrd:
        if el.isdigit():
            count_digits += 1
        if not el.isdigit() and not el.isalpha():
            consist_only_letters_and_digits = False
            is_valid = False

    if not consist_only_letters_and_digits:
        print("Password must consist only of letters and digits")

    if count_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid == True


password = input()
result = check_password_is_valid(password)

if result == True:
    print("Password is valid")
