n = int(input())
nums = []

# for _ in range(n):
#     data = [int(i) for i in input().split(", ")]
#     nums.extend(data)
# print(nums)

matrix = [[int(el)for el in input().split(", ")] for _ in range(n)]
flattened_matrix = [num for row in matrix for num in row]

print(flattened_matrix)