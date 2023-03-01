class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog:
    def __init__(self, name, breed):
        self.breed = breed
        Animal.__init__(self, name, species="Lab")

    def show(self):
        Animal.show(self)
        print(f"breed : {self.breed}")


class Dog1:
    def __init__(self, name, color):
        self.color = color
        Dog.__init__(self, name, breed="Dog1")

    def show(self):
        Dog.show(self)
        print(f"color : {self.color}")


d1 = Dog1("xyz", "black")
d1.show()

# Name : xyz
# Species : Lab
# breed : Dog1
# color : black

print(Dog1.mro())
# [<class '__main__.Dog1'>, <class 'object'>]