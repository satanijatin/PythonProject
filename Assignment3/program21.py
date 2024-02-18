#  What are oops concepts? Is multiple inheritance supported in java 

class ClassA:
    def method_A(self):
        print("Method A from ClassA")

class ClassB:
    def method_B(self):
        print("Method B from ClassB")

class ClassC(ClassA, ClassB):
    def method_C(self):
        print("Method C from ClassC")


obj = ClassC()
obj.method_A()
obj.method_B()
obj.method_C()
