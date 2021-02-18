def check_if_palindrome(el):
    if el == el[::-1]:
        return True
    return False


given_list = input().split(", ")

for element in given_list:
    print(check_if_palindrome(element))
