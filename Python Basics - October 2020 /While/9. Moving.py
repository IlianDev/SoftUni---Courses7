width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height  #
command = input()

while command != "Done":
    boxes = int(command)
    free_space -= boxes
    if free_space <= 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break
    command = input()
else:
    print(f"{free_space} Cubic meters left.")
