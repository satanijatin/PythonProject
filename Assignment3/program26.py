#  What is Instantiation in terms of OOP terminology

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


my_car = Car("Toyota", "Camry")


print(my_car.make) 
print(my_car.model) 
