# toppings = []
# while not toppings or toppings:
#     topping = input("Which topping would you like to have on your pizza? ").lower()
#     if topping != 'quit':
#         toppings.append(topping)
#         print("We have added your topping to your pizza\n")
#     else:
#         print("Thank you for ordering from us.")
#         break

# stop = False
# while not stop:
#     toppings = []
#     topping = input("Which topping would you like to have on your pizza? ").lower()
#     if topping != 'quit':
#         toppings.append(topping)
#         print("We have added your topping to your pizza\n")
#         stop = False
#     else:
#         print("Thank you for ordering from us.")
#         stop = True


while True:
    toppings = []
    topping = input("Which topping would you like to have on your pizza? ").lower()
    if topping != 'quit':
        toppings.append(topping)
        print("We have added your topping to your pizza\n")
    else:
        print("Thank you for ordering from us.")
        break