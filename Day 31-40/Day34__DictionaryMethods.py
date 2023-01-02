dic1 = {1:'Ram', 2:'Sita', 4:'Sugriv', 3:'Wali'}
dic2 = {6:'Krishna', 16:'Yudhishthir', 14:'Gandhari', 12:'Arjun'}

#*********** I] Update


dic1.update(dic2)
print(dic1) 
#{1: 'Ram', 2: 'Sita', 4: 'Sugriv', 3: 'Wali', 6: 'Krishna', 16: 'Yudhishthir', 14: 'Gandhari', 12: 'Arjun'}


#************ II] Pop
# a = dic1.pop(14)
# print(a) 
print(dic1.pop(14)) #Gandhari
print(dic1) # {1: 'Ram', 2: 'Sita', 4: 'Sugriv', 3: 'Wali', 6: 'Krishna', 16: 'Yudhishthir', 12: 'Arjun'}


#************* III] Popitem - deletes last item
print(dic1.popitem()) #(12, 'Arjun')
print(dic1) # {1: 'Ram', 2: 'Sita', 4: 'Sugriv', 3: 'Wali', 6: 'Krishna', 16: 'Yudhishthir'}

# print(del dic1(1)) #SyntaxError: invalid syntax


#************** IV] Delete item from dict
# a = del dic1[1]
# print(a)

del dic1[1]
print(dic1)#{2: 'Sita', 4: 'Sugriv', 3: 'Wali', 6: 'Krishna', 16: 'Yudhishthir'}


#************** V] Clear - deletes all items

dic2.clear()
print(dic2) #{}


#*************** VI] Delete all items along with its structure

del dic2
print(dic2)
#NameError: name 'dic2' is not defined.

