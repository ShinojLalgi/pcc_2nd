path = 'Python\Chapter 10\some_text.txt'

with open(path) as f:
    file = f.read()
print(file + '\n')
    
if "Python" in file:
    file = file.replace("Python", "C")
print(file)