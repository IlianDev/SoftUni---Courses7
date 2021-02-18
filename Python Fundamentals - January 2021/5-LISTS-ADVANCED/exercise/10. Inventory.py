def chek_item_exist(items_list, item):
    if item in items_list:
        return True
    return False


def add_item(items_list, item):
    if not chek_item_exist(items_list, item):
        items_list.append(item)
    return items_list


def drop_item(items_list, item):
    if chek_item_exist(items_list, item):
        items_list.remove(item)
    return items_list


def combine_items(items_list, items_data):
    old_item, new_item = items_data.split(":")
    if chek_item_exist(items_list, item):
        index_old_item = items_list.index(old_item)
        items_list.insert(index_old_item+1, new_item)
    return items_list


def renew_item(items_list, item):
    if chek_item_exist(items_list, item):
        items_list.remove(item)
        items_list.append(item)
    return items_list


items = input().split(", ")
command_data = input()

while not command_data == "Craft!":
    command, item = command_data.split(" - ")
    if command == "Collect":
        items = add_item(items, item)
    elif command == "Drop":
        items = drop_item(items, item)
    elif command == "Combine Items":
        item_data = combine_items(items, item)
    elif command == "Renew":
        items = renew_item(items, item)

    command_data = input()

print(*items, sep=", ")