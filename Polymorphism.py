# Polymorphism - poly means many morph means form
# one  thing can take multiple forms
# 4 ways of implementing polymorphism
# duck typing , Operator overloadming, method overloading, method overriding

# Duck Typing - Here we have a method execute which is behaving same. we creating object of either A or B

class B:
    def execute(self):
        print("commpiling")
        print("running")

class A:
    def execute(self):
        print("Spell check")
        print("convention check")
        print("commpiling")
        print("running")


class D:
    def code(self,ide):
        ide.execute()

ide = A()
d1 = D()
d1.code(ide)

#Operator overloading

class student:

    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    def __str__(self):
       # return self.m1 , self.m2  # it gives an error for __str__ returned non-string (type tuple) so for this we need to return it as string
       return "{} {}".format(self.m1,self.m2)


s1 = student(58,69)
s2 = student(68,45)
s3 = s1 +  s2   # it give an error unsupported operand types for student + student
print(s3.m2)
print(s1)   # it will give the address not value because it is passing str type so for we need to define str method
print(s2)

#method Overloading

class student:

    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s= a+b
        else:
            s=a
        return s
s1 = student(12,14)
print(s1.sum(12,15))


#Method Overriding

class A:
    def show(self):
        print("show method")

class B(A):
    def show(self):
        print("show method of B")

a1= B()
a1.show()
