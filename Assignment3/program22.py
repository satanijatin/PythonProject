# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

class Family:
    cast = "Patel"
    
   
    def __init__(self, name, age):
        self.name = name
        self.age = age

   
    def display_info(self):
        print(f"{self.name} is {self.age} years old and belongs to the {self.cast}")


myfamliy = Family(name="Jatin", age=29)

myfamliy.display_info()
