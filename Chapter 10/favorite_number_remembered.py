import json

try:
    with open('names_list.json') as f:
        file = f.read()
except FileNotFoundError:
    name = input("Enter your name: ") 
    with open('names_list.json', 'w') as f: 
        json.dump(name , f)
else:
    print(file)