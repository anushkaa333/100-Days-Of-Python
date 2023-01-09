marks = [11, 44, 33, 78, 23, 40, 26, 81]


#************************** I]
index = 0
for mark in marks:
    print(mark)
    if(index==3):
        print(f"Index is {index}")
    index+=1


# 11
# 44
# 33
# 78
# Index is 3
# 23
# 40
# 26
# 81


#************************* II] Start Index from 0 - by default

for index, mark in enumerate(marks):
    print(f" Marks at Index {index} is {mark}")
    if(index==3):
        print(f"curr index is {index}")

# Marks at Index 0 is 11
#  Marks at Index 1 is 44
#  Marks at Index 2 is 33
#  Marks at Index 3 is 78
# curr index is 3
#  Marks at Index 4 is 23
#  Marks at Index 5 is 40
#  Marks at Index 6 is 26
#  Marks at Index 7 is 81



#************************* III] Different start index

for index, mark in enumerate(marks, start=2):
    print(f" Marks at Index {index} is {mark}")
    if(index==3):
        print(f"curr index is {index}")

# Marks at Index 2 is 11
#  Marks at Index 3 is 44
# curr index is 3
#  Marks at Index 4 is 33
#  Marks at Index 5 is 78
#  Marks at Index 6 is 23
#  Marks at Index 7 is 40
#  Marks at Index 8 is 26
#  Marks at Index 9 is 81