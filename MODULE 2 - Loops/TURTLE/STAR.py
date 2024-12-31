import turtle

turtle.Screen().bgcolor ("pink")
turtle.Screen().setup(600,600)

star = turtle.Turtle()

num_sides = 3
side_length = 100

angle = 360.0/num_sides

for i in range(num_sides):
    star.forward(side_length)
    star.right(angle)

star.penup()

star.right(90)

star.forward(50)

star.left(90)

star.pendown()

for j in range(num_sides):
    star.forward(side_length)
    star.left(angle)

turtle.done()
