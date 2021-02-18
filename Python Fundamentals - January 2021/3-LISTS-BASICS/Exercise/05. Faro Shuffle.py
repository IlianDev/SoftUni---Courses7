import copy

cards = input().split()
n_shuffles = int(input())

top_card = cards[0]
bottom_card = cards[-1]

half = len(cards) // 2
shuffle_cards = []

right_cards = []
left_cards = []

# for left side
for index in range(1, half):
    left_cards.append(cards[index])

# for right side
for index in range(half, len(cards)-1):
    right_cards.append(cards[index])

for index in range(len(left_cards)):
    shuffle_cards.append(right_cards[index])
    shuffle_cards.append(left_cards[index])

for n_shuffle in range(n_shuffles):
    right_cards = []
    left_cards = []

    # for left side
    for index in range(1, half):
        left_cards.append(cards[index])

    # for right side
    for index in range(half, len(cards) - 1):
        right_cards.append(cards[index])

    for index in range(len(left_cards)):
        shuffle_cards.append(right_cards[index])
        shuffle_cards.append(left_cards[index])

    cards = shuffle_cards.copy()
    cards.append(bottom_card)
    cards.insert(0, top_card)
    shuffle_cards = []

print(cards)