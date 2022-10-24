from .figure import Figure
from .color import Color

class Rect(Figure):
    def __init__(self, width, height, color):
        self.name = "Rectangle"
        self.width = width
        self.height = height
        self.color = Color(color)
    
    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Figure: {}, Weight: {}, Height: {}, Color: {}".format(
            self.getName(),
            self.width,
            self.height,
            self.color
        )
