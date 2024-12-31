def add(p,q):
    return p + q

def subtract(p,q):
    return p - q

def multiply(p,q):
    return p * q

def divide(p,q):
    return p / q



print("PLEASE SELECT OPERATION: ")
print("a. ADD")
print("b. SUBTRACT")
print("c. MULTIPLY")
print("d. DIVIDE")

choice = input("PLEASE ENTER CHOICE, a/b/c/d ")
p = int(input("ENTER FIRST NUMBER: "))
q = int(input("ENTER SECOND NUMBER: "))

if (choice == "a"):
    print (p,"+",q,"=",add(p,q))
elif (choice == "b"):
    print (p,"-",q,"=",subtract(p,q))
elif (choice == "c"):
    print (p,"*",q,"=",multiply(p,q))
elif (choice == "d"):
    print (p,"/",q,"=",divide(p,q))
else:
    print(" ERROR! NOT DEFINED")
