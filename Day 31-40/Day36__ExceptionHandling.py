

#********************* Ex.1

a = input("Enter Input")

try:
    num = 2 * int(a)
    print(num)
except Exception as e:
    print(e)
    


#********************** Ex.2

lst = [6, 7]
a = input("Enter input")
try:
    print(lst[a])
    
except ValueError:
    print("Entered input is not integer")
except IndexError:
    print("index out of range")