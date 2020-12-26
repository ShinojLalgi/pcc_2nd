def car(brand, model, color=None, **kargs):
    """ Prints the information about your car """
    car = {
        'brand' : brand.title(),
        'model' : model.title()
    }

    if color:
        car['color of car'] = color.title()

    for key, value in kargs.items():
        car[key] = value

    print(car)

car('subaru', 'outback', color='blue', tow_package=True)