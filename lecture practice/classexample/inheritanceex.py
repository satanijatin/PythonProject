class A:

    def __init__(self):
        print("Hello world")

    def display(self):
        print("first class is A")

class B(A):

    def __init__(self):
        print("hello")
    

    def display(self):
        print("Second class is B")

class C(B):

    def __init__(self):
        print("hello C")
    

    def display(self):
        print("Third class is C")

a=A()
a.display()
b=B()
b.display()
c=C()
c.display()
        