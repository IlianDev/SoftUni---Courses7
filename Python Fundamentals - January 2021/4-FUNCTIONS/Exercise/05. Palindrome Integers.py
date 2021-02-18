def chek_if_palindrome(el):
    if el == el[::-1]:
        return True
    return False



nums_as_string = input().split(", ")

for element in nums_as_string:
    is_palindrome = chek_if_palindrome(element)
    if is_palindrome:
        print(True)
    else:
        print(False)
