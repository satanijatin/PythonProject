class A:

    def __init__(self,name):
        self.name=name
        # print("Hello world")

   

    def displaya(self):
        print(f"first class is A {self.name}")

class B():

    def __init__(self):
        print("hello")

    def displayb(self):
        print("Second class is B")


aa=A("jatin")
aa.displaya()

bb=B()
bb.displayb()

