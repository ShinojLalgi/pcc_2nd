import json

name = input("Enter your name: ") 
with open('names_list.json', 'w') as f: 
    json.dump(name , f)

with open('names_list.json') as f:
    file = f.read()
    
print(file)

