while True:
    name = input("Please enter your name: ")
    if name == 'q':
        break

    language = input("Please enter your favorite language: ")
    if language == 'q':
        break
    
    path = 'Python\Chapter 10\poll_list.txt'
    with open(path, 'a') as f:
        f.write(f"{name.title()} likes {language.title()} language.\n")

with open(path) as f:
    file = f.read()

print(file.strip())