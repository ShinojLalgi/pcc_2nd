import json

def get_new_username():
    name = input("Enter your name: ") 
    with open('name.json', 'w') as f: 
        json.dump(name , f)

def greet_user():
    try:
        with open('name.json') as f:
            file = json.load(f)
    except FileNotFoundError:
        get_new_username()
    else:
        confirm = input(f"Is this your name {file}? ").lower()
        if confirm == 'y':
            print(f"Welcome back {file.title()}!")
        else:
            get_new_username()
        

greet_user()