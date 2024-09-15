import math
from statistics import multimode


class Shape:
    width = 0
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Shape):
    # def __init__(self, width, height):
    #     self.width = width
    #     self.height = height

    degree = 0

    def __init__(self, width, height):
        super().__init__(width, height)
        self.degree = 90


    def draw(self):
        print("Drawing rectangle " + str(self.width) + " x " + str(self.height))


    def area(self):
        print(self.width * self.height)


class ColorRectangle(Rectangle):
    color = ""
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color

    def draw(self):
        super().draw()
        print("Drawing color " + self.color)


class Parallelogram(Rectangle):
    def __init__(self, width, height, degree):
        super().__init__(width, height)
        super().degree = degree # 120



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print("Drawing circle")
        print(self.radius)

    def area(self):
        print(math.pi * math.pow(self.radius, 2))


rectangle = Rectangle(5, 5)
circle = Circle(5)

rectangle.area()
circle.area()


color_rectangle = ColorRectangle(5, 5, "red")
color_rectangle.draw()


class Computer:
    def __init__(self,model, *args, **kwarks):
        super().__init__(*args, **kwarks)
        self.model = model
        self.memory = 128
class Display:
    def __init__(self, *args, **kwarks):
        super().__init__(*args, **kwarks)
        self.resolution = "4k"
class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)


iphone = SmartPhone(model = "Last")
iphone.print_info()