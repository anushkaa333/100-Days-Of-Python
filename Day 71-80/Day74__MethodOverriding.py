
#******************** I]


class shape:
    def __init__(self, x, y):
        self.width = x
        self.height = y

    def method(self):
        return self.width * self.height


class circle(shape):
    def __init__(self, r):
        self.radius = r
        super().__init__(r, r)

    def method(self):
        return 3.14 * super().method()     
    


c = circle(3)
print(c.method())
#28.26



#*************************  II]



class shape:
    def __init__(self, x, y):
        self.width = x
        self.height = y

    def method(self):
        return self.width * self.height


class circle(shape):
    def __init__(self, r):
        self.radius = r
        super().__init__(r, r)

    


c = circle(3)
print(c.method())
#9