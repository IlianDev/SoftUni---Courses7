def repeat_string(string, times):
    result = " "
    for i in range(0, times):
        result += string
    return result


text = input()
n = int(input())
print(repeat_string(text, n))
