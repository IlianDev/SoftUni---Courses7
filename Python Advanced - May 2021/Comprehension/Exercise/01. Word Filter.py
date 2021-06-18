words = input().split()

# list_result = []
# for word in words:
#     if len(word) % 2 == 0:
#         list_result.append(word)
# for i in list_result:
#     print(i)

list_result = [word for word in words if len(word) % 2 == 0]
print('\n'. join(list_result))