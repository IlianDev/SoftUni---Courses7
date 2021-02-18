numbers_as_strings = input().split()
numbers_descending_as_string = sorted(numbers_as_strings, reverse=True)
print("".join(numbers_descending_as_string))
