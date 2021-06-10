sequences = input().split("|")

# numbers = []
# for seq in sequences:
#     row = []
#     for el in seq.split(" "):
#         if el.isnumeric():
#             row.append(int(el))
#
#     numbers.append(row)

numbers_list = [
    [int(el)for el in seq.split()
     if el.isnumeric()]
    for seq in sequences
]
numbers_list.reverse()

numbers = [str(number) for sequences in numbers_list for number in sequences]
print(' '.join(numbers))