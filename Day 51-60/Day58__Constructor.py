#Constructor - used to create and initialize an object of class. It is invoked when object of class created
#Purpose of constructors is to initialize and assign the values to data members of class
#It cant return any value other than none


# Syntax

# 1. 
# def __init__(self):
    # initializations

#2. Create fun name same as class name
# class name1:
#     def name1(self):



#****************** I]

class student():
    def __init__(self, n, s):
        self.name = n
        self.std = s
    
    def info(self):
        print(f"name is {self.name} and year is {self.std}")



s1 = student("Geeta", "BE")
s1.info() #name is Geeta and year is BE

        

#****************** II]

class teacher():
    def __init__(self, n, s):
        self.name = n
        self.std = s
    
    
t1 = student("Seeta", "TE")
print(f"name is {t1.name} and year is {t1.std}") #name is Seeta and year is TE