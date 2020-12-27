from random import choice

series = ['a', 'b', 'c', 'd', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

lottery = []
while len(lottery) < 4:
    lot = choice(series)
    lottery.append(lot)
print(lottery) 