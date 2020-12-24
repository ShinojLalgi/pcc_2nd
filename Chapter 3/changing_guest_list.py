guests = ['adam', 'sam', 'ava']

print(f"Hey guys {guests[-1].title()} won't be able to attend the party\n")

del guests[-1]
guests.append('max')

for guest in guests:
    print(f"Hi {guest.title()}! Please come to my party.")
