import turtle

my_wn = turtle.Screen()

my_wn.bgcolor("hot pink")

my_wn.title("TURTLE!!")


mypen = turtle.Turtle()


size = 0

while True:
    for i in range(4):
        mypen.fd(size+1)
        mypen.left(90)
        
        size = (size - 5)
    
    size = (size + 1)

turtle.done()
    






