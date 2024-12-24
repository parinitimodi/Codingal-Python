import turtle

turtle.Screen().bgcolor ("turquoise")
turtle.Screen().setup(500,500)

polygon = turtle.Turtle()

num_sides = 6
side_length = 90

angle = 360.0/num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
