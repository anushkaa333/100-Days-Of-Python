#Tuples are immutable


#******************** I] Print multiple numbers
tup = (11, 22, 33, 44, 55, 66)
print(tup, type(tup)) #(11, 22, 33, 44, 55, 66) <class 'tuple'>


#******************* II] Print single number

tup1 = (11)
print(tup1, type(tup1)) #11 <class 'int'>

#In order to make this tuple (with 1 value) and not int, always write "," at the end

tup2 = (11,)
print(tup2, type(tup2)) #(11,) <class 'tuple'>

#********************** III] Indexing
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1]) #66


#********************* IV] Slicing

print(tup[1:5]) #(22, 33, 44, 55)


#****************** V] In keyword

tup3 = (11, 22, 33, 44, 55, 66, "john")

if "66" in tup:
    print("66 present")
else:
    print("Not present") #Not present



if "john" in tup3:
    print("John present") #John present
else:
    print("John Not present") 
