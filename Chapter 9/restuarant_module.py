class Restuarant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Prints name of restuarant and its cuisine """
        print(f"{self.restaurant_name.title()} has {self.cuisine_type.title()} as its cuisine.")

    def open_restuarant(self):
        """ Prints whether the restuarant is open or not """
        print(f"{self.restaurant_name.title()} is open now.")