targets_list = [int(el) for el in input().split()]

index_command = input()
counter_shoot_targets = 0

while not index_command == "End":
    index_command = int(index_command)

    # check if there is such an index
    if index_command not in range(len(targets_list)):
        index_command = input()
        continue

    # chek if the item is shot
    current_value = targets_list[index_command]
    if current_value == -1:
        index_command = input()
        continue

    targets_list[index_command] = -1
    counter_shoot_targets += 1

    for current_index in range(len(targets_list)):
        if targets_list[current_index] == -1:
            continue
        if targets_list[current_index] > current_value:
            targets_list[current_index] -= current_value
        else:
            targets_list[current_index] += current_value
    index_command = input()

print(f"Shot targets: {counter_shoot_targets} ->{' '.join([str(el) for el in targets_list])}")