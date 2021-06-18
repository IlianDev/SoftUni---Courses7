heroes = input().split(", ")
# inventory = {hero: {} for hero in heroes}
inventory = {}
for hero in heroes:
    inventory[hero] = {}

line = input()
while line != "End":
    hero, item_name, item_cost = line.split("-")
    if item_name not in inventory[hero]:
        inventory[hero][item_name] = int(item_cost)
    line = input()

for hero in heroes:
    costs = sum(inventory[hero].values())
    count = (len(inventory[hero]))
    print(f"{hero} -> Items: {count}, Cost: {costs}")
