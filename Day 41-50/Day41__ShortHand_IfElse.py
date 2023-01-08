#Short hand of ifelse - this short hand must be written in single line as in EX.1


#****************** Ex.1
a = 30
b = 40
print("A") if a>b else print("B") if b>a else print("A = B")
#B



#****************** Ex.2 - If you write one below other it will throw error - InvalidSyntax
# a = 30
# b = 40
# print("A") if a>b else 
# print("B") if b>a else 
# print("A = B")



 
#****************** Ex.3 - Even with intendation - it'll throw error
# a = 30
# b = 40
# print("A") if a>b else
#     print("B") if b>a else 
#         print("A = B")



# a = 30
# b = 40
# print("A") if a>b 
#     else print("B") if b>a 
#         else print("A = B")