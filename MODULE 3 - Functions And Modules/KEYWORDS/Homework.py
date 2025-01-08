x = int(input("Please enter bill amount "))
y = int(input("Please enter the amount you paid"))

if (y>x):
    print("Change =",y - x)

elif (x>y):
    print("The amount left to pay is ",x - y)

else:
    print("There is no amount left to pay")