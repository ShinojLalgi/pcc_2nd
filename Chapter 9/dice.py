from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


mydie = Dice(6)
print("6 sided die")
for x in range(10):
    mydie.roll_die()
print()

mydie = Dice(10)
print("10 sided die")
for x in range(10):
    mydie.roll_die()
print()

mydie = Dice(20)
print("20 sided die")
for x in range(10):
    mydie.roll_die()
print()
