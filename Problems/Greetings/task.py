class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print(f"Hello, I am {self.name}!")


user_name = input()
my_person = Person(user_name)
my_person.greet()
