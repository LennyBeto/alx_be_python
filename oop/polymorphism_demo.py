# polymorphism_demo.py

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def main():
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    # Calculate and print areas
    print(f"Area of Rectangle: {rectangle.area()}")
    print(f"Area of Circle: {circle.area()}")

if __name__ == "__main__":
    main()
#main.py
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
