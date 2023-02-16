
#************ I] dir
#Describes the methids and attributes available for object
#Its good tool for discovering what you can do with object


x = [1,2,4]
print(dir(x))

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']



#************ II] __dict__

#This attribute returns the dictionary representation of object attribute 
#This is used for introspection


class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age


p = person("abc", 30)
print(p.__dict__)
# {'name': 'abc', 'age': 30}


#**************** III] help()

#Used to help in documentation of object and methods in well mannered description

print(help(person))
# Help on person in module __main__ object:

# class person(builtins.object)
#  |  person(name, age)
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name, age)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)

# None

print(help(p))
# Help on person in module __main__ object:

# class person(builtins.object)
#  |  person(name, age)
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name, age)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
# -- More  --