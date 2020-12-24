guests = ['adam', 'sam', 'ava']

del guests[-1]
guests.append('max')

print("Hey guys I found a bigger table for the party!\n")

guests.insert(0, 'lia')
guests.insert(1, 'dan')
guests.append('mia')

for guest in guests:
    print(f"Hi {guest.title()}! Please come to my party.")
