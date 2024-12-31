n = int(input("ENTER A NUMBER"))
x = ""
while(n>0):
    y = n%2
    x = str(y) + x
    n = n//2
print(int(x))


