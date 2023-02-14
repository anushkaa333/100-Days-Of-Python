
#****************** I] Without class method


class Employee:
    company = "Apple"

    def info(self):
        print(f"Name of company {self.company} and name of employee {self.name}")


    def change_compName(cls, newCompany):
        cls.company = newCompany



e1 = Employee()
e1.name = "abc"
e1.info() #Name of company Apple and name of employee abc

e1.company = "Google"
e1.info() #Name of company Google and name of employee abc


e1.change_compName("Twitter")
e1.info()#Name of company Twitter and name of employee abc
print(Employee.company) #Apple



#Thr' instance of class, company name would change ***temporarily*** by calling the function of class
#But to change company name ***permanently*** by using instance of class by calling function of class, we'll need use @classmethod decorator



#********************** II] With class method


class Emp:
    company = "Apple"

    def info(self):
        print(f"Name of company {self.company} and name of employee {self.name}")


    @classmethod
    def change_compName(cls, newCompany):
        cls.company = newCompany



e2 = Emp()
e2.name = "pqr"
e2.change_compName("FB")
e2.info() #Name of company FB and name of employee pqr

print(Emp.company) #FB



#Purpose of @classmethod is to change the class variables ***permanently*** 
#Purpose of @classmethod is to change the instance variables ***temperorily*** =>Day70
