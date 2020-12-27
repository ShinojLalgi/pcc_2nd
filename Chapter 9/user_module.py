class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def describe_user(self):
        profile = {
            'first name' : self.f_name,
            'last name' : self.l_name
        }
        print(profile)

    def greet_user(self):
        print(f"Hello {self.f_name.title()} {self.l_name.title()}!")