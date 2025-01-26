
x = int(input("Please enter bill amount "))
y = int(input("Please enter the amount you paid "))
def calculate(x,y):
    if (y>x):
        return("Change =",{y - x})
    
    elif (x>y):
        return ("Due Amount",{x - y})
    
    else:
        return("There is no amount left to pay")
    

