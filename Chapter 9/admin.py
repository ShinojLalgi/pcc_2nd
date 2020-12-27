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
        
class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.adminprivileges = []

    def showprivileges(self):
        print("The admin has the following privileges:")
        for privilege in self.adminprivileges:
            print(f"-{privilege}")

me = Admin('shinoj', 'lalgi')
me.adminprivileges = ['can delete posts', 'can remove users']
me.showprivileges()