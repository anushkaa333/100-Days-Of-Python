#Static Methods - No need to write self word in static function
# We generally use static methods to create utility functions.
#utility function - A function that doesn't access any properties of a class but makes sense that it belongs to the class, we use static functions.



#****************** I] Inheritance 

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)


    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)



    def display(self):
        print(self.name + "'s age is: " + str(self.age))



class Man(Person):
    sex = 'Male'


person = Person.fromBirthYear('John', 1985)
print(person.age) #38
print(isinstance(person, Person)) #True


man = Man.fromBirthYear('John', 1985)
print(man.age) #38
print(isinstance(man, Man)) #True


person1 = Person.fromFathersAge('John', 1965, 20)
print(person1.age) #78
print(isinstance(person1, Person)) #True


man1 = Man.fromFathersAge('John', 1965, 20)
print(man1.age) #78
print(isinstance(man1, Man)) # False, => #Cant create instace thr' inheriting
# fromFathersAge method doesn't return a Man object but its base class Person's object.

