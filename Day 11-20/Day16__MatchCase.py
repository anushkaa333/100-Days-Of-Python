#Match-Case in python is similar to switch case in java but it *** DOESNT CONTAIN BREAK stat ***, it will stop automatically once it gets its case


# num = int(input("Enter Number"))
# #num will try to match with case number

# match num:
#     case 0:
#         print("Case 0")

#     case 4:
#         print("Case 4")

#     case _: # _ is default case, if nothing matches 
#         print("Invalid")

    
    
    # case _: # _ is 2nd default case, if above one executes then this and below it wont match
    #     print("Print", num)
    # if we try to write multiple default cases then it'll throw error

# H:\100 Days of Python\Day 11-20>python Day16.py
# Enter Number3
# Invalid

# H:\100 Days of Python\Day 11-20>python Day16.py
# Enter Number4  
# Case 4




# *************Ex 2 *************
num = int(input("Enter Number"))
#num will try to match with case number

match num:
    case 0:
        print("Case 0")

    case 4 if (num%5==0):
        print("Case 4 Divisible by 2")

    case 5 if (num%2==0):
        print("Case 5 Divisible by 5")

    case 6 if num%2==0:
        print(" Case 6 Divisible by 2")


    case _: # _ is default case, if nothing matches 
        print("Invalid")


# H:\100 Days of Python\Day 11-20>python Day16.py
# Enter Number0
# Case 0

# H:\100 Days of Python\Day 11-20>python Day16.py
# Enter Number4
# Invalid

# H:\100 Days of Python\Day 11-20>python Day16.py
# Enter Number6
#  Case 6 Divisible by 2
