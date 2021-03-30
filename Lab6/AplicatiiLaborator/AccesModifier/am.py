class AccessModifiers:
    public_variable = "This is public"
    _protected_variable = "This is theoretically protected"
    __private_variable = "This is theoretically private"
    def __init__(self):
        self.print_members()
    def set_private_variable(self, new_value):
        self.__private_variable = new_value
    def print_members(self):
        print(self.public_variable)
        print(self._protected_variable)
        print(self.__private_variable)
    def public_method(self):
        print("I'm a public method")
    def _protected_method(self):
        print("I'm a protected method")
    def __private_method(self):
        print("I'm a private method")

if __name__ == '__main__':
    access_modifiers = AccessModifiers()
    access_modifiers.public_variable = 0
    access_modifiers._protected_variable = 1
    access_modifiers.__private_variable = 2
    access_modifiers.print_members()
    # setarea variabilei private printr-o metoda setter
    access_modifiers.set_private_variable(2)
    access_modifiers.print_members()
    access_modifiers.public_method()
    access_modifiers._protected_method()
    try:
        access_modifiers.__private_method()
    except AttributeError as e:
        print("Error", e)