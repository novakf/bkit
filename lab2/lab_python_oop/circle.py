from .figure import Figure
from .color import Color
from math import pi

class Circle(Figure):
    def __init__(self, radius, color):
        self.name = "Circle"
        self.radius = radius
        self.color = Color(color)
    
    def area(self):
        return pi * (self.radius ** 2)

    def __repr__(self):
        return "Figure: {}, Radius: {}, Color: {}".format(
            self.getName(),
            self.color,
            self.radius,
        )