def show_messages(message_list):
    """ Prints the messages inside a list """
    print("\nYour messages: ")
    for message in message_list:
        print(message)

messages = ['i love python', 'i am hungry', 'i want to eat']
show_messages(messages)