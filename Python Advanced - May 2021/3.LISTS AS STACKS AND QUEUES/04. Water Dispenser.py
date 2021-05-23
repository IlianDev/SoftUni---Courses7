from collections import deque

liters = int(input())
name = input()
queque = deque()

while not name == "Start":
    queque.append(name)
    name = input()

# giving water
command = input()
while not command == "End":
    if command.startswith("refill"):
        liters += int(command.split()[-1])
    else:
        liters_wanted = int(command)
        name = queque.popleft()
        if liters >= liters_wanted:
            liters -= liters_wanted
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    command = input()

print(f"{liters} liters left")
