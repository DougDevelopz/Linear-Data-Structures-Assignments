import math

class QuadraticFormula:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def geta(self):
        return self.a

    def getb(self):
        return self.b

    def getc(self):
        return self.c

    def getDiscrimant(self):
        return (int(self.b)**2) - (4*self.a*self.c)

    def getRoot1(self):
        return (-self.b+ math.sqrt(((self.b ** 2) - (4 * self.a * self.c))) / (2*self.a))

    def getRoot2(self):
        return (-self.b - math.sqrt(((self.b ** 2) - (4 * self.a * self.c))) / (2*self.a))

def main() :
    print("Type in a number that represents a, b, and c!")
    qFormula = QuadraticFormula(int(input()), int(input()), int(input()))
    if(qFormula.getDiscrimant() > 0):
        print("The answer for Root 1", qFormula.getRoot1())
        print("The answer for Root 2", qFormula.getRoot2())
    else:
        print("The equation has no roots")
main()
