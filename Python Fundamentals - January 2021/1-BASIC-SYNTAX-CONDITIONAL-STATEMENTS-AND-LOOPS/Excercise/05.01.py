sheep_count = int(input())
message = ""

for sheep in range (1, sheep_count+1):
    message += f"{sheep}sheep..."
print(message)