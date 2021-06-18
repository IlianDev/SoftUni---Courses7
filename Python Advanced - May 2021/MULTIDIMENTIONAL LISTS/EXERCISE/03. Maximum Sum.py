def read_matrix(num_rows):
    mtrx = []
    for _ in range(num_rows):
        nums = [int(el) for el in input().split()]
        mtrx.append(nums)
    return mtrx


num_rows, num_cols = input().split()
num_rows, num_cols = int(num_rows), int(num_cols)

matrix = read_matrix(num_rows)

max_el = None
max_start_i, max_start_j = 0, 0

for i in range(num_rows - 2):
    for j in range(num_cols - 2):
        current_sum = sum([
            matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2],
        ])
        if max_el is None or max_el < current_sum:
            max_el = current_sum
            max_start_i, max_start_j = i, j

print(f"Sum = {max_el}")
for i in range(3):
    for j in range(3):
        print(matrix[max_start_i + i][max_start_j + j], end=" ")
    print()
