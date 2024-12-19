print("HALF PYRAMID PATTERN OF (*):")
n = int(input("ENTER NUMBER OF ROWS:"))

for i in range (n):
    for j in range (i + 1):
        print("*", end = "")
    print()
