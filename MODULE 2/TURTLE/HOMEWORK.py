import turtle

my_wn = turtle.Screen()

my_wn.bgcolor("red")

my_wn.title("TURTLE!!")

mypen = turtle.Turtle()

num_sides = 4
side_length = 200

angle = 360.0/num_sides

for i in range(num_sides):
    mypen.forward(side_length)
    mypen.right(angle)
    mypen
   
 
turtle.circle(100)



