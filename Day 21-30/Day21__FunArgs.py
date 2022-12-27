#******************DEFAULT ARGUMENTS

#************ Ex 1
def add(a=6, b=7): #required args
    c = a+b
    print("sum is", c)
    # return c

add() #sum is 13


#************ Ex 2
def add(a=6, b=7): #required args
    c = a+b
    print("sum is", c)

add(3,4) #sum is 7


#************ Ex 3
def add(a=6, b=7): #required args
    c = a+b
    print("sum is", c)

add(3) # a=3, b=7
#sum is 10


#************ Ex 4
def add(a=6, b=7): #required args
    c = a+b
    print("sum is", c)

add(b=3) # a=6
#sum is 9


#************ Ex 5
# def add(2, 3): #invalid syntax
#     c = a+b
#     print("sum is", c)

# add(5,6) 




#******************************* KEYWORD LENGTH ARGUMENTS
def add(a, b, d): #required args
    c = a+b+d
    print("sum is", c)

add(2, 3, 1) 
#sum is 6





#********************************* VARIABLE LENGTH

def add_multipleNo(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Sum is", sum)


add_multipleNo(1,2,3,4,5,6)



# def add_multipleNo(*numbers):
#     print("Sum is", sum(numbers))


# lst = [1,2,3,4,5,6]
# add_multipleNo(lst)

# TypeError: unsupported operand type(s) for +: 'int' and 'list'