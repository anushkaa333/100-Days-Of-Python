#Class and object
#Object is instance of class used to access the properties of class
#Self(wo object jiske liye method call kiya ja raha hai) - parameter is a reference to current instance of class and used to access variables that belongs to class

class person:

    name = "Ram"
    surname = "Sharma"

    def info(self):
        print(f"Name of person {self.name} and surname of person {self.surname}")



obj1 = person()
print(obj1.name) #Ram


obj2 = person()
obj2.name = "Rama"
print(obj2.name, obj2.surname) #Rama Sharma


obj3 = person()
obj3.info() #Name of person Ram and surname of person Sharma


obj4 = person()
obj4.name = "Suresh"
obj4.surname = "Raina"
obj4.info()#Name of person Suresh and surname of person Raina

