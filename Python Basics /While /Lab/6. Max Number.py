import sys
command = input()
max_el = - sys.maxsize
while command != "Stop":
    number = int(command)
    if number > max_el:
        max_el = number
    command = input()
else:
    print(max_el)