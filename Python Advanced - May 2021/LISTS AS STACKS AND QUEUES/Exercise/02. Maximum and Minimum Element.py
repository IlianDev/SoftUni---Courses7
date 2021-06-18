n = int(input())

stack = []
for idx in range(n):
    command = input().split()
    # push something in the stack
    if command[0] == "1":
        stack.append(int(command[1]))
    # delete top most el in the stack
    elif command[0] == "2":
        if len(stack) > 0:
            stack.pop()
    # print the maximum element in the stack
    elif command[0] == "3":
        if len(stack) > 0:
            print(max(stack))
    # print the minimum element in the stack
    elif command[0] == "4":
        if len(stack) > 0:
            print(min(stack))

reversed_numbers = []
for i in range(len(stack)):
    reversed_numbers.append(str(stack.pop()))

print(', '.join(reversed_numbers))
