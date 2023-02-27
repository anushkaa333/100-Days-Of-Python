
#**************** I]

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"the name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show_1(self):
        print(f"the dance is {self.dance}")


class DancerEmployee(Dancer, Employee):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance



de = DancerEmployee("abc", "kathak")
de.show()
de.show_1()
# the name is abc
# the dance is kathak




#***************** II]


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal, {self.species}, {self.name}")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color

    def make_sound(self):
        print("mammel animal")
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")



d = Dog("abc", "lab", "black")
d.make_sound() # Bark!

#make_sound method will be searched by object first in current class "Dog" then Animal as Animal class is the 1st class passed as parameter and 
# then in mammel as its 2nd parameter 
# and if multiple classes are passed as parameter then it will search in them sequentially 



print(Dog.mro())
# [<class '__main__.Dog'>, <class '__main__.Animal'>, <class '__main__.Mammal'>, <class 'object'>]


#Without "Animal.__init__(self, name, species="Dog")" in __init__ method of Dog, d.make_sound will be call make_sound method in Animal
# But cant assign variables like  {self.species}, {self.name}
# Hence o/p will be ====> Sound made by the animal, {self.species}, {self.name}


