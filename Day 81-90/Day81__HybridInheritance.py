class base_class:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f"this is base class, {self.name}")


class derived_class1(base_class):
    def __init__(self, stream):
        base_class.__init__(self, name="xyz")
        self.stream = stream

    def info(self):
        base_class.info(self)
        print(f"this is derived class 1, {self.name}, {self.stream}")


class derived_class2(derived_class1, base_class):
    def __init__(self, year):
        super().__init__(stream="IT")
        self.year = year

    def info(self):
        derived_class1.info(self)
        print(f"this is derived class 1, {self.name}, {self.stream}, {self.year}")


d2 = derived_class2("FE")
d2.info()


# this is base class, xyz
# this is derived class 1, xyz, IT
# this is derived class 1, xyz, IT, FE