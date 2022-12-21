#********* 1 *******

a = 98
b = "ammm"
c =True
d = 45.9

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#output
# <class 'int'>
# <class 'str'>
# <class 'bool'>
# <class 'float'>

# ******** 2 **********

first_name = 'am'
name = first_name
print(name) #am


#********* 3 **********
name = first_name
first_name = 'am'
print(name)

# Traceback (most recent call last):
#   File "h:\100 Days of Python\Day6__DataTypes.py", line 23, in <module>
#     name = first_name
#            ^^^^^^^^^^
# NameError: name 'first_name' is not defined