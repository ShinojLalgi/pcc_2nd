class Restuarant:

    def __init__(self, restaurant_name, cuisine_type, number_served=0 ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """ Prints name of restuarant and its cuisine """
        print(f"{self.restaurant_name.title()} has {self.cuisine_type.title()} as its cuisine.")

    def open_restuarant(self):
        """ Prints whether the restuarant is open or not """
        print(f"{self.restaurant_name.title()} is open now.")

    def served(self):
        print(f"{self.restaurant_name.title()} has served {self.number_served} till today.")
    
    def set_number_served(self, update):
        self.number_served = update

    def increment_number_served(self):
        self.number_served += 1


my_restuarant = Restuarant('china chinese', 'chinese')
my_restuarant.served()
my_restuarant.increment_number_served()
my_restuarant.set_number_served(25)
my_restuarant.increment_number_served()
my_restuarant.served()