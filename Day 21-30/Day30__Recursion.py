def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Enter number"))
num = factorial(n)
print("Factorial is", num)


#Enter number4
#Factorial is 24





def fibbo(n, a , b, c,  count):
    
    if(count-1 == n):
        return c

    else:
        c = a+b
        print(c)
        a = b
        b = c
        return fibbo(n, a , b, c, count=count+1)



n = int(input("Enter number"))
if(n == 0):
    print("0 is at index zero")
    
elif(n==1):
    print("1 is at index zero")
 
else:   
    a =0
    b =1
    c = a+b
    count = 2
    num = fibbo(n, a, b, c, count)
print("Fibonacci is", num)


# Enter number4
# 1
# 2
# 3
# Fibonacci is 3