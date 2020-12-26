
class User:

    def __init__(self, f_name, l_name, log_attempts=0):
        self.f_name = f_name
        self.l_name = l_name
        self.login_attempts = log_attempts

    def describe_user(self):
        profile = {
            'first name' : self.f_name,
            'last name' : self.l_name
        }

        print(profile)

    def greet_user(self):
        print(f"Hello {self.f_name.title()} {self.l_name.title()}!")

    def reset_login_attempts(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
        

me = User('shinoj', 'lalgi')
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attempts)
me.reset_login_attempts()
print(me.login_attempts)