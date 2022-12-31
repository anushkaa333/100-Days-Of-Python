#Sets are:
# 1. Immutable
# 2. Duplicates arent printed
# 3. Order not maintained
# 4. Since order not maintained, elements cant be accessed by index number
# 5. TYPE - Empty set can be displayed by "set()" - type would be set and not by only "{}" - type would be dict

# 2

s = {2, 4, 2, 6}
print(s)
#{2, 4, 6}


# 3

s = {True, "John", 19 ,"Pune"}
print(s)
#{'John', True, 19, 'Pune'}


# 4

#print(s[1]) #'set' object is not subscriptable


# 5

s = {}
print(type(s)) #<class 'dict'>

s = set()
print(type(s)) #<class 'set'>