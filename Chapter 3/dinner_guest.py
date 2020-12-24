guests = ['adam', 'sam', 'ava']

del guests[-1]
guests.append('max')

guests.insert(0, 'lia')
guests.insert(1, 'dan')
guests.append('mia')

for x in range(4):
    guest = guests.pop()
   
del guests[0]
del guests[0]

print(len(guests))
