class A:

    def __init__(self):
        print("Hello world")

    def display(self):
        print("first class is A")

class B(A):

    def __init__(self):
        print("hello")
    

    def display(self):
        print("first class is B")

a=A()
a.display()
b=B()
b.display()
        