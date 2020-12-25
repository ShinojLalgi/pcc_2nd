current_users = ['adm123', 'admin', 'maximus', 'rahuls', 'beast']
new_users = ['adma', 'leo232', 'Maximus', 'Beast', 'Gin323']

for user in new_users:
    if user.lower() in current_users:
        print(f"Sorry user but this username has already been used '{user}'!")
    else:
        print(f"This username is available: '{user}'!")
