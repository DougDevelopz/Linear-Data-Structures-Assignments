import math

from GeometricObject import GeometricObject

class Triangle(GeometricObject):

    def __init__(self, color, filled, side1 = 1.0,side2 = 1.0,side3 = 1.0):
        super().__init__(color,filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getSide1(self):
        return self.side1

    def getSide2(self):
        return self.side2

    def getSide3(self):
        return self.side3

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return math.sqrt(area)

    def getPerimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return "The Triangle Area is " + str(self.getArea()) + \
            "\nThe Triangle Perimeter is " + str(self.getPerimeter()) + "\n" \
            "The Triangle Color is: " + self.color  + "\n" \
            "The Triangle is filled: " + str(self.filled)


