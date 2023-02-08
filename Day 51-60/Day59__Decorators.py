
#**************** Decorators - Used for adding content before and after function

# I] Create a function - named grtings
# II] Add the new content before and after using decorator as function - named greet
    # 2.1] Pass the decorator a function as arg, here fx
    # 2.2] For adding content, always write content within function and return same function
# III] Call funtion crated in [I]

#************* I] Ex.1

def greet(fx):
    def greet_fun():
        print("Hello World")
        fx()
        print("Good morning")
    return greet_fun 


@greet
def grtings():
    print("Namaste")

grtings()
# Hello World
# Namaste     
# Good morning

#******* OR


# def greet(fx):
#     def greet_fun():
#         print("Hello World")
#         fx()
#         print("Good morning")
#     return greet_fun 


# def grtings():
#     print("Namaste")

# greet(grtings)()

#***************** II] Ex.2

def addd(fx):
    def add_prog(*args, **kwargs): #*args - accept args in tuples, **kwargs - accept args in the form of dict 
        print("Welcome to add prog")
        fx(*args, **kwargs)
        print("Done!!!!")
    return add_prog


# @addd
def add (a,b):
    print (a+b) #return stats arent allowed in this function

# ans = addd(add)(3,4)  #Storing value in the variable will give output as 'None', hence dont store. Storing usually happens in case return stat but return is not applicable in decorators as above
# print(ans)
# Welcome to add prog
# 7
# Done!!!!
# None

addd(add)(3,4)
# Welcome to add prog
# 7
# Done!!!!
