#******************I] Import module directly
import math

ans = math.sqrt(9)
print(ans) #3.0
ans1 = math.ceil(ans)
print(ans1) #3


#************** II] Import module with fuctions and methods specified


from math import sqrt, pi

ans = sqrt(4)
print(ans) #2.0
ans1 = ans * pi
print(ans1) #6.283185307179586



#*************** III] Import module with fuctions and methods specified with keyword


from math import sqrt as s, pi as p

print(s(16)) #4.0
print(p) #3.141592653589793


#************* IV] * functionality in import

from math import * # Drawback - If use multiple froms-imports, would be difficult to understand which method comes from which module


#******************* v] Display methods and functions in math module

print(dir(math))
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


# ******************* VI] Importing functions and methods from other files , hre file used (Day44__1)

from Day44__1 import fun, a

fun() 
print(a)
# Its function
# Hello world

