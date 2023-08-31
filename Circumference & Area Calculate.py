import os


class Circle:
    def __init__(self, Radius):
        self.Radius = Radius

    def CalculateArea(self):
        return (3.14 * (self.Radius ** 2))

    def CalculateCircumference(self):
        return (2 * 3.14 * self.Radius)


class Rectangular:
    def __init__(self, Length, Width):
        self.Length = Length
        self.Width = Width

    def CalculateArea(self):
        return (self.Length * self.Width)

    def CalculateCircumference(self):
        return (2 * (self.Length + self.Width))
    

class Triangle:
    def __init__(self, Base, Height):
        self.Base = Base
        self.Height = Height

    def CalculateArea(self):
        return ((self.Base * self.Height) / 2)

    def CalculateCircumference(self, Side1, Side2, Side3):
        return Side1 + Side2 + Side3


def Program():
    os.system("cls")
    Choice = input("1. Circle\n2. Rectangular\n3. Triangle\n4. Exit\n\nEnter your choice: ")
    if (Choice == "1"):
        os.system("cls")
        Radius = float(input("Enter radius: "))
        circle = Circle(Radius)
        print(f"\n\nArea = {str(circle.CalculateArea())}\nCircumference = {str(circle.CalculateCircumference())}")
        Choice = input("\n\n\nPress any key to back... ")
        Program()
    elif (Choice == "2"):
        os.system("cls")
        Length = float(input("Enter length: "))
        Width = float(input("Enter width: "))
        rectangular = Rectangular(Length, Width)
        print(f"\n\nArea = {str(rectangular.CalculateArea())}\nCircumference = {str(rectangular.CalculateCircumference())}")
        Choice = input("\n\n\nPress any key to back... ")
        Program()
    elif (Choice == "3"):
        os.system("cls")
        Base = float(input("Area:\nEnter base: "))
        Height = float(input("Enter height: "))
        triangle = Triangle(Base, Height)
        Side1 = float(input("\nCircumference:\nEnter side 1: "))
        Side2 = float(input("Enter side 2: "))
        Side3 = float(input("Enter side 3: "))
        print(f"\n\nArea = {str(triangle.CalculateArea())}\nCircumference = {str(triangle.CalculateCircumference(Side1, Side2, Side3))}")
        Choice = input("\n\n\nPress any key to back... ")
        Program()
    elif (Choice == "4"):
        exit()
    else:
        Program()



Program()