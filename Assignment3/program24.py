#  Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 


import math

class Circle:
  
    def __init__(self, radius):
        self.radius = radius

 
    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area

   
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


my_circle = Circle(radius=4)


area_of_circle = my_circle.calculate_area()
print(f"The area of the circle is: {area_of_circle}")

perimeter_of_circle = my_circle.calculate_perimeter()
print(f"The perimeter of the circle is: {perimeter_of_circle}")
