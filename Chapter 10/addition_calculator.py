while True:
    try:
        number1 = input("\nEnter the first number: ")
        if number1 == 'q':
            break
        number2 = input("Enter the first number: ")
        if number2 == 'q':
            break
        add = int(number1) + int(number2)

    except ValueError:
        print("You cannot do addition with a string.")

    else:
        print(f"Result: {add}")