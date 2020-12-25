pet1 = {
    'animal' : 'dog',
    'name' : 'alexis',
    'owner' : 'adam'
    
}

pet2 = {
    'animal' : 'cat',
    'name' : 'vivian',
    'owner' : 'dan',
}

pet3 = {
    'animal' : 'parrot',
    'name' : 'tori',
    'owner' : 'lia',
}

pet4 = {
    'animal' : 'hamster',
    'name' : 'manny',
    'owner' : 'nova',
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()} : {value.title()}")
    print()