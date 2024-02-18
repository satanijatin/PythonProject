# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")


print(my_dog.speak())
print(my_cat.speak())  
