import sys
command = input()
min_el = sys.maxsize

while command != "Stop":
    number = int(command)
    if number < min_el:
        min_el = number
    command = input()
else:
    print(min_el)
