# If parent-child init args are EQUAL then thr' child instance calling only child init method is called, bcoz instances are specific to class and instances can overriden using super keyword as in III] and Day74
# If parent-child init args are NOT EQUAL then respective instaces will be called at respective object creation OR [use super().__init__ in child class => Day74] 



#******************** I] 

class Parent:
    def pmethod(self):
        print("This is parent method")


class Child(Parent):
    def pmethod(self):
        print("calling parent method thr' child instance")
        super().pmethod()


    def cmethod(self):
        print("This is class method")


c = Child()
c.pmethod()
# calling parent method thr' child instance
# This is parent method



#******************** II]


class Parent:
    def pmethod(self):
        print("This is parent method")


class Child(Parent):
    # def pmethod(self):
    #     print("calling parent method thr' child instance")
    #     super().pmethod()


    def cmethod(self):
        print("This is class method")


c = Child()
c.pmethod()
# This is parent method



#****************** III] If child constructor created
#Conclusion:
#Here, we'll need to pass args equal to child instance

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pmethod(self):
        print("This is parent method")


class Child(Parent):
    def __init__(self, name, age, stream):
        super().__init__(name, age)
        self.stream = stream
        

    def cmethod(self):
        print("This is class method")



# cp = Child("pqr", 20)
# print(c.name)
# print(c.age)
# TypeError: Child.__init__() missing 1 required positional argument: 'stream'
#Unlike methods, instace can't be find out in parent class, if its doesnt get exact matching args count, it will throw


#Conclusion:
#Here, we'll need to pass args equal to child instance while creating child object **if child constructor is present**


#Solution:

c = Child("abc", 18, "Science")
print(c.name)
print(c.age)
print(c.stream)
# abc
# 18
# Science



#************************ IV] If child constructor not created and parent constructor created


#Conclusion:
#Here, we'll need to pass args equal to parent instance

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pmethod(self):
        print("This is parent method")


class Child(Parent):
        

    def cmethod(self):
        print("This is class method")



p = Parent("xyz", 30)
print(p.name)
print(p.age)
# xyz
# 30

# cp = Child()
# print(cp.name)
# print(cp.age)
# cp.cmethod()
# TypeError: Parent.__init__() missing 2 required positional arguments: 'name' and 'age' => for all 3;cp.name, cp.age and cp.method(), we'll get TypeError

#Conclusion:
#Here, we'll need to pass args equal to parent instance while creating child object **if child constructor is NOT present**

#Solution:

cp = Child("abcd", 12)
print(cp.name)
print(cp.age)
# abcd
# 12

