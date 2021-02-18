def get_chars_in_range(start_char, end_char):
    start_int = ord(start_char)
    end_char = ord(end_char)
    chars = []
    for num in range(start_int + 1, end_char):
        chars.append(chr(num))
    return chars


arg1 = input()
arg2 = input()
result = get_chars_in_range(arg1, arg2)
print(" ".join(result))