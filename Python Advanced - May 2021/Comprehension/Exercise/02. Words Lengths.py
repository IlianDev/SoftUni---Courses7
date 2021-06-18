words = input().split(", ")
# list_words = []
# for word in words:
#     result = f"{word} -> {len(word)}"
#     list_words.append(result)
# print(', '.join(list_words))


list_words = [f"{word} -> {len(word)}" for word in words]
print(', '.join(list_words))