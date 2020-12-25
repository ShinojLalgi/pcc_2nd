myself = {
    'name' : 'shinoj', 
    'city' : 'kalyan',
    'age' : '7'
}

myfriend = {
    'name' : 'jim',
    'city' : 'london',
    'age' : '25'
}

myfriend2 = {
    'name' : 'alex',
    'city' : 'new york',
    'age' : '30'
}

people = [myself, myfriend, myfriend]

for person in people:
    for key, value in person.items():
        print(f"{key.title()} : {str(value).title()}")
    print()