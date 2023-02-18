from Day73_1 import Employee

e = Employee("ABCD")
# print(len(e)) #4

print(e) #This will print __str__ and __repr__ methods. If __str__ kept in comments then only repr will get printed and vice versa.

print(e()) # calling object only => used for calling __call__ method only 
     