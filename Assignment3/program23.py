#  Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 


class Rectangle:
  
    def __init__(self, length, width):
        self.length = length
        self.width = width

   
    def calculate_area(self):
        area = self.length * self.width
        return area


my_rectangle = Rectangle(length=5, width=8)


area_of_rectangle = my_rectangle.calculate_area()
print(f"The area of the rectangle is: {area_of_rectangle}")
