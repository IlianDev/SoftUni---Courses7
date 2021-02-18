n = int(input())

negative_lists = []
positive_lists = []

for _ in range(n):
    current_number = int(input())
    if current_number < 0:
        negative_lists.append(current_number)
    else:
        positive_lists.append(current_number)

print(positive_lists)
print(negative_lists)

print(f"Count of positives: {len(positive_lists)}. Sum of negatives: {sum(negative_lists)}")


