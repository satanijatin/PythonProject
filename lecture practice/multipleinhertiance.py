class A:

    def __init__(self):
        print("Hello world")

    def displaya(self):
        print("first class is A")

class B():

    def __init__(self):
        print("hello")

    def displayb(self):
        print("Second class is B")

class C(A,B):

    def __init__(self):
        print("hello C")
    

    def displayc(self):
        print("Third class is C")

c=C()
c.displaya()
c.displayb()
c.displayc()
        