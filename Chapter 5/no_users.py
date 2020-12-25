usernames = ['adm123', 'admin', 'maximus', 'rahuls', 'beast']

if usernames:
    for username in usernames:
        if username != 'admin':
            print(f"Welcome {username}!")
        else:
            print(f"\tWelcome back {username}!")
else:
    print("We need to find some users!!")