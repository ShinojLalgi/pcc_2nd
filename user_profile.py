def build_profile(first_name, last_name, **kargs):
    """ Prints a summary about the user profile"""
    profile = {
        'first_name' : first_name.title(),
        'last_name' : last_name.title()
    }

    if kargs:
        for key, value in kargs.items():
            profile[key] = value

    print(profile)

build_profile('shinoj', 'lalgi', location = 'princeton', field = 'physics', age = 25, email = 'shin2223@gmail.com')