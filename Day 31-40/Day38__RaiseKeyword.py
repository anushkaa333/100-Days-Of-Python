num = int(input("Enter value between 5 to 9  "))

if(num<5 or num>9):
    raise ValueError("value not between 5 to 9")

print("value between 5 to 9")



# Enter value between 5 to 9  7
# value between 5 to 9



# Enter value between 5 to 9  3
# Traceback (most recent call last):
#   File "h:\100 Days of Python\Day 31-40\Day38.py", line 4, in <module>
#     raise ValueError("value not between 5 to 9")
# ValueError: value not between 5 to 9