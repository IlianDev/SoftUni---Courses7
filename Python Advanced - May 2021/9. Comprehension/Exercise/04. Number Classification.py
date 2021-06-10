nums_data = [int(el) for el in input().split(", ")]

positive = [str(x) for x in nums_data if x >= 0]
negative = [str(x) for x in nums_data if x < 0]
even = [str(x) for x in nums_data if x % 2 == 0]
odd = [str(x) for x in nums_data if x % 2 != 0]

# for num in nums_data:
#     if num > 0:
#         positive.append(num)
#     if num < 0:
#         negative.append(num)
#     if num % 2 == 0:
#         even.append(num)
#     if num % 2 == 0:
#         odd.append(num)

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")

