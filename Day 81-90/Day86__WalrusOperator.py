# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

# Here's an example of how you can use the Walrus Operator in a while loop:



#********* I]
a = True
print(a)
# O/P => True

#********* II]
# print(b = True)

# O/P => TypeError: 'b' is an invalid keyword argument for print()
#Declaration and initialization is not allowed in print stat at the time


#********* III]
c = True

#1.
# print(c = False)
#TypeError: 'c' is an invalid keyword argument for print()

#2.
# print(c:=False)
# False
#Walrus operator used for assigning/changing the prev value in stats like print and while



#********* IV]

numbers = [1,2,3,4,5]

while (n:= len(numbers)) > 0:
    print(numbers.pop())


# 5
# 4
# 3
# 2
# 1


#********* V]

names = ["ABC", "PQR", "XYZ"]

if (name:= input("Enter name")) in names:
    print(f"{name}")
else:
    print("invalid")

# Enter namea
# invalid


# Enter nameABC
# ABC

#******** VI]


foods = list()
while True:
    food = input("Enter food")
    if food == 'quit':
        break
    foods.append(food)

print(foods)


# OR


foods = list()
while (food:=input("Enter food")) != 'quit':
    foods.append(food)

print(foods)


# Enter foodx
# Enter foody
# Enter foodz
# Enter foodquit
# ['x', 'y', 'z']

