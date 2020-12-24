guests = ['adam', 'sam', 'ava']

del guests[-1]
guests.append('max')

guests.insert(0, 'lia')
guests.insert(1, 'dan')
guests.append('mia')

print("I am really sorry guys but I can only have two people for the party.\n")

for x in range(4):
    guest = guests.pop()
    print(f"I am really sorry {guest.title()} but you can't come for the party.")

print()
for guest in guests:
    print(f"{guest.title()} you are still invited for the party.")

del guests[0]
del guests[0]

print(f"\n{guests}")
