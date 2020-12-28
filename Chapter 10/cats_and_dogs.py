path1 = 'Python\Chapter 10\cats.txt'
path2 = 'Python\Chapter 10\dogs.txt'

try:
    with open(path1) as f:
        file1 = f.read()
except FileNotFoundError:
    print("File 'cats.txt' not found. Please check.")
else:
    print("Contents of 'cats.txt':")
    print(file1)

try:
    with open(path2) as f:
        file12 = f.read()
except FileNotFoundError:
    print("File 'dogs.txt' not found. Please check.")
else:
    print("\nContents of 'dogs.txt':")
    print(file12)