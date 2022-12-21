print("****************Calculator **************")

num1 = float(input("Enter 1st Number"))
num2 = float(input("Enter 2nd Number"))

print("\n1. Additon \n2.Subtraction \n3.Multiplication \n4.Division")
c = int(input("Enter choice"))


if c==1:
    print("Additon of numbers: " , num1+num2)

elif c==2:
    print("Subtraction of numbers: " , num1-num2)


elif c==3:
    print("Subtraction of numbers: " , num1*num2)


elif c==4:
    print("Subtraction of numbers: " , num1/num2)

else:
    print("Invalid Input")

# ****************Calculator **************
# Enter 1st Number3
# Enter 2nd Number5

# 1. Additon
# 2.Subtraction
# 3.Multiplication
# 4.Division
# Enter choice3
# Subtraction of numbers:  15.0