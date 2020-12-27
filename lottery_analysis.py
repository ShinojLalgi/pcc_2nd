from random import choice

series = ['a', 'b', 'c', 'd', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lottery = []
mylottery = ['a', 0, 3, 'b']
count = 0
while True:
    while len(lottery) < 4:
        lot = choice(series)
        lottery.append(lot)
    count += 1
    
    if mylottery != lottery:
        lottery = []
    else:
        break
    
    

print(mylottery)
print(lottery)
print(count)
