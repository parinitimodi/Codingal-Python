import turtle

my_wn = turtle.Screen()

my_wn.bgcolor("red")

my_wn.title("TURTLE!!")

mypen = turtle.Turtle()

num_sides = 4
side_length = 200

angle = 360.0/num_sides

mypen.circle

for i in range(num_sides):
    mypen.forward(side_length)
    mypen.right(angle)
mypen.up()
mypen.goto(100,-200)

mypen.circle(100)
mypen.down()
mypen.circle(100)
    


