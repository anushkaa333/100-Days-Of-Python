#Catching Memory -  Cache is maintained for current running program


# If curr program is ran for some values then same values appear next time then it wont take time to execute the function for those values
# ONLY for current running program

import functools #*OR* from functools import lru_cache
import time


@functools.lru_cache(maxsize=None) # *OR* @lru_cache(maxsize=None)
def func(x):
    time.sleep(5)
    return x*2


print(func(2))
print("Done for 2")

print(func(4))
print("Done for 4")

print(func(11))
print("Done for 11")


print(func(2))
print("Done for 2")

print(func(4))
print("Done for 4")

print(func(7))
print("Done for 7")


print(func(11))
print("Done for 11")