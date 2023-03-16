# Generator

# To generate the values on-the -fly
# To create and store the sequence in memory
# Values are generated as per user's need
# It saves memory space unlike list, tuple


# (In list and tuple, we'll need to store values at a time and then print, this wastes the memory,
# But in case of generators, values are not stored anywhere, it will get printed immediately)


#  Yield is used print the values OUTSIDE function
# 1.(Even return stat can print the values outside function but it wont iterate futher inside function loop)
# 2.(Print stats can also print values inside function but not outside)




import time

def my_generator():
    for i in range(5):
      yield i 


gen = my_generator()
# print(gen) #<generator object my_generator at 0x000002CABD864040>

for j in gen:
   print(j)



# 0
# 1
# 2
# 3
# 4



