import math

# Define base class Shape with method area
class Shape:
    def area(self):
        raise NotImplementedError

# Define derived class Rectangle with method area overriding area method in base class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Define derived class Cirle with method area overriding area method in base class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius