    #                     A
    #                     |
    #     - - - - - - - - - - - - - - - - - - - - - -
    #     |             |            |               | 
    #     B             C            D               E
    #     |             |                            |
    # - - - - -         -                        - - - - -
    # |        |        |                        |    |   |
    # F        G        H                        I    J   K


#Single => No siblings
#Multilevel => Extended form of single inheritance - No Siblings
#Multiple => class formed using 2 or more parent classes


class A:
    def funA(self):
        print("Class A")

class B(A):
    def funB(self):
        print("Class B")

class C(A):
    def funC(self):
        print("Class C")


class D(A):
    def funD(self):
        print("Class D")

class E(A):
    def funE(self):
        print("Class E")

class F(B):
    def funF(self):
        print("Class F")

class G(B):
    def funG(self):
        print("Class G")

class H(C):
    def funH(self):
        print("Class H")

class I(E):
    def funI(self):
        print("Class I")

class J(E):
    def funJ(self):
        print("Class J")

class K(E):
    def funK(self):
        print("Class K")


k = K()
k.funK()
k.funA()
k.funE()

# Class K
# Class A
# Class E