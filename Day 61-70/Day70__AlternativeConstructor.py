class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def dash(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
        
        #OR
        # n, s = string.split("-")
        # return cls(n, s)

    


e1 = Employee("abc", 10000)
print(e1.name)
print(e1.salary)
# abc
# 10000


string = "pqr-12000"
e2 = Employee.dash(string)
print(e2.name)
print(e2.salary)
# pqr
# 12000

# print(Employee.name)
# print(Employee.salary)
# AttributeError: type object 'Employee' has no attribute 'name'






class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def comma(cls, string):
        n, a = string.split(",")
        return cls(n, a)

    
str = "John, 30"
p = Person.comma(str)
print(p.name)
print(p.age)
# John
#  30
