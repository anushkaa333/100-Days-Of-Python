lst = [9,67, 45, 34, 78, 234, 846, 555, 11, "john", True]

# ********* I]
print(lst) #print(lst[:])
print(type(lst)) #<class 'list'>


# ************ II] Slicing with +/-ve and 3 numbers

print(lst[1:]) #[67, 45, 34, 78, 234, 846, 555, 11, 'john', True]
print(lst[:6]) #[9, 67, 45, 34, 78, 234]
print(lst[2:4]) #[45, 34]
print(lst[-2:]) #['john', True]
print(lst[:-4]) #[9, 67, 45, 34, 78, 234, 846]
print(lst[-5:-1]) #[846, 555, 11, 'john']

print(lst[1:5:2])#[67, 34]........67, 45, 34, 78,
print(lst[3:10:3])#[34, 846, 'john'].........34, 78, 234, 846, 555, 11, "john",


#************* III] If-Else, in keyword

if "john" in lst:
    print("yes")
else:
    print("no")

#yes

#************ IV] For-loop

lst1 = [i for i in lst]
print(lst1) #[9, 67, 45, 34, 78, 234, 846, 555, 11, 'john', True]


lst2 = [i*i for i in range(4)]
print(lst2) #[0, 1, 4, 9]

lst3 = [i*i for i in range(4) if i%2==0]
print(lst3) #[0, 4]



