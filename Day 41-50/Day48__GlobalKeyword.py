#****************** I] Value doesnt change

x = 3

def fun1():
    x=4
    print("Value of x", x)


print("Value of x", x) #3
fun1()#4
print("Value of x", x)#3



#********************** II] Value changes if we pass args and perform operations
#************ If we dont pass args and perform operations then value wont change
y = 3

def fun2(yy):
    y= yy+4
    print("Value of y", y)


print("Value of y", y) #3
fun2(3)#7
print("Value of y", y)#3



#************************* III] Global keyword


z = 3

def fun3():
    global z
    z=4
    print("Value of z", z)


print("Value of z", z) #3
fun3()#4
print("Value of z", z)#4
