def send_messages(message_list):
    """ Prints the messages inside a list """
    sent_messages = []
    print("\nYour messages: ")
    while message_list:
        message = message_list.pop()
        print(message)
        sent_messages.append(message)

messages = ['i love python', 'i am hungry', 'i want to eat']
send_messages(messages)