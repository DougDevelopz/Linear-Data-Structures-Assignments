import math

class RegularPolygon:

    def __init__(self, n=3, side=1, x=0, y=0):
        self.n = n
        self.side = float(side)
        self.x = x
        self.y = y

    def getn(self):
        return self.n

    def setn(self, n):
        self.n = n

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getPerimeter(self):
        return self.n * self.side

    def getArea(self):
        return (int(self.n) * int(self.side) ** 2) / (4 * math.tan(math.pi / self.n))


def main():
    # Original Polygon
    defaultPolygon = RegularPolygon()
    print("The perimeter with n as", defaultPolygon.n, "and with a side of", defaultPolygon.side, "is:",
          defaultPolygon.getPerimeter())
    print("The area with the formula being (n*side^2) / (4*tan(PI/n)) is:", defaultPolygon.getArea())

    # Custom Polygon 1
    customPolygon1 = RegularPolygon(6, 4)
    print("The perimeter with n as", customPolygon1.n, "and with a side of", customPolygon1.side, "is:",
          customPolygon1.getPerimeter())
    print("The area with the formula being (n*side^2) / (4*tan(PI/n)) is:", customPolygon1.getArea())

    # Custom Polygon 2
    customPolygon2 = RegularPolygon(10, 4, 5.6, 7.8)
    print("The X cord for this regular polygon is:", customPolygon2.x)
    print("The Y cord for this regular polygon is:", customPolygon2.y)
    print("The perimeter with n as", customPolygon2.n, "and with a side of", customPolygon2.side, "is:", customPolygon2.getPerimeter())
    print("The area with the formula being (n*side^2) / (4*tan(PI/n)) is:", customPolygon2.getArea())


main()
