items_list = input().split("!")

command = input()


def check_item_exist(items_list, item_researched):
    return True if item_researched in items_list else False


while command != "Go Shopping!":
    command_type = command.split()[0]
    item = command.split()[1]

    if command_type == "Urgent":
        if not check_item_exist(items_list, item):
            items_list.insert(0, item)
    elif command_type == "Unnecessary":
        if check_item_exist(items_list, item):
            items_list.remove(item)
    elif command_type == "Correct":
        if check_item_exist(items_list, item):
            new_item = command.split()[2]
            old_item = items_list.index(item)
            items_list[old_item] = new_item
    elif command_type == "Rearrange":
        if check_item_exist(items_list, item):
            items_list.remove(item)
            items_list.append(item)
    command = input()

print(", ".join(items_list))
