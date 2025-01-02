import math

radius = float(input("ENTER THE RADIUS OF THE CIRCLE: "))
CIRCUMFERENCE = 2*math.pi*radius
print("The Circumference of the circle is ",CIRCUMFERENCE, ".")


side = float(input("ENTER THE LENGTH OF A SIDE OF A SPQUARE: "))
perimeter = side*4
print("The Perimeter of the square is",perimeter)


length = float(input("ENTER THE LENGTH OF THE RECTANGLE: "))
breadth = float(input("ENTER THE BREADTH OF THE RECTANGLE: "))
perimeterofrectangle = (length + breadth)*2
print("The Perimeter of the rectangle is",perimeterofrectangle)


sideoftriangle = float(input("ENTER THE LENGTH OF THE SIDE OF THE TRIANGLE: "))
perimeteroftriangle = sideoftriangle*3
print("The Perimeter of the triangle is", perimeteroftriangle)

print("Perimeter of all 5 shapes are done.")