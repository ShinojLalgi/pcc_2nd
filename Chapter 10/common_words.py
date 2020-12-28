path = "Python\Chapter 10\carol.txt"
with open(path) as f:
    file = f.read()
word = input("Enter the word you want to search: ")
words = file.lower().split()
word_count = words.count(word.lower())
print(f"The word '{word}' has occured {word_count} times in the file.")