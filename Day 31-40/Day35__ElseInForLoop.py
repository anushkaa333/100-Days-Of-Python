# Q : Else used in for loop or not 

# A : Break stat applied in for loop else wont execute as in Ex.2, Otherwise if break not applied then else will execute


#***************** Ex.1
for i in range(4):
    print(i)
else:
    print("Value of iteration", i)
    print("Value of wont increment")

# 0
# 1
# 2
# 3
# Value of iteration 3
# Value of wont increment



#***************** Ex.2
for i in range(7):
    print(i)
    if i==5:
        break
    
else:
    print("Value of iteration", i)
    print("Value of wont increment")

# 0
# 1
# 2
# 3
# 4
# 5