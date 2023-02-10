#There's no specific convention for private, public, protected in python
#Private e.g: __varName => to access private var, we'll need to use name mangling
#Name Mangling e.g: _className__varName



#************** I] Public
class Student:
    def __init__(self):
        self.name = "Ram"

    def info(self):
        print(f"Name : {self.name}")


s1 = Student()
s1.info() #Name : Ram


#*************** II] Private

class Employee:
    def __init__(self, n, eid):
        self.__name = n
        self.__empid = eid

    def __info(self):
        print(f"Name of employee {self.__name} and employee id is {self.__empid}")





e1 = Employee("Rahul", 101)
# e1.__info() #AttributeError: 'Employee' object has no attribute '__info'
# print(e1.__name) #AttributeError: 'Employee' object has no attribute '__name'
#Trowing attribute error bcoz method and varName declared as private (starts with __)

#Name mangling can be used to access private members
print(e1._Employee__empid) #101
e1._Employee__info() #Name of employee Rahul and employee id is 101




#*************** III]  Protected - Accessing private members to inherited class and outside class

class Employee:
    def __init__(self, n, eid):
        self.__name = n
        self.__empid = eid

    def __info(self):
        print(f"Name of employee {self.__name} and employee id is {self.__empid}")



class Student(Employee):
    def sinfo(self):
        print(f"Student is inherating properties of employee, name : {self._Employee__name}, id : {self._Employee__empid} ")


s1 = Student("Ramesh", 102)
s1.sinfo() #Student is inherating properties of employee, name : Ramesh, id : 102     ==>Accessing private members to inherited class
s1._Employee__info() #Name of employee Ramesh and employee id is 102  ==>Accessing private members outside class