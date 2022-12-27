lst = [11, 45, 62, 29, 36, 89, 34, 45]

#************** I] List Methods

lst.reverse() #[45, 34, 89, 36, 29, 62, 45, 11]
print(lst)

lst.sort()
print(lst) #[11, 29, 34, 36, 45, 45, 62, 89]

lst.sort(reverse=True)
print(lst) #[89, 62, 45, 45, 36, 34, 29, 11]

lst.append(55)
print(lst) #[89, 62, 45, 45, 36, 34, 29, 11, 55]

print(lst.index(29)) #6
print(lst.count(45)) #2



#************* II] Clone Methos

l = lst
l[0] = 0
print(l) #[0, 62, 45, 45, 36, 34, 29, 11, 55]
print(lst) #[0, 62, 45, 45, 36, 34, 29, 11, 55]

l = lst.copy()
l[0] = 1
print(lst) #[0, 62, 45, 45, 36, 34, 29, 11, 55]
print(l) #[1, 62, 45, 45, 36, 34, 29, 11, 55]



#***************** III] Insert, append, extend

lst.insert(1, 60)
print(lst) #[0, 60, 62, 45, 45, 36, 34, 29, 11, 55]

l1 = [11,22,33]
lst.append(l1)
print(lst) #[0, 60, 62, 45, 45, 36, 34, 29, 11, 55, [11, 22, 33]]

lst.extend(l1)
print(lst) #[0, 60, 62, 45, 45, 36, 34, 29, 11, 55, [11, 22, 33], 11, 22, 33]



#******************** IV] + symbol to concatenate lists

list1 = [44,55]
list2 = [66, 77]
list3 = list2 + list1
print(list3) #[66, 77, 44, 55]

