class GeometricObject:

    def __init__(self, color = "green", filled = True):
        self.color = color
        self.filled = filled


    def getColor(self):
        return self.color

    def setColor(self):
        self.color = self.color

    def isFilled(self):
        return self.filled

    def setFilled(self):
        self.filled = self.filled

    def __str__(self):
        return "color: " + self.color + \
            " and filled: " + str(self.filled)
