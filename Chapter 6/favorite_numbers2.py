favorite_numbers = {
    'adam' : [7, 2, 10, 21],
    'max' :  [8, 3, 101, 2], 
    'lisa' : [71, 69, 20, 50]
}

for key, value in favorite_numbers.items():
    print(f"{key.title()}'s favorite numbers are:")
    for number in value:
        print(number)
    print()