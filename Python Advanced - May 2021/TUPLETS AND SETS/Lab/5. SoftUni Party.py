n = int(input())
all_guests = set()

for x in range(n):
    all_guests.add(input())

ticket = input()

arrived = set()
while not ticket == "END":
    arrived.add(ticket)
    ticket = input()

print(len(all_guests.difference(arrived)))
result =sorted (all_guests.difference(arrived))
[print(x) for x in result]
