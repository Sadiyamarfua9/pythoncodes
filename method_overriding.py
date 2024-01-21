class Shape:
    def calculate_area(self):
        pass
        # This method is a placeholder in the base class and will be overridden by subclasses.
        # Method overriding is a concept in object-oriented programming (OOP) where a subclass
        # provides a specific implementation for a method that is already defined in its superclass.
        # In this case, subclasses like Triangle, Rectangle, and Square will provide their own
        # implementations of calculate_area, tailored to their specific geometric shapes.

# For triangle
class Triangle(Shape):
    def __init__(self, base, height):
        # Initializing the triangle with base and height
        self.base = base
        self.height = height

    def calculate_area(self):
        # Overriding the calculate_area method for triangles
        # The formula for the area of a triangle is 0.5 * base * height
        return 0.5 * (self.base * self.height)

# For rectangle
class Rectangle(Shape):
    def __init__(self, length, breadth):
        # Initializing the rectangle with length and breadth
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        # Overriding the calculate_area method for rectangles
        # The formula for the area of a rectangle is length * breadth
        return self.length * self.breadth

# For square
class Square(Shape):
    def __init__(self, side):
        # Initializing the square with the side length
        self.side = side

    def calculate_area(self):
        # Overriding the calculate_area method for squares
        # The formula for the area of a square is side * side
        return self.side ** 2

# Creating objects and testing the classes
triangle_obj = Triangle(5, 8)
print('Area of triangle:', triangle_obj.calculate_area())

rectangle_obj = Rectangle(10, 20)
print('Area of Rectangle:', rectangle_obj.calculate_area())

square_obj = Square(15)
print('Area of square:', square_obj.calculate_area())
