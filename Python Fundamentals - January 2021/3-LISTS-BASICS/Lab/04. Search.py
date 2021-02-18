n = int(input())
searched_word = input()

all_words = []
mached_words = []

for _ in range(n):
    current_word = input()
    all_words.append(current_word)
    if searched_word in current_word:
        mached_words.append(current_word)
print(all_words)
print(mached_words)

