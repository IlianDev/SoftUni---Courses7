biscuits_list = input().split(", ")
commands = input()

while not commands == "Eat":
    commands_type = commands.split()[0]
    biscuit_name = commands.split()[1]

    if commands_type == "Update-Any":
        for i in range(len(biscuits_list)):
            if biscuits_list[i] == biscuit_name:
                biscuits_list[i] = "Out of stock"

    elif commands_type == "Remove":
        replacement_int = int(commands.split()[2])
        if 0 <= replacement_int < len(biscuits_list):
            biscuits_list[replacement_int] = biscuit_name

    elif commands_type == "Update-Last":
        biscuits_list[len(biscuits_list) - 1] = biscuit_name

    elif commands_type == "Rearrange":
        if biscuit_name in biscuits_list:
            biscuits_list.remove(biscuit_name)
            biscuits_list.append(biscuit_name)

    commands = input()

biscuits_list_formatted = biscuits_list.copy()
for i in range(len(biscuits_list)):
    if biscuits_list[i] == "Out of stock":
        del biscuits_list_formatted[i]

print(' '.join(biscuits_list_formatted))

