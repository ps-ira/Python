import math

class Polygon:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

def main():
    print("Area of Triangle:")
    triangle = Triangle(10, 5)
    print(f"Area: {triangle.area()}")

    print("\nArea of Rectangle:")
    rectangle = Rectangle(4, 6)
    print(f"Area: {rectangle.area()}")

    print("\nArea of Circle:")
    circle = Circle(7)
    print(f"Area: {circle.area()}")

if __name__ == "__main__":
    main()
