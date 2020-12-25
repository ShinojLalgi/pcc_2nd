favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['jen', 'sam', 'ben', 'phil', 'maxie']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()} for participating in our poll.\n")
    else:
        print(f"Hi {person.title()}! We are invited for participating in our poll.")