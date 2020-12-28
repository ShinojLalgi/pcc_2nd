try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the first number: "))

except ValueError:
    print("You cannot do addition of a string.")

else:
    add = number1 + number2
    print(f"Result: {add}")