


#*********************** I] Without finally

# Usually return stat wont execute below lines of code but if write finally keyword it will execute block of code in finally

def mult():

    a = input("Enter Input")
    
    try:
        num = 2 * int(a)
        print(num)
        return 1
    
    except Exception as e:
        print(e)
        return 0
    
    print("Finally stat executed")


ans = mult()
print(ans)

# Enter Input45
# 90
# 1

# Enter Inputaa
# invalid literal for int() with base 10: 'aa'
# 0



#****************************** II] With Finally

def mult():

    a = input("Enter Input")
    
    try:
        num = 2 * int(a)
        print(num)
        return 1

    except Exception as e:
        print(e)
        return 0
    
    finally:
        print("Finally stat executed")

        
ans = mult()
print(ans)

# Enter Input34
# 68
# Finally stat executed
# 1

#Enter Inputaa
# invalid literal for int() with base 10: 'aa'
# Finally stat executed
# 0