
#Instance Variables =>
# They are specific to instace of class
# If a new instance is created, totally new values or default values will get assigned to object of class. 



class person:
    def __init__(self, n, yoe):
        self.name = n
        self.yroe = yoe

    def info(self):
        print(f"Name of person is { self.name } and their YOE is {self.yroe}")



p1 = person("amm", 1)
p1.info() #Name of person is amm and their YOE is 1





#Class Variables => 
# For entire class, their value would remain same for diff objects of class
# A same copy shared to all instances of class. 
# After updating its value in prev iteration the same value will get carry forwarded for next new instace of class, if created
    

class employee:

    Employee_Count = 0 #Class Variable


    def __init__(self, n, yoe):
        self.name = n
        self.yroe = yoe
        employee.Employee_Count +=1

    def info(self):
        print(f"Name of employee is { self.name } and their YOE is {self.yroe}. Now total number of employees are {self.Employee_Count}")



e1 = employee("am", 2)
e1.info()

e1 = employee("bm", 3)
e1.info()

e1 = employee("cm", 3)
e1.info()

e1 = employee("dm", 3)
e1.info()

e1 = employee("em", 3)
e1.info()


# Name of employee is am and their YOE is 2. Now total number of employees are 1
# Name of employee is bm and their YOE is 3. Now total number of employees are 2
# Name of employee is cm and their YOE is 3. Now total number of employees are 3
# Name of employee is dm and their YOE is 3. Now total number of employees are 4
# Name of employee is em and their YOE is 3. Now total number of employees are 5





# ************ Another e.g with class and instace variable added

class emp:

    Employee_Count = 0 #Class Variable
    comp_name = "Apple"

    def __init__(self, n, yoe):
        self.name = n
        self.yroe = yoe
        self.raise_amt = 3000
        emp.Employee_Count +=1

    def info(self):
        print(f"Name of employee is { self.name } and their YOE is {self.yroe}. Now total number of employees are {self.Employee_Count}")
        print(f"Raise amt {self.raise_amt} and company name {self.comp_name}")



e1 = emp("xy", 2)
e1.info()

e2 = emp("xyz", 1)
e2.info()


# Name of employee is xy and their YOE is 2. Now total number of employees are 1
# Raise amt 3000 and company name Apple
# Name of employee is xyz and their YOE is 1. Now total number of employees are 2
# Raise amt 3000 and company name Apple


e3 = emp("pqr", 3)
e3.comp_name = "Google"
e3.raise_amt = 2000
e3.info()

# Name of employee is pqr and their YOE is 3. Now total number of employees are 3
# Raise amt 2000 and company name Google


e4 = emp("abc", 8)
emp.Employee_Count = 6
e4.info()
# Name of employee is abc and their YOE is 8. Now total number of employees are 6
# Raise amt 3000 and company name Apple


e5 = emp("jk", 1)
e5.info()
# Name of employee is jk and their YOE is 1. Now total number of employees are 7
# Raise amt 3000 and company name Apple


e6 = emp("jkl", 4)
emp.Employee_Count = 20
emp.comp_name = "Twitter"
e6.info()
# Name of employee is jkl and their YOE is 4. Now total number of employees are 20
# Raise amt 3000 and company name Twitter


e7 = emp("l", 4)
e7.info()
# Name of employee is l and their YOE is 4. Now total number of employees are 21
# Raise amt 3000 and company name Twitter


e8 = emp("lm", 2)
emp.raise_amt = 500
e8.Employee_Count = 100
e8.info()
# Name of employee is lm and their YOE is 2. Now total number of employees are 100
# Raise amt 3000 and company name Twitter

e9= emp("lmm", 22)
e9.info()
# Name of employee is lmm and their YOE is 22. Now total number of employees are 23
# Raise amt 3000 and company name Twitte

# 1.
#If class and instance variable changes are made thr' instance of class that change would be applicable to only that instance, change would be temperory.
#It would not get refelcted when new instances are created.
# e.g e1, e2, e3 

# 2.
#If class and instance variable changes are made thr' class name then 
# only class variable change would be updated permanently to all new instance of class. # e.g e4, e5, e6, e7
# And instace variable never get updated thr' class name, neither permanently nor temperory # e.g e8

#3.

# Instace => instace and class variable values temperory
# Class => class values permanetly