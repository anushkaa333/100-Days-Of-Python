
#***************** I] Conversion of tuple to list


cities = ('pune', 'mumbai', 'nagpur', 'kolhapur', 'solapur' )
temp = list(cities)
temp[-1] = 'nashik' #('pune', 'mumbai', 'nagpur', 'kolhapur', 'nashik')
temp.append('solapur') #('pune', 'mumbai', 'nagpur', 'kolhapur', 'nashik', 'solapur')
temp.pop(3) #('pune', 'mumbai', 'nagpur', 'nashik', 'solapur')
cities = tuple(temp)
print(cities)


#******************* II] Concatenate

city_1 = ('p', 'm')
city_2 = ('n', 's')

city_3 = city_1 + city_2
print(city_3) #('p', 'm', 'n', 's')


#******************** III] Index, Cont methods

num = (1, 22, 3, 2, 4, 6, 5, 3, 8, 3)
print(num.count(3)) #3
print(num.index(3)) #2

print(num.index(3, 2, 7)) #2  .index(element, start, end) => here value of end is //index number// and not index number - 1

