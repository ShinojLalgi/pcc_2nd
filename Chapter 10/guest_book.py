while True:
    name = input("Please enter your name: ")
    if name == 'q':
        break

    path = 'Python\Chapter 10\guest.txt'
    with open(path, 'a') as f:
        f.write(f"{name.title()} \n")

with open(path) as f:
    file = f.read()

print(file.strip())