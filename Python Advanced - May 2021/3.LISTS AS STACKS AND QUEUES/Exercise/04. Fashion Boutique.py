box = list(map(int, input().split()))
capacity = int(input())

counter_racks = 1

new_capacity = capacity
while len(box) > 0:
    given_value_cloth = box.pop()

    if given_value_cloth <= new_capacity:
        new_capacity -= given_value_cloth
    else:
        counter_racks += 1
        new_capacity = capacity
        new_capacity -= given_value_cloth

print(counter_racks)