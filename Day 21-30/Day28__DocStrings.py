# Docstrings are written immediate next to function name

#***************** I] Doc string immediate next to function name

def add(a, b):
    ''' Addition of 2 numbers''' # Can be written in single and double quotes
    num = a+b
    print(num)

add(4, 5)
print(add.__doc__)

# 9
#  Addition of 2 numbers



#********************** II] Display output if Doc string not written immediate next to function name

def add(a, b):
    num = a+b
    print(num)
    'Addition of 2 numbers'

add(4, 5)
print(add.__doc__)

# 9
# None