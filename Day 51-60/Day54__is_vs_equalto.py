# is v/s ==

#is => [1] checks identity OR [2] objects pointing to same location in memory
#== => checks value

#************** I] Number String
a = 4
b = "4"

print(a is b)
print(a == b)
# False
# False


#*********** II] Number Number

a = 4
b = 4
# 4 is constant, its value will remain at same location in memory
print(a is b)
print(a == b)
# True
# True


#**************** III] String string

a = "4"
b = "4"

print(a is b)
print(a == b)

# True
# True


#****************** IV] List - Mutable

lst1 = [1,2,3]
lst2 = [1,2,3]

print(lst1 is lst2) #lists sre mutable, values in list can change after some time so its identity wont be same
print(lst1 == lst2)
# False
# True


#******************** V] Tuple - Immtuable

tup1 = (1,2,3)
tup2 = (1,2,3)

print(tup1 is tup2)
print(tup1 == tup2)

# True
# True