name = input("Please enter your name: ")

path = 'Python\Chapter 10\guest.txt'
with open(path, 'w') as f:
    f.write(f"{name} \n")

with open(path) as f:
    file = f.read()

print(file.strip())