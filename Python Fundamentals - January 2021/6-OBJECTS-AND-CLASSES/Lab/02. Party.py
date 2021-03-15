class Party:
    def __init__(self):
        self.people = []  # people e атрибут


# инстанция my_party
my_party = Party()

name = input()
while not name == "End":
    my_party.people.append(name)
    name = input()
print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {len(my_party.people)}")
