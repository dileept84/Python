# single level inheritance  ---- B class extends All properties of A class

class A:
    def feature1(self):
        print("feature 1")
    def feature2(self):
        print("feature 2")

class B(A):
    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")

b1 = B()
b1.feature1()

#Multilevel inheritance  F class extends D class and D extends C class

class C:
    def feature5(self):
        print("feature 5")
    def feature6(self):
        print("feature 6")

class D(C):
    def feature7(self):
        print("feature 7")

    def feature8(self):
        print("feature 8")
class F(D):
    def feature9(self):
        print("feature 9")

    def feature10(self):
        print("feature10")

f1 = F()
f1.feature7()


#Multipal inheritance  I class extends G and H class properties

class G:
    def feature11(self):
        print("feature 11")
    def feature12(self):
        print("feature 12")

class H():
    def feature13(self):
        print("feature13")

    def feature14(self):
        print("feature 14")

class I(G,H):
    def feature15(self):
        print("feature 15")

    def feature16(self):
        print("feature16")

I1 = I()

I1.feature13()
I1.feature12()


#Constructor in inheritance
class X:
    def __init__(self):    #defining consturctor method
        print("in X init")

    def feature0(self):
        print("feature 0")

class Y():

    def __init__(self):
        print("in Y init")

    def feature01(self):
        print("feature01")


class Z(X,Y):

    def  __init__(self):
        print("in Z init")  # by Super() method we can call parent class constructor
        super().__init__()  # calling init method of super class (it calls from left to right so it will call
                            #init method of X )

    def feature02(self):
        print("feature 02")

z1= Z()   # creating object
z1.feature01()