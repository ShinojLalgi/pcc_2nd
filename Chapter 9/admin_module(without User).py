from user_module import User

class Privilege:
    def __init__(self, privileges=[]):
        self.adminprivileges = privileges
    
    def showprivileges(self):
        print("The admin has the following privileges:")
        for privilege in self.adminprivileges:
            print(f"-{privilege}")

class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privileges = Privilege()


