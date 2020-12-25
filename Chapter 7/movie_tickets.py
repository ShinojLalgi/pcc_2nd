while True:
    age = input("What is your age? ").lower()
    if age == 'quit':
        break
    elif int(age) <= 3:
        print("Your ticket is free")
    elif 3 < int(age) <= 12:
        print("Your ticket is worth $10")
    elif int(age) > 12:
        print("Your ticket is worth $15") 
     

    