#******************* I] Map
#Syntax : list_name = list(map(function_name, iterable object))........... iterable object= list, tuple 

def sq(x):
    return x*x


l = [1,2,3,4,5,6,7]
ls =[]
for i in l:
    ls.append(sq(i))

print(ls)
[1, 4, 9, 16, 25, 36, 49]


#Instead of using for loop and add to new list, we can use map functionality
#Chnage and then append == Map
lst = list(map(sq, l))



#************************ II] Filter

#Syntax : list_name = list(filter(function_name, iterable object))........... iterable object= list, tuple 
# Filter used for Conditional stats => true or false

def sml(x):
    return x<5

list1 = [6,3,1,9,3,2,7,8]

lst1 = list(filter(sml,list1))
print(lst1)
# [3, 1, 3, 2]



#******************** III] Reduce
# Reducing to 1 item

from functools import reduce

list2 = [1,2,3,4,5,6,7,8]

def avg(x,y):
    return x+y/2


lst2 = reduce(avg,list2) #OR lst2 = reduce(lambda x,y: x+y/2, list2)
print(lst2)
# 18.5
