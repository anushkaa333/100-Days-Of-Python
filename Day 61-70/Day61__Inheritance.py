class Employee:
    def __init__(self, n, eid):
        self.name = n
        self.empid = eid

    def info(self):
        print(f"Name of employee {self.name} and employee id is {self.empid}")



class Student(Employee):
    def sinfo(self):
        print(f"Student is inherating properties of employee, name : {self.name}, id : {self.empid} ")


e1 = Employee("Rahul", 101)
e1.info() #Name of employee Rahul and employee id is 101
e1.sinfo() 
#  e1.sinfo()
#     ^^^^^^^^
# AttributeError: 'Employee' object has no attribute 'sinfo'. Did you mean: 'info'?


s1 = Student("Ramesh", 102)
s1.sinfo()
s1.info()
# Student is inherating properties of employee, name : Ramesh, id : 102
# Name of employee Ramesh and employee id is 102