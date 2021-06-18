n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(num) for num in input().split(", ")])
diagonal_1 = [matrix[i][i] for i in range(n)]
diagonal_2 = [matrix[i][n - 1 - i] for i in range(n)]

print(f"First diagonal: {', '.join([str(i) for i in diagonal_1])}. Sum: {sum(diagonal_1)}")
print(f"Second diagonal: {', '.join([str(i) for i in diagonal_2])}. Sum: {sum(diagonal_2)}")
