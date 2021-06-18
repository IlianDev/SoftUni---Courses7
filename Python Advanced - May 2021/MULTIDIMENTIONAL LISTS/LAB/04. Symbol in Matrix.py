n = int(input())

matrix = []
position = None

for row in range(n):
    matrix.append(list(input()))

searched_symbol = input()
for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_symbol:
            position = (row, col)
            break
    if position:
        break

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")
