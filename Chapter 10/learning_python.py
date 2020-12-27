path = 'Python\Chapter 10\some_text.txt'
with open(path) as f:
    file = f.read()
print(file + '\n')


with open(path) as f:
    for line in f:
        print(line.strip())


with open(path) as f:
    file = f.readlines()
print()
for line in file:
    print(line.strip())