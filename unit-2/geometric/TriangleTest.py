from Triangle import Triangle

def main():
    print("Type the color, filled (1 or 0), and the three sides remaining")
    triangleObject = Triangle(input(), bool(input()), float(input()), float(input()), float(input()))
    print(triangleObject)

main()