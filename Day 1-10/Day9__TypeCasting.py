# Boolean => byte => short => char => int => long => float => double ......... Implicit (Widening)
# Double => float => long => int => char => short => byte => boolean ......... Explicit (Narrowing)

num1 = "45"
num2 = "10"

# print("Sum of 2 numbers" + int(num1) + int(num2)) 
# #  print("Sum of 2 numbers", (int)num1+ (int)num2)
# #                                ^^^^^^^^^^^^^^^
# # SyntaxError: invalid syntax. Perhaps you forgot a comma?

print("Sum of 2 numbers", int(num1) + int(num2)) #Sum of 2 numbers 55
print("Sum of 2 numbers"+ num1+ num2) #Sum of 2 numbers4510
print("Sum of 2 numbers", num1+ num2) #Sum of 2 numbers 4510

