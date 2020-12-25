poll = {}

while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    
    place = input("Where do you want to go for your dream vacation? ")
    if place == 'q':
        break

    poll[name] = place

print("\nHere's the result of the poll:")
for key, value in poll.items():
    print(f"{key.title()} : {value.title()}")