#  What is used to check whether an object o is an instance of class A

class A:
    pass

class B(A):
    pass

class C():
    pass

obj_a = A()
obj_b = B()
obj_c = C()

print(isinstance(obj_a, A))  
print(isinstance(obj_b, B)) 
print(isinstance(obj_c, C)) 
