def test1(t1):
    def test2(*a, **aa):
        print("Start")
        t1(*a, **aa)
        print("End")
    return test2

@test1
def hello():
    print("Hello Python")

@test1
def sum(a,b):
    print(a+b)


hello()
sum(10,20)
