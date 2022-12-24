#********* Break will skip the loop

i= 0

for i in range(10):
    if(i==6):
        break
    print("5 X", i, "=", 5*i)

# 5 X 0 = 0
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25    

#************* Continue will skip the iteration

i= 0

for i in range(10):
    if(i==6):
        continue
    print("5 X", i, "=", 5*i)

# 5 X 0 = 0
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 0 = 0
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45