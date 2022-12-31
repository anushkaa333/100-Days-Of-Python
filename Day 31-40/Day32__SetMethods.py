
#******************** I] Union

s1 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
s2 = {'Solapur', 'Kolhapur', 'Nagpur', 'Nashik'}
s3 = s1.union(s2)
print(s3)#{'Pune', 'Mumbai', 'Kolhapur', 'Nagpur', 'Nashik', 'Solapur', 'Latur'}

s4 = s1.update(s2)
print(s4)# None - Bcoz s1 gets update ONLY not s4

s1.update(s2)
print(s1) #{'Mumbai', 'Latur', 'Pune', 'Solapur', 'Kolhapur', 'Nashik', 'Nagpur'}


#***************** II] Intersection - common in both sets

s11 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
s12 = {'Solapur', 'Kolhapur', 'Nagpur', 'Nashik'}
s13 = s11.intersection(s12)
print(s13) #{'Nashik', 'Nagpur'}


s14 = s11.intersection_update(s12)
print(s14) #None
print(s11) #{'Nagpur', 'Nashik'}#


#********************* III] Symmetric Difference - Not common in both sets

s31 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
s32 = {'Solapur', 'Kolhapur', 'Nagpur', 'Nashik'}
s33 = s31.symmetric_difference(s32)
print(s33) #{'Pune', 'Solapur', 'Latur', 'Mumbai', 'Kolhapur'}

s34 = s31.symmetric_difference_update(s32)
print(s34) #None
print(s31) #{'Kolhapur', 'Mumbai', 'Latur', 'Pune', 'Solapur'}


#*************************** IV] Difference

s1 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
s2 = {'Solapur', 'Kolhapur', 'Nagpur', 'Nashik'}
s3 = s1.difference(s2) # Present in A but not in B
print(s3) #{'Latur', 'Pune', 'Mumbai'}

s3 = s2.difference(s1)
print(s3) #{'Solapur', 'Kolhapur'}

s3 = s1.difference_update(s2)
print(s3)#None
print(s1)#{'Pune', 'Mumbai', 'Latur'}



#******************************* V] Add

s1 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik'}
print(s1) #{'Mumbai', 'Nashik', 'Pune', 'Nagpur'}
s1.add('Latur')
print(s1) #{'Pune', 'Mumbai', 'Nashik', 'Nagpur', 'Latur'}


#************************** VI] Remove / Discard

s1 = {'Pune', 'Mumbai', 'Nashik', 'Nagpur', 'Latur'}
print(s1) #{'Pune', 'Mumbai', 'Nashik', 'Nagpur', 'Latur'}
s1.remove('Latur')
print(s1) # {'Nashik', 'Pune', 'Mumbai', 'Nagpur'}


# remove in case throws it wont run below code, for this use discard


s1.discard('Latur')
print(s1) #{'Nashik', 'Pune', 'Mumbai', 'Nagpur'}

s1.discard('Pune')
print(s1) #{'Mumbai', 'Nashik', 'Nagpur'}



#***************************** VII] Pop

print(s1.pop()) # Mumbai
print(s1) #{'Nashik', 'Nagpur'}


#***************************** VIII] Del/ Clear

#Del will delete the set and throw NameError, if try to print but clear will keep set as it is and remove elements

s1 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
del s1
#print(s1) #NameError: name 's1' is not defined. Did you mean: 's2'?



s2 = {'Solapur', 'Kolhapur', 'Nagpur', 'Nashik'}
s2.clear()
print(s2) #set()



####################################### CONDITIONAL

#*************************** I] Disjoint - 2 sets should be independent


s1 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
s2 = {'Solapur', 'Kolhapur', 'Nagpur', 'Nashik'}
print(s1.isdisjoint(s2)) #False

s1 = {'Pune', 'Mumbai', 'Latur'}
s2 = {'Solapur', 'Kolhapur'}
print(s1.isdisjoint(s2)) #True


#************************ II] Superset

s1 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
s2 = {'Solapur', 'Kolhapur', 'Nagpur', 'Nashik'}
print(s1.issuperset(s2)) #False


s1 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
s2 = {'Nagpur', 'Nashik'}
print(s1.issuperset(s2)) #True


#*************************** III] Subset


s1 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
s2 = {'Solapur', 'Kolhapur', 'Nagpur', 'Nashik'}
print(s2.issubset(s1)) #False


s1 = {'Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Latur'}
s2 = {'Nagpur', 'Nashik'}
print(s2.issubset(s1)) #True










 