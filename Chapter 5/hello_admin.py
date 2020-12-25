usernames = ['adm123', 'admin', 'maximus', 'rahuls', 'beast']

for username in usernames:
    if username != 'admin':
        print(f"Welcome {username}!")
    else:
        print(f"\tWelcome back {username}!")