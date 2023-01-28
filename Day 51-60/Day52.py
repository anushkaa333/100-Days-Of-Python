#****************** I] Normal Function

def cube(x):
    return x*x*x

ans = cube(2)
print(ans) #8


#******************* II] Lamba function - used for single liner function

square = lambda x : x*x
print(square(2)) #4


#******************* III] Passed function to function

def sum(fx, value):
    return 8 + fx(value)


a = sum(square, 3)
print(a) #17


#********************* IV] Passed function(function functionality) to function

avg = lambda x,y,z: x+y+z/3
print(avg(1,2,3)) #4.0


def av(fx, val1, val2, val3):
    return fx(val1, val2, val3)

print(av(lambda x,y,z: x+y+z/3, 0,1,2))
#1.6666666666666665