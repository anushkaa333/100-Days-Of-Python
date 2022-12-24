# ************** Ex 1 ********

i = 0
while(i<3):
    print(i)
    i = i+1

# 0
# 1
# 2

# ************* Ex 2 ************
count = 5
while(count > 0):
    print(count)
    count = count - 1

# 5
# 4
# 3
# 2
# 1

# **************** Ex 3 *************
num = int(input("Enter number"))

while(num<=38):
    num = int(input("Enter the num"))
    print(num)
print("Done with loop")

# Enter number23
# Enter the num23
# 23
# Enter the num34
# 34
# Enter the num38
# 38
# Enter the num39
# 39
# Done with loop




# ****************** Do While in python *************

x = 1
while True:
    print(x)
    x = x+1
    if(x%5==0):
        break
    # x= x+1



# 1
# 2
# 3
# 4
# 5