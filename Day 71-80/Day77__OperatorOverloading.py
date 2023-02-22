class Vtr:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    

    # def __add__(self , x):
    #     return f"{self.i + x.i}i + {self.j+x.j}j + {self.k+x.k}k" #Its class type is str


    def __add__(self , x):
        return Vtr(self.i + x.i, self.j+x.j, self.k+x.k) #Its class type is Vector

    

v1 = Vtr(2,3,4)
print(v1)
# 2i + 3j + 4k

v2 = Vtr(4,5,6)
print(v2)
# 4i + 5j + 6k

print(v1 + v2)
# 6i + 8j + 10k
# print(type(v1 + v2)) #<class 'str'>
print(type(v1 + v2)) # <class '__main__.Vtr'>
