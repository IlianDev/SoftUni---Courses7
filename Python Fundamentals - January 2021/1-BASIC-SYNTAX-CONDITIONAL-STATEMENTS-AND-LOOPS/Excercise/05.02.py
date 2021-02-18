sheep_count = int(input())
message = ""
sheep = 1
while sheep < sheep_count:
    message += f"{sheep}sheep..."
    sheep += 1
print(message)