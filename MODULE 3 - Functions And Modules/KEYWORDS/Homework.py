x = int(input("Please enter bill amount "))
y = int(input("Please enter the amount you paid"))
def calculate(x,y):
    if (y>x):
        return("Change =",{y - x})
    
    elif (x>y):
        return
    
    else:
    print("There is no amount left to pay")

