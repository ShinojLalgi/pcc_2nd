def sandwich_order(*items):
    """ Prints the summary of your sandwich order"""
    print("Your order:")
    for item in items:
        print(f"-{item}")

sandwich_order('olive', 'cheese', 'capsicum')
